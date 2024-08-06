from flask import Blueprint, render_template

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/')
def user_profile():
    # Example user data
    user_data = {
        'username': 'JohnDoe',
        'email': 'john.doe@example.com'
    }
    return render_template('user.html', **user_data)
