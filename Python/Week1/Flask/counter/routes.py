from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'realsecret'

@app.route('/')
def index():
    if 'counts' not in session:
        session['counts'] = 1
    else:
        session['counts'] += 1
    print 'this is a session', session['counts']
    return render_template('index.html')

@app.route('/reload')
def reload_page():
    session['counts'] += 2
    print 'reload button clicked', session['counts']
    return render_template('index.html')

@app.route('/reset')
def reset_counter():
    print 'reset session to 1'
    session.clear()
    return redirect('/')

app.run(debug=True)