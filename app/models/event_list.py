from app.models.event import *

event1 = Event("2020-12-12", "Python Lesson", 20, "Computing room 1", "Learn about Python", True)
event2 = Event("2021-10-10", "French Lesson", 15, "French room 2", "Basic French", False)
events = [event1, event2]

def add_new_event(event):
    events.append(event)