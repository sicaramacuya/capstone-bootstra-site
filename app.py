from flask import Flask,request, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    """A homepage for the website."""
    return render_template('home.html')

@app.route('/spacex')
def spacex_page():
    """A page for the spacex informtion."""
    return render_template('spacex.html')

@app.route('/ula')
def ula_page():
    """A page for the united launch alliance informtion."""
    return render_template('ula.html')

@app.route('/rocketlab')
def rocketlab_page():
    """A page for the rocket lab informtion."""
    return render_template('rocketlab.html')

if __name__ == '__main__':
    app.run(debug=True)