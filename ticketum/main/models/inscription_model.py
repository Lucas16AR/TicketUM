from .. import db

class Inscription(db.Model):
    '''
    Model of the Entity Inscription
    '''
    __tablename__ = 'inscriptions'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(255), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)

    event = db.relationship('Event', backref=db.backref('inscriptions', lazy='dynamic'))
    guest = db.relationship('Guest', backref=db.backref('inscriptions', lazy='dynamic'))

    def __repr__(self):
        return f'<Inscription {self.id} - {self.status} - {self.event} - {self.guest}>'