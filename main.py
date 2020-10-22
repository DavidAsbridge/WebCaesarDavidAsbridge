
from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask('app')
app.config['DEBUG'] = True



@app.route("/")
def index():
  template = jinja_env.get_template('user_signup.html')
  return template.render()

@app.route("/", methods=['POST'])
def vailidate():
  name = request.form['username']
  email = request.form['email']
  password = request.form['password']
  confirm = request.form['confirm']
  nameerror = ""
  emailerror = ""
  passworderror = ""
  confirmerror = ""
  template = jinja_env.get_template('user_signup.html')
  

  def validate(entry):
    if len(str(entry)) == 0:
      return False
    else:
      return True

  if not validate(name):
    nameerror = "Invalid Username"
    password = ""
    confirm = ""
    return template.render(username = name, email = email, password = password, confirm = confirm, nameerror = nameerror, emailerror = emailerror, passworderror = passworderror, confirmerror = confirmerror)
  if not validate(email):
    emailerror = "Invalid Email"
    password = ""
    confirm = ""
    return template.render(username = name, email = email, password = password, confirm = confirm, nameerror = nameerror, emailerror = emailerror, passworderror = passworderror, confirmerror = confirmerror)
  if not validate(password):
    passworderror = "Invalid Password"
    password = ""
    confirm = ""
    return template.render(username = name, email = email, password = password, confirm = confirm, nameerror = nameerror, emailerror = emailerror, passworderror = passworderror, confirmerror = confirmerror)
  if not validate(confirm):
    confirmerror = "Please Confirm Your Password"
    password = ""
    confirm = ""
    return template.render(username = name, email = email, password = password, confirm = confirm, nameerror = nameerror, emailerror = emailerror, passworderror = passworderror, confirmerror = confirmerror)
  
  
  
  
  else:
    template = jinja_env.get_template('welcome_screen.html')
    return template.render(username = name)

  



app.run(host='0.0.0.0', port=8080)