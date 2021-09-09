from website.models import User
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
# never store passwords in plain text
from werkzeug.security import generate_password_hash, check_password_hash
# hash is that no have inverse(like an inverse of a funcion)
# given f:x -> y you can't get f'(f'=?)
# so you can only check, given a password, this is equals to hashed password
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    #print(data)
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return '<p>this will be a logout template</p>'


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')


        #checking the information is valid
        if len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(first_name)<2:
            flash('First name must be greater than 1 character', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1)<8:
            flash('password must be at least 8 characters', category='error')
        else:
            #add user to database
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))

            #add to database
            db.session.add(new_user)
            #commit
            db.session.commit()
            flash('account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template('sign_up.html')
