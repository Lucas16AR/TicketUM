from .. import db

class Guest(db.Model):
    __tablename__ = 'guests'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    dni = db.Column(db.Integer, nullable=False)

    # Relationship with Event
    events = db.relationship('Event', secondary='guest_event', backref='guests')

    def __repr__(self):
        return f'<Guest {self.name}>'