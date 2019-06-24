from flask import Blueprint, render_template, flash, current_app
from flask_login import login_required, current_user

from src.channelry.models import db
from src.channelry.models.auth import User
from src.channelry.forms.profile import (
    EditEmailForm, EditNameForm, EditPasswordForm
)
from src.channelry import helper_email

profile_bp = Blueprint('profile', __name__)


@profile_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def index():
    edited = False
    form_email = EditEmailForm(prefix='form_email')
    form_name = EditNameForm(prefix='form_name')
    form_password = EditPasswordForm(prefix='form_password')

    if form_email.submit.data:
        if form_email.validate_on_submit():
            old_email = current_user.email
            new_email = form_email.email.data
            if new_email == old_email:
                errors = ['New email should be different from old email']
                form_email.email.errors = errors
            else:
                user = User.query.filter_by(email=new_email).first()
                if user:
                    form_email.email.errors = ['Email is already taken']
                else:
                    helper_email.send_change_email(current_user, new_email)
                    message = "To finish changing your email address, " \
                        f"we've sent an email to {old_email}. " \
                              "Simply click the button in the email to " \
                              "complete the process."
                    flash(message, 'success')

        if form_email.errors:
            flash('Failed to change email. Please try again.', 'danger')

    elif form_name.submit.data:
        if form_name.validate_on_submit():
            new_name = form_name.name.data
            if new_name == current_user.name:
                errors = ['New name should be different from old name']
                form_name.name.errors = errors
            elif new_name:
                current_user.name = new_name
                flash('Successfully changed your Channelry name.', 'success')
                edited = True
            else:
                flash('Please provide a valid name', 'danger')

        if form_name.errors:
            flash('Failed to change name. Please try again.', 'danger')

    elif form_password.submit.data:
        if form_password.validate_on_submit():
            old_password = form_password.old_password.data
            new_password = form_password.new_password.data

            if old_password and new_password:
                if old_password == new_password:
                    msg = 'New password should be different from old password'
                    flash(msg, 'danger')
                elif current_user.password_match(old_password):
                    hashed_password = current_user.password_hash(new_password)
                    current_user.password = hashed_password.decode('utf8')
                    helper_email.send_change_password_success(current_user)
                    edited = True
                    msg = 'Successfully changed your Channelry password'
                    flash(msg, 'success')
                else:
                    flash('Wrong old password.', 'danger')

        if form_password.errors:
            flash('Failed to change password. Please try again.', 'danger')

    if edited:
        db.session.add(current_user)
        db.session.commit()

    forms = {
        'form_email': form_email,
        'form_name': form_name,
        'form_password': form_password
    }
    return render_template('profile/index.html', **forms)
