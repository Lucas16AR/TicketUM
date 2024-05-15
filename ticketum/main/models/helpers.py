from .. import db

# Tabla intermedia para la relación many-to-many
guest_event = db.Table('guest_event',
    db.Column('guest_id', db.Integer, db.ForeignKey('guests.id'), primary_key=True),
    db.Column('event_id', db.Integer, db.ForeignKey('events.id'), primary_key=True)
)