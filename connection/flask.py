from flask import Flask
app = Flask(__name__)

test = "hellow serever open to pyton" 
@app.route("/")
def main():
    return test

 
host = 'localhost'
port = '80'

if __name__ == "__main__":
    app.run(host, port)
