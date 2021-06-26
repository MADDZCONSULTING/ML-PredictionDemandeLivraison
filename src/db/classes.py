from app.main import db


class HistoriqueDemande(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date(), unique=True, nullable=False)
    demande_reelle = db.Column(db.Integer, unique=False, nullable=True)
    demande_prevue = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return '<date %s|demande_reelle %s|demande_prevue %s>' % (self.date, self.demande_reelle, self.demande_prevue)
