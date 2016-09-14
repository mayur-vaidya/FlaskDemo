from FlaskDemo import app
from flask import Flask, render_template, request, jsonify
from FlaskDemo.view2 import result_service

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/demo/', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      nm = request.form['nm']
      ps = request.form['ps']
      s = 'Please Enter some details!!!! You left the fields empty.'
      value = result_service(nm , ps)
      task = {'user': nm, 'password': ps}
      if value is True:
         return jsonify({'task': task })
      else:
         return s
