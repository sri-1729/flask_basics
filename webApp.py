from flask import Flask, render_template, request
import show

x = Flask("first")

@x.route("/") #what Url should trigger our function
def home():
	return render_template("index.html")

@x.route("/", methods=['POST'])
def display():
	roll = request.form['roll']
	li = show.roll(roll)
	
	#dic = {'Name': li[0], 'Id' : li[1], 'Rank': li[2], 'CGPA' : li[3]}
	return render_template("result.html", li = li)
