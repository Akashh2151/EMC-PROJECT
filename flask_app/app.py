from flask import Flask
app=Flask(__name__) 
from controller import*


@app.route("/")
def welcome():
    return "hellow Akash"


if __name__ == "__main__":
    app.run(debug=True)