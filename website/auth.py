from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
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
            flash('account created!', category='success')
    return render_template('sign_up.html')
