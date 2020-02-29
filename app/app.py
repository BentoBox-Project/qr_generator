from flask import Flask
from flask_restful import Resource, Api
from . import util

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        text = "algo"
        qr_code = util.get_qr_code(text)
        if qr_code:
            print(qr_code)
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run()
