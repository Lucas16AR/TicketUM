from .. import db

class Guest(db.Model):
    '''
    Model of the Entity Guest
    '''
    __tablename__ = 'guests'
    id = db.Column(db.Integer, primary_key=True)
    guest_code = db.Column(db.String(255), nullable=False, unique=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    dni = db.Column(db.Integer, nullable=False)
    
    inscriptions = db.relationship('Inscription', back_populates='guest')

    def __repr__(self):
        return f'<Guest {self.name}> - {self.email} - {self.phone} - {self.dni} - {self.guest_code}'
