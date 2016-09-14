from flask import render_template, request
from FlaskDemo import app

# @app.route('/demo/')

def result_service(nm, ps):
   if nm:
      print nm
      return True
   else:
      return  False
