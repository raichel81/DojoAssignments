from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/dojos', methods=['POST'])
def create_ninja():
   print "Got Post Info"
   name = request.form['name']
   email = request.form['email']
   # redirects back to the '/' route
   return redirect('/')
@app.route('/ninjas')
def ninjas():
  return render_template('ninjas.html')
@app.route('/dojos')
def dojos():
  return render_template('dojos.html')
app.run(debug=True) # run our server