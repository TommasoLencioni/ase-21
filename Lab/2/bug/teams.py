#teams.py
from flask import Blueprint, jsonify
teams = Blueprint('teams', __name__)
_DEVS = ['Tarek', 'Bob']
_OPS = ['Bill']
_DIR = ['Tizio']
_TEAMS = {1: _DEVS, 2: _OPS, 9:_DIR}

@teams.route('/teams')
def get_all():
	return jsonify(_TEAMS)

@teams.route('/teams/<int:team_id>')
def get_team(team_id):
	return jsonify(_TEAMS[team_id])
