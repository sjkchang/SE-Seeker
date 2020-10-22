"""
models.py
====================================
The models that go into the database
"""

from . import db


class Internship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), index=True, nullable=False)
    term = db.Column(db.String(100), index=True, nullable=False)
    year = db.Column(db.Integer, index=True, nullable=False)
    additional_info = db.Column(db.String(800), index=True, nullable=False)
