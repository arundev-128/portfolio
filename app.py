from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "Rooney in the house!"


if __name__ == "__main__":
  print("Inside IF")
  app.run(host='0.0.0.0', debug=True)
