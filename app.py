from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world! This is my simple python app for my hands-on project'

if __name__ == '__main__':
    app.run()
