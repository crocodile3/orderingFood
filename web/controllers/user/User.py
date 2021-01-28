from flask import Blueprint
from flask import render_template

route_user = Blueprint('user_page', __name__)


@route_user.route("/login")
def login():
    return render_template( "user/login.html" )


@route_user.route("/list")
def list():
    return "user list page"


route_user.route("/edit")
def edit():
    return "user info edit"


route_user.route("register")
def register():
    return "user register"

