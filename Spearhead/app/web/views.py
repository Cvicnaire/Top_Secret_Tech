
from flask import Blueprint, current_app, jsonify, render_template, flash, redirect, url_for
from flask_restful import Api
from marshmallow import ValidationError
from app.extensions import apispec
from app.api.resources import UserResource, UserList
from app.api.schemas import UserSchema
from app.forms import ContactForm


""" Endpoints for the Webpage"""


# Define a new Blueprint for the web views
web_blueprint = Blueprint("web", __name__)

@web_blueprint.route('/', endpoint='home')
def home():
    navigation = [
        {'name': 'mission statement', 'endpoint': 'web.base'},
        {'name': 'form', 'endpoint': 'web.form'},
        {'name': 'browsing', 'endpoint': 'web.browse'}
    ]
    return render_template('index.html', navigation=navigation)

@web_blueprint.route('/base', endpoint='base')
def page1():
    return render_template('base.html')


# Route to Handle form Submission
@web_blueprint.route('/form', methods=['GET', 'POST'])
def form():
    form = ContactForm()
    if form.validate_on_submit():  # Corrected the typo
        flash('Form Submitted Successfully', 'success')
        return redirect(url_for('web_blueprint.form'))  # Using the blueprint name explicitly
    return render_template('workflow_forms.html', form=form)

# route to browse result files
@web_blueprint.route('/form')
    def browsing():
    

# We need to create 