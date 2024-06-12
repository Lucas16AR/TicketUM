from .. import db

class Event(db.Model):
    '''
    Model of the Entity Event
    '''
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    event_code = db.Column(db.String(255), nullable=False, unique=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

    inscriptions = db.relationship('Inscription', back_populates='event')

    def __repr__(self):
        return f'<Event {self.name}>'
