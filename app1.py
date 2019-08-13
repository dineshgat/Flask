'''from flask import Flask
app=Flask(__name__)

@app.route('/<name>')
def index(name):
    return 'Hello,{name}'

if __name__=='__main__':
    app.run(debug=True)'''

'''
#flask
Flask is a micro framework developed by Armin Ronacher he leads an international group of python named as pocco
flask is based on Werkzeug ,WSGI toolgit and jinja2 template engine both of these are Pocco projects
WSGI:
    This has been adopted as a standard for python web development it is a specification for universal interface 
i.e web server and web application
Werkzeug:
    It implements concepts such as request,response,objects and many other utility functions
it enables build-in web framework so flask uses Werkzeug as a basis for a framework
Jinja2 Template Engine:
    It is templatiing engine that combine template to certain data source to render dynamic web pages 
flask aims at keeping the core of an application simple and yet extensible flask doesn't have any
inbuilt abstraction layer for data handling nor does it have any validation support.However flask supports
such extensions to support different functionalities

flask is a name of module and Flask is a class present in a class module
flask constructor takes name of the current module,represented as __name__

route() function is a decorator which has two parameters (rule  and options) rule parameter is used for 
url binding with a function options parameter is used for listing of parameters to be forwarded to be underline 
ruled object

app.run() is used to run application on a web development server it has three parameters first is host
it is a name of the host to which we want listen on default is 127.0.0.1
Port-default port no is 5000
Options-its used to be forwarded to underline Werkzeug server 
debug parameter nis also used by default is set to false

Routing-
routing helps user to remember application url better  it is easy to access url instead of navigating from
 actual page 
 we can create url dynamically by adding variable parts to the rule parameter 
 
 #1:for example create url which consists of text hello followed by name
 Write a function which displays hello and name

'''

'''@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!!'%name
if __name__ == "__main__":
    HOST=environ.get('SERVER_HOST','localhost')
    try:
        PORT=int(environ.get('SERVER_HOST','5555'))
    except ValueError:
        PORT=5555
    app.run(HOST,PORT)'''

'''
from os import environ
from Flask_var_rules import app
from flask import Flask

app=Flask(__name__)
@app.route('/stud/<int:studno>')
'''

'''
url_var is used for dynamically building url
http methods:
get
post
put-it replaces all current representations of target resource with uploaded contents
delete-removes all current representations of target resource given by the url
'''


from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

if __name__ == '__main__':
   app.run(debug = True)


#Q2: