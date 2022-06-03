from flask import Flask
from flask_restplus import Api
from resources import AdsListResource, ImpressionsResource, StatsResource

app = Flask(__name__)
api = Api(app)

api.add_resource(AdsListResource, "/ads")
api.add_resource(ImpressionsResource, "/impressions")
api.add_resource(StatsResource, "/stats")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

