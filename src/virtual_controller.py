import argparse
import sys
import os
import time
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

parser = argparse.ArgumentParser(description='Start the program')
parser.add_argument('-ip', '--ip', type=str, help='IP address of the server')
parser.add_argument('-p', '--port', type=int, help='Port number of the server')
parser.add_argument('-d', '--debug', action='store_true', help='Enable debug mode')

args = parser.parse_args()

if args.ip is None:
    print('IP address is required')
    sys.exit(1)
elif args.port is None:
    print('Port number is required')
    sys.exit(1)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Inputs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    A1 = db.Column(db.Float, nullable=False)
    A2 = db.Column(db.Float, nullable=False)
    A3 = db.Column(db.Float, nullable=False)
    A4 = db.Column(db.Float, nullable=False)
    A5 = db.Column(db.Float, nullable=False)
    B1 = db.Column(db.Boolean, nullable=False)
    B2 = db.Column(db.Boolean, nullable=False)
    B3 = db.Column(db.Boolean, nullable=False)
    B4 = db.Column(db.Boolean, nullable=False)
    B5 = db.Column(db.Boolean, nullable=False)
    