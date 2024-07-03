from flask import Blueprint, render_template
from src.board import Board
from src.player import Player

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():
    return render_template('index.html')