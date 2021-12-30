# using flask_restful
#pip3 install flask-restful

from flask import Flask, jsonify, request
from flask_restful import Resource, Api

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class predict(Resource):
	def get(self,n=0,p=0,k=0,t=0,h=0,ph=0,rain=0):
		return jsonify({'data':{'N':n,'P':p,'K':k,'Temp':t,'Hum':h,'Ph':ph,'Rain':rain}})
	def post(self):
		data=request.get_json()
		return jsonify({'data': data}), 201

# adding the defined resources along with their corresponding urls
api.add_resource(predict,'/predict/<int:n>&<int:p>&<int:k>&<int:t>&<int:h>&<int:ph>&<int:rain>')

# driver function
if __name__ == '__main__':
	app.run(debug = True)
