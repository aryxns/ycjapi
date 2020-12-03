from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import api

hn = api.HackerNews()

DEBUG = True

# instantiate the app
app = Flask(__name__)

@app.route('/main', methods=["GET", "POST", "OPTIONS"])
def get_main():
	if request.method == "OPTIONS":
		return _build_cors_prelight_response()
	elif request.method == "GET":
		newlist = []
		for post in hn.jobs(limit=10):
			answer = {
				"title": post.title,
				"link": post.link,
				"content": post.content
			}
			newlist.append(answer)
		return _corsify_actual_response(jsonify(newlist))
	elif request.method == "POST":
		mylist = []
		search = request.get_json('search')
		role = search['search']
		for post in hn.jobs():
			if str(role) in str(post.title):
				result = {
					"title": post.title, 
					"link" : post.link,
					"content" : post.content
				}
				mylist.append(result)
		return _corsify_actual_response(jsonify(mylist)

def _build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == '__main__':
	app.run()
