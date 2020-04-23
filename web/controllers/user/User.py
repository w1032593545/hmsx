  
from flask import Blueprint,render_template


router_user = Blueprint('user_page',__name__)

@router_user.route("/login")
def login():
    return render_template('user/login.html')