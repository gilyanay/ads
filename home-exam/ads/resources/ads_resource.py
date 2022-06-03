
from flask import request
import requests
import xmltodict

from resources.base_resource import BaseResource


class AdsListResource(BaseResource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self):
        try:
            args = request.args.to_dict()
            user_data = self.UserData(**args)
            ad = self.get_ad()
            self.update_redis("ad_requests", user_data)
        except ValueError as ve:
            return str(ve), 400
        except ConnectionError as ce:
            return str(ce), 400
        except Exception as e:
            return str(e), 501
        return ad, 200

    @staticmethod
    def get_ad():
        response = requests.get(url="https://6u3td6zfza.execute-api.us-east-2.amazonaws.com/prod/ad/vast")
        if response.status_code != 200:
            raise ConnectionError("there seems to have a problem ")
        data_dict = xmltodict.parse(response.text)
        if not data_dict:
            raise ValueError("there are no ads at this moment")
        return response.text



