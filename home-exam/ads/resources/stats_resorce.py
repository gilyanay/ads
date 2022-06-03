from flask import request

from resources.base_resource import BaseResource


class StatsResource(BaseResource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self):
        filt = request.args.to_dict()
        try:
            impressions, ad_requests = self.get_data_from_redis(filt)
        except ValueError as ve:
            return str(ve), 400
        return {
            "impressions": impressions,
            "ad_requests": ad_requests,
            "fill_rate": impressions/ad_requests if ad_requests > 0 else 0
        }

    def get_data_from_redis(self, filt):
        impressions = self._redis.get(f"impressions_for_{filt['filter_type']}")
        impressions = int(impressions) if impressions else 0

        ad_requests = self._redis.get(f"ad_requests_for_{filt['filter_type']}")
        ad_requests = int(ad_requests) if ad_requests else 0
        return impressions, ad_requests
