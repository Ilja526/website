from flask import Flask, render_template
app = Flask('app')


@app.route('/')
def main():
  return render_template("main.html")


@app.route('/about')
def about():
  return render_template("about.html")


app.run(host='0.0.0.0', port=8080)