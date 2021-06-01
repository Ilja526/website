from flask import Flask, render_template
app = Flask('app')


@app.route('/')
def main():
  return render_template("main.html")


@app.route('/login')
def login():
  return render_template("login.html")

@app.route('/sign')
def signup():
  return render_template("signup.html")

@app.route('/register')
def register():
  return render_template("register.html")

app.run(host='0.0.0.0', port=8080)