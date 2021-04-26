# Default Python Library OS
import os
import json
# Importing Flask class, render_template to use HTML templates
# Request to use method POST, flash for flashed messages
from flask import Flask, render_template, request, flash
# Import env is exists. Ignore error as "not used"
if os.path.exists("env.py"):
    import env

# Creating the Flask instance
# By convention, the instance is called app, secret key for flash
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


# Route decorator to tell Flask what URL should trigger the function
# The render_template take the contents of an HTML and render it to the screen.
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


# The < > dedscribes items passed from the URL
@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if member_name == obj["url"]:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


"""The 'host' will be set to os.environ.get("IP"),
and I will set a default of "0.0.0.0".
We're using the os module from the standard library to get the 'IP'
environment variable if it exists, but set a default value if it's not found.
It will be the same with 'PORT', but this time, we're casting it as an integer,
and I will set that default to "5000",
which is a common port used by Flask.
We also need to specify "debug=True",
because that will allow us to debug our code
much easier during the development stage.
The word 'main' wrapped in double-underscores (__main__) is the name of the
default module in Python. """
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
"""You should only have debug=True while testing your application in
development mode, but change it to debug=False
before you submit your project."""
