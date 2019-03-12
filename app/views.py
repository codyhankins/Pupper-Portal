from flask import render_template
from flask import request
from app import app
from owlready2 import *

def underscore_to_camelcase(name):
    components = name.split('_')
    ret = ''
    for i, c in enumerate(components):
        if i == len(components) - 1:
            ret += c.capitalize()
        else:
            ret += c.capitalize() + ' '
    return ret

def camel_case_split(identifier):
    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
    result = [m.group(0) for m in matches]
    ret = ''
    for word in result:
        ret += word + ' '
    return ret[:-1]

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


        print(size)
        print(allergic)
        print(active)
        print(trainable)
        print(others)
        print(shed)
        print(kids)
        print(apartment)
        print(protective)
        print(groom)
        # create candidate list of dogs from ontology results
        onto_path.append('')
        onto = get_ontology('file://pupper_ontology_final.owl')
        onto.load()

        full_breed_list = onto.search(type = onto.Dog)

        final_results = full_breed_list
        size_list = []
        if len(size) > 0:
            for selected_size in size:
                results = onto.search(size = selected_size)
                for breed in results:
                    size_list.append(breed)
            final_results = list(set(final_results) & set(size_list))

        if len(allergic) > 0:
            if allergic[0] == 'yes':
                results = onto.search(hypoallergenic = True)
                final_results = list(set(results) & set(final_results))

        energy_list = []
        if len(active) > 0:
            for selected_energy in active:
                results = []
                print(selected_energy)
                matched_energy = underscore_to_camelcase(selected_energy)
                print(matched_energy)
                results = onto.search(energy = matched_energy)
                for breed in results:
                    energy_list.append(breed)
            final_results = list(set(final_results) & set(energy_list))

        trainable_list = []
        if len(trainable) > 0:
            for selected_trainability in trainable:
                results = []
                matched_trainability = underscore_to_camelcase(selected_trainability)
                results = onto.search(trainability = matched_trainability)
                for breed in results:
                    energy_list.append(breed)
            final_results = list(set(final_results) & set(energy_list))

        other_dogs_list = []
        if len(others) > 0 and others[0] == 'yes':
            other_dogs_answer = ['Yes', 'With Supervision']
            for selected_others in other_dogs_answer:
                results = onto.search(good_with_dogs = selected_others)
                for breed in results:
                    other_dogs_list.append(breed)
            final_results = list(set(other_dogs_list) & set(final_results))

        shedding_list = []
        if len(shed) > 0:
            shedding_answer = []
            if not shed[0] == 'yes':
                if shed[0] == 'occasional':
                    shedding_answer = ['Seasonal', 'Infrequent']
                elif shed[0] == 'no':
                    shedding_answer = ['Infrequent']
                for selected_shedding in shedding_answer:
                    results = onto.search(shedding = selected_shedding)
                    for breed in results:
                        shedding_list.append(breed)
                final_results = list(set(shedding_list) & set(final_results))

        if len(kids) > 0 and kids[0] == 'yes':
            results = onto.search(good_family_dog = True)
            final_results = list(set(results) & set(final_results))

        if len(apartment) > 0 and apartment[0] == 'yes':
            results = onto.search(good_apartment_dog = True)
            final_results = list(set(results) & set(final_results))

        if len(protective) > 0 and protective[0] == 'yes':
            results = onto.search(good_guard_dog = True)
            final_results = list(set(results) & set(final_results))

        grooming_list = []
        if len(groom) > 0:
            for selected_grooming in groom:
                results = []
                matched_grooming = underscore_to_camelcase(selected_grooming)
                results = onto.search(grooming = matched_grooming)
                for breed in results:
                    grooming_list.append(breed)
            final_results = list(set(grooming_list) & set(final_results))

        final_results_dict = {}
        for breed in final_results:
            name = camel_case_split(breed.name)
            if name not in final_results_dict:
                final_results_dict[name] = []
            final_results_dict[name].append(breed.description)
            final_results_dict[name].append(breed.personality)
            final_results_dict[name].append(breed.image_url)
        
        #print(final_results_dict)
        dogs_to_display = {k: final_results_dict[k] for k in list(final_results_dict)[:10]}
        # query the breed dictionary here to get the individual dog qualities
        #dogs_to_display = 
        # pass the collection of dictionaries to the render template method

        return render_template("results.html", dog_list = dogs_to_display, total_dogs = len(final_results_dict))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/results')
def results():
    return render_template("results.html")
