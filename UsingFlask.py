#Flask is a micro web framework and it used to create an applications 
# flask=(jinja2)+(werkzeug)
#Jinja2 is a template engine for Flask. It's very easy to create templates with Jinja2.
#Jinja is used to create HTML,XML or other markup formats that are returned to the user via an HTML request.
#Django is a Python-based web application framework that follows the model-view-controller (MVC) pattern. It is an open source project that uses Python as its programming language.
#A template contains a series of placeholders that can be filled in with data to create a dynamic web page.
#A template contains variables which are replaced by the values which are passed in when the template is used or needed.
#Template inheritance is used to create a hierarchy of templates to inherit from. This allows us to reuse code across different pages, for example.
#Werkzeug(tool) WSGI toolkit is used to create a WSGI application.
#Flask uses it to handle the details of WSGI while provinding more structure and patterns for defining powerful applications
#WSGI is a standard for defining web applications. It is an application programming interface (API) that allows web servers to communicate with web applications.
#WSGI(Web Server Gateway Interface) is a standard that defines how web servers and web applications talk to each other. It is used to create web applications.
#HTTP (Hypertext Transfer Protocol) is a standard that defines how web servers and web applications talk to each other. It is used to create web applications.
#root() is used to start the server.
#HTTP methods: GET, POST, PUT, PATCH, DELETE, OPTIONS, HEAD, CONNECT, TRACE
#GET: used to get data from a server.
#POST: Used to send data to a server. The data sent to the server will not be displayed in the browser.
#PUT: Used to send data to a server. The data sent to the server will be displayed in the browser.
#PATCH: Used to send data to a server. The data sent to the server will be displayed in the browser.
#DELETE: Used to delete data from a server.
#OPTIONS: Used to get information about the capabilities of a server.
#HEAD: Used to get information about the capabilities of a server.
#CONNECT: Used to establish a connection with a server.
#TRACE: Used to get information about the capabilities of a server.
#Flask will figure out what those requests are dealing with and what they are asking.
# It will also figure out what response to send to the user.
#App rooting is used to map the specific URL with the associated function that is intended to perform some task.
#@app.route('/') is a python decorator that flask provides to assign URL's in our app to some functions.
#Python decorator is a function that takes another function as an argument, adds some functionality and returns the modified function.
#Flask applications can optionally be executed in debug mode.
#Flask will automatically reload the application if it detects any changes in the code.
#In order to run a Flask application, we need to import Flask and create an application object.
#Then we use @app.route() decorator to map the specific URL with the associated function that is intended to perform some task.
#In this mode (debug mode), two convenient modules of the server called the reloader and debugger are installed.
#When the reloader is enabled, the server will automatically reload the application if it detects any changes in the code.
#The url_for() function is used to generate URLs for the application.
#It takes two arguments - the name of the function and the arguments of the URL.
#This function is useful in  the sense that we can avoid hard-coding URLs into the templates by dynamically building them using this function.
#URL(Uniform Resource Locator) is a standardized way of identifying web resources.
#The @ sign followed by the name of the function is a decorator. A decorator is a design pattern that allows us to modify the behavior of the function or method that we are decorating.
#The @ sign is used before a function to indicate that it is a decorator.
#Every valid URL points to a unique resource.
#The url_for() function is used to generate URLs for the application.
#Templates in Flask are files that contain some HTML code as well as some Python code embedded within them.
#These Python code blocks are called Templates.
#In your app,you will use templates to render HTML which will display in the user's browser.
#In flask,Jinja is configured to autoescape any data that is provided in HTML templates.
#The template files will be stored in the templates folder inside the flask package.
#Flask comes with a very popular extension known as a flask login.
#Flask login is used to authenticate users.
#The flask login extension also provides the "remember me" functionality that allows users to stay logged in even if they close the browser.
#In layman's terms, the "remember me" functionality is used to remember the user's login credentials.
#This means that when the user logs into the application, the application will remember the user's login credentials.
#the four required items or demands are listed below:
#1. is_authenticated: checks if the user is authenticated or not. If yes then returns True else False.
#2. is_active: checks whether the user is active or not. If yes then returns True else False.
#3. is_anonymous: checks whether the user is anonymous or not. If yes then returns True else False.
#4. get_id: returns the unique id of the user. This is used to identify the user.
#User loader is used to load the user object.
#User session is used to store the user's login credentials.
#Flask-login uses sessions to keep track of the user's login credentials.
#A secret key is needed by Flask-login to keep track of the user's login credentials.
#This secret key should remain consistent across all instances of the application.
#user model is a collection of personal data associated with a spcific user.
#Flask protects you against one of the most common attacks known as Cross-Site scripting(XSS).
#Cross-Site scripting(XSS) is a type of attack that allows an attacker to inject malicious code into a web application.
#Flask uses the concept of blueprints for making application components and to greatly simplify how large applications work.
#The blueprints are used to organize the application's components.
#They make administration of very large flask applications easier and as such can be used to scale flask applications.
#Blueprint in flask also supports common patterns within an application or across applications
#It's a set of operations which can be registered on an application,even multiple times.
#Flask class has a redirect() function.
#redirect() function is used to send HTTP request to another URL.
#This function gets activated when a user clicks on a link.
#HTTP status codes represent responses from server to the client.
#The status codes are 200, 201, 204, 301, 302, 304, 400, 401, 403, 404, 500, 503.
#The 200 status code indicates that the request was successful.
#The 201 status code indicates that the request was successful and the resource was created.
#The 204 status code indicates that the request was successful and the resource was deleted.
#The 301 status code indicates that the resource has been moved.
#The 302 status code temporarily redirects the user to another URL.
#The 304 status code means that the resource has not been modified.
#The 400 Bad Request status code indicates that the server cannot or will not process the request due to something that is perceived to be a client error.
#The 401 Unauthorized status code indicates that the request requires user authentication.
#The 403 Forbidden status code indicates that the server understood the request but refuses to authorize it.
#The 404 Not Found status code indicates that the server can't find the requested resource.
#The 406 Not Acceptable status code indicates that the server cannot produce a response that accepts the request.
#The 415 Unsupported Media Type status code indicates that the server cannot produce a response that accepts the request.
#The 429 Too Many Requests status code indicates that the user has sent too many requests in a given amount of time ("rate limiting").
#The 500 Internal Server Error status code indicates that the server encountered an unexpected condition that prevented it from fulfilling the request.
#The 503 Service Unavailable status code indicates that the server is temporarily unable to service the request due to maintenance downtime or capacity problems.
#the syntax to use redirect function: flask.redirect(location,statuscode,response)
#location: where the user will be redirected to.
#statuscode: optional parameter, default value is 302.
#response: optional parameter,default value None.
#The get_id() method is used to get the unique id of the user.
#The abort() function is used to raise an exception. It takes two parameters: the error code and message.
#flask.abort(error code[, message])
#from flask import Flask, render_template#Importing Flask


