'''
Templates:-
different delimeters are used in templates 
1){{ }}:-expressions to print on the template output
2){% %}:-used for statements,loops etc
3){# #}:-used for comments

Q1]write a program which consists of html file display hello name it also 
consists of python file which is used to render the template

'''
'''
from flask import Flask, redirect, url_for,render_template
app = Flask(__name__)

@app.route('/hello/<name>')
def index(name):
   return render_template('index.html',name=name)

if __name__ == '__main__':
    app.run(debug=True)'''



#create html file which displays result pass if the marks are >40 otherwise displays fail


'''
from flask import Flask, redirect, url_for,render_template
app = Flask(__name__)

@app.route('/hello/<int:mark>')
def index(mark):
   return render_template('index.html',marks=mark)

if __name__ == '__main__':
    app.run(debug=True)'''



#consider a dictionary of key value pair of subject and marks and render the dictionary with html page


from flask import Flask, redirect, url_for,render_template
app = Flask(__name__)

@app.route('/hello')
def hello():
    dict = {'c':50,'c++':60,'math':70}
    return render_template('index.html',dict=dict)

if __name__ == '__main__':
    app.run(debug=True)