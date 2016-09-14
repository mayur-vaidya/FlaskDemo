from flask import render_template, request
from myfile import app
from FlaskDemo.view2 import result_service


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/demo/', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      nm = request.form['nm']
      ps = request.form['ps']
      value = result_service(nm , ps)
      print value
      task = {'user': nm, 'password': nm}
      #ls = ls.update(task)
      return str(task)