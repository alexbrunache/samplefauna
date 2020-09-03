from src.fauna import getfam
from flask import Flask

app = Flask(__name__)


@app.route("/users")
def getall(self):
    return getfam()
