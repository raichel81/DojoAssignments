from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/', methods=['POST'])
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/process', methods=['GET'])
def process():
  username = request.form['name']
  print username
  return redirect('/')
app.run(debug=True) # run our server