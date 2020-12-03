from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import api

hn = api.HackerNews()

DEBUG = True

# instantiate the app
app = Flask(__name__)
cors = CORS(app, resources={r"/main"}:{"origins":"https://ycjobs.vercel.app/"})

@app.route('/main', methods=["GET", "POST", "OPTIONS"])
def get_main():
	if request.method == "OPTIONS":
		return request.headers.add("Access-Control-Allow-Origin", "https://ycjobs.vercel.app/")
	elif request.method == "GET":
		request.headers.add("Access-Control-Allow-Origin", "https://ycjobs.vercel.app/")
		newlist = []
		for post in hn.jobs(limit=10):
			answer = {
				"title": post.title,
				"link": post.link,
				"content": post.content
			}
			newlist.append(answer)
		return (jsonify(newlist))
	elif request.method == "POST":
		request.headers.add("Access-Control-Allow-Origin", "https://ycjobs.vercel.app/")
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
		return (jsonify(mylist)

if __name__ == '__main__':
	app.run()
