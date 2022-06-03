from dataclasses import dataclass

from flask_restplus import Resource
from redis import Redis


class BaseResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._redis = Redis(host='redis', port=6379, decode_responses=True)

    @dataclass
    class UserData:
        sdk_version: str
        user_name: str
        session_id: str
        platform: str
        country_code: str

    def update_redis(self, prefix: str, user: UserData):
        self._redis.incr(f"{prefix}_for_{user.sdk_version}")
        self._redis.incr(f"{prefix}_for_{user.user_name}")