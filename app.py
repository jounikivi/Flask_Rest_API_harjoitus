from flask import Flask

app = Flask(__name__)

@app.route('/')
def help():
  return '<h1>hello world</h1>'

  if __name__ == '__main__':
    app.run(debug=True)