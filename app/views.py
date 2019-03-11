from flask import render_template
from flask import request
from app import app


ButtonPressed = 0        
@app.route('/button', methods=["GET", "POST"])
def button():
    if request.method == "POST":
        # all the data from the form can be found at request.form
        size = request.form.getlist('size')
        allergic = request.form.getlist('allergic')
        active = request.form.getlist('active')
        trainable = request.form.getlist('trainable')
        others = request.form.getlist('others')
        shed = request.form.getlist('shed')
        kids = request.form.getlist('kids')
        apartment = request.form.getlist('apartment')
        protective = request.form.getlist('protective')
        groom = request.form.getlist('groom')


        # create candidate list of dogs here to put in render for results page

        return render_template("results.html", ButtonPressed = ButtonPressed)
        # I think you want to increment, that case ButtonPressed will be plus 1.
    return render_template("button.html", ButtonPressed = ButtonPressed)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/results')
def results():
    return render_template("results.html")
