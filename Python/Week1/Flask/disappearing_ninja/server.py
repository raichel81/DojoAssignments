from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/ninja')
def ninja():
    return render_template("ninja.html")
@app.route('/select_color', methods=['POST'])
def select_color():
  color = request.form['color']
  return redirect("/ninja/"+color)
@app.route('/ninja/<color>')
def show_pic(color):
	if( color == 'Blue'):
		return render_template("ninja.html",color='/static/leonardo.jpg')
	elif( color == 'Orange'):
		return render_template("ninja.html",color='/static/michelangelo.jpg')
	elif( color == 'Red'):
		return render_template("ninja.html",color='/static/raphael.jpg')
	elif( color == 'Purple'):
		return render_template("ninja.html",color='/static/donatello.jpg')	
	else:
		return render_template("ninja.html",color='/static/notapril.jpg')
app.run(debug=True) # run our server
