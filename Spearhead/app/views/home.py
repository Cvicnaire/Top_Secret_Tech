from flask import Blueprint, render_template

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/')
def user_profile():
    return render_template('user.html')