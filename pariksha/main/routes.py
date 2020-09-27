from flask import render_template,redirect,Blueprint

main = Blueprint("main",__name__,template_folder="templates")

@main.route("/")
def welcome():
    return render_template("welcome.html")