from flask import Blueprint, jsonify

#Models

from models.Word_model import WordModel


main = Blueprint('word_blueprint',__name__)


@main.route('/')
def get_words():

    try:
        words = WordModel.get_words()
        return jsonify(words)

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500