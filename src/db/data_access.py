from sqlalchemy import and_, func
#from db.classes import HistoriqueDemande
#from app.main import db
import pandas as pd
from src.db.classes import HistoriqueDemande
from src.app.main import db



def get_demande_jour(jour):
    return HistoriqueDemande.query.filter(HistoriqueDemande.date == jour).first().demande_reelle


def get_demande_intervalle(debut, fin):
    return db.session.query(func.sum(HistoriqueDemande.demande_reelle)).filter(
        and_(HistoriqueDemande.date <= fin, HistoriqueDemande.date >= debut)).first().__getitem__(0)


def get_demande_predite_jour(jour):
    return HistoriqueDemande.query.filter(HistoriqueDemande.date == jour).first().demande_prevue


def get_demande_predite_intervalle(debut, fin):
    return db.session.query(func.sum(HistoriqueDemande.demande_prevue)).filter(
        and_(HistoriqueDemande.date <= fin, HistoriqueDemande.date >= debut)).first().__getitem__(0)


def get_historique_demande_reelle():
    return pd.read_sql_table('historique_demande', db.session.connection())[["date", "demande_reelle"]]


def set_demande_predite(prediction):
    for p in prediction.iterrows:
        h = HistoriqueDemande(date=p['date'], demande_prevue=p['demande_prevue'])
        db.session.add(h)
        db.session.commit()


def set_demande_reelle(jour, demande):
    h = HistoriqueDemande.query.filter_by(date=jour).one()
    h.demande_reelle = demande
    db.session.commit()
