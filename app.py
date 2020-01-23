from flask import Flask #from package import class
    
app = Flask(__name__) # creating an object of flask to give unique name to each file

# to tell our app what request its going to understand
# using decorators

@app.route('/') #http://www.google.com/
def home():
    return 'Hello World'

app.run(port = 5000)
        
    