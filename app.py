from flask import Flask
import test
app = Flask(__name__)

@app.route("/")
def hello():
    return "Help me, No! importing test "#+ str(3+test.test_function(3))
