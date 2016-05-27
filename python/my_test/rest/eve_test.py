from eve import Eve

app = Eve()

@app.route("/hello")
def hello():
    return "Hello World!"

app.run()