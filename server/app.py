from flask import Flask, Request 

app = Flask(__name__) 

@app.route('/')
def default(): 
    return {"success": 200}

if __name__ == '__main__':
    app.debug = True
    app.run()