#!/usr/bin/env python3

from . import db
from flask_login import UserMixin
from .utils.blockchain import Transaction
from .utils.Wallet import Wallet

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	wallet = Wallet()
	
	def __repr__(self):
		return f'<User {self.username}>'
	
class Transport(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	host = db.Column(db.String(2048))
	port = db.Column(db.Integer)
	from_address = db.Column(db.String(2048))
	to_address = db.Column(db.String(2048))
	amount = db.Column(db.Float)
	password = db.Column(db.String(60), nullable=False)
	transaction = Transaction(from_address, to_address, amount)
	
	def __repr__(self):
		return f'<Transport {self.id}>'
	