from eve import Eve

# my_sessting = {"DOMAIN" : {'user': {}}}
my_sessting = {"DOMAIN" : {}}
app = Eve(settings=my_sessting)

@app.route("/hello")
def hello():
    return "Hello World!"

app.run()