#app = Flask(__name__)#Creating Flask App

#@app.route('/')#Defining route / which means if anyone goes to http://127.0.0.1:81/ it will go to index function@app.route('/')
#def index():#Defining index function
#    return 'Web App with Python Flask!'#Returning a string to the user
#app.run(host='0.0.0.0', port=81)#Running the app on localhost at port 81
# app.py

#from flask import Flask, render_template, request

#app = Flask(__name__,template_folder='D:/panag/Documents/ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ/template/')

#@app.route('/')
#def index():
#    return render_template('index2.html')

#@app.route('/submit', methods=['POST'])
#def submit():
#    name = request.form.get('name')
#    return f"Hello, {name}! Your form was submitted successfully."

#if __name__ == '__main__':
    #app.run(debug=True)
#    app.run(host='0.0.0.0', port=8081)
from flask import Flask, render_template, request
from ai_model import AIModel  # Your AI model implementation
import json

app = Flask(__name__,template_folder=r"/run/media/panos/SAMSUNG T7/panag/Documents/ΕΡΓΑΣΤΗΡΙΑΚΕΣ ΑΣΚΗΣΕΙΣ/template/")

# Initialize AI model
ai_model = AIModel()

@app.route('/')
def index():
    return render_template('input.html')

@app.route('/update', methods=['POST'])
def update_model():
    data = request.json
    ai_model.update(data)
    return 'OK'

@app.route('/graph')
def graph():
    # Generate data for the 3D graph
    graph_data = ai_model.get_graph_data()
    return render_template('graph.html', graph_data=json.dumps(graph_data))

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=8081)
