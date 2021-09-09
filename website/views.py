from flask import Blueprint, render_template, jsonify
from flask.globals import request
from flask.helpers import flash
from flask_login import login_required, current_user
from .models import Note
from . import db

import json #js request return a json object


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required #the home is aviable for logged users
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note)<1:
            flash('Note is too short!', category='error')

        else:
            #add note
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template('home.html', user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    data = json.loads(request.data)
    noteId = data['noteId']
    note = Note.query.get(noteId)

    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            
    return jsonify({})
