from flask import Flask
from flask_restplus import Resource, Api, Namespace, fields
from Controllers.bootstrap import bootstrap
from flask_cors import CORS


app = Flask(__name__)
api = Api(app)
CORS(app)
ns_Search = Namespace('ContentSquare')
api.add_namespace(ns_Search)
searchPayload = ns_Search.model('Search Name', {
    'search' : fields.String(required=True, description="The name of the person you are looking for"),
    'dataType' : fields.String(required=True, description="What type of data are you looking for (i.e : 'users'"),
    'actionType' : fields.String(required=True, description="what action to perform (i.e : autocomplete or search item detail"),
})

@ns_Search.route('/search')
class Search(Resource):
    @ns_Search.expect(searchPayload)
    def post(self):
        factory = bootstrap("search", api.payload["actionType"])
        instance = factory(api.payload["search"], api.payload["dataType"])
        result = instance.exec()
        return result, 200, {'Access-Control-Allow-Origin' : '*'}

@ns_Search.route('/users/<string:id>')
class get(Resource):
    def get(self, id):
        factory = bootstrap("search", "byID")
        instance = factory(id, "users")
        result = instance.exec()
        return result, 200, {'Access-Control-Allow-Origin' : '*'}







if __name__ == '__main__':
    app.run()
