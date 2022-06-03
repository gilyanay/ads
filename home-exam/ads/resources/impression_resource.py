from resources.base_resource import BaseResource
from flask import request


class ImpressionsResource(BaseResource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def post(self):
        user_data = self.UserData(**request.json)
        self.update_redis("impressions", user_data)
        return {}, 200
