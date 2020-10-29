from flask import render_template, request
from app import app
from app.models.event_list import events, add_new_event
from app.models.event import *

@app.route('/')
def index():
    return render_template('index.html', title="Home", events=events)

@app.route('/add-event', methods=['POST'])
def add_event():
    event_date = request.form['date']
    event_name = request.form['event-name']
    event_number_of_guests = request.form['number-of-guests']
    event_room_location = request.form['room-location']
    event_description = request.form['description']
    new_event = Event(date=event_date, event_name=event_name, no_guests=event_number_of_guests, room_location=event_room_location, description=event_description)
    add_new_event(new_event)
    return render_template('index.html', title='Home', events=events)

    