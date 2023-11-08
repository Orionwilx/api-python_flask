from flask import Blueprint, jsonify

main=Blueprint('word_blueprint',__name__)

@main.route('/')
def get_words():

    return jsonify('message': "wilfrandev")