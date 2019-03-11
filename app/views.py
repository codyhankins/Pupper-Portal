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

        # create candidate list of dogs from ontology results
        dogList = ['golden-retriever']
        
        # query the breed dictionary here to get the individual dog qualities

        # pass the collection of dictionaries to the render template method

        return render_template("results.html", dog_list = None)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/results')
def results():
    return render_template("results.html")
