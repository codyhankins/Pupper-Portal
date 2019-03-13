
Everything in this directory is the web interface extension built on top
of our ontology. We used Flask, a python-based web framework, 
along with owlready2, to make an online interface to interact with 
our underlying ontology. This program prompts the user with a 
number of questions that are translated into OWL queries. The 
resulting matches and relevant properties are displayed on the 
result page. 

To run the online quiz:

1. Run the command "python run.py" inside the web_app directory
    - this will start the web server
2. Go to the web address listed on the command line. Use your browser
    - the address is http://127.0.0.1:5000/
3. The web interface for the ontology should be good to go

Notes: You may need to install owlready2 on your local machine. Run:
"pip install owlready2" to get the necessary package for the
ontology to work properly. 
