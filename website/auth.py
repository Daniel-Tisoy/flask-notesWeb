from flask import Blueprint, render_template, request

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
            pass
        elif len(first_name)<2:
            pass
        elif password1 != password2:
            pass
        elif len(password1)<7:
            pass
        else:
            #add user to database
            pass
    return render_template('sign_up.html')
