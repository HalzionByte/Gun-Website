from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def my_func1():
    return render_template('index.html')

@app.route('/home')
def my_func():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/rifles')
def rifles():
    return render_template('Ar.html')

@app.route('/shotguns')
def shotguns():
    return render_template('Shotgun.html')

@app.route('/pistols')
def pistols():
    return render_template('pistol.html')

if __name__== "__main__":
    app.run(debug=True)