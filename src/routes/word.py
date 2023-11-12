from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.Word import Word

# Models

from models.Word_model import WordModel


main = Blueprint('word_blueprint',__name__)


@main.route('/')
def get_words():

    try:
        words = WordModel.get_words()
        return jsonify(words)

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/<id>')
def get_word(id):
    try:
        word = WordModel.get_word(id)
        if word != None:
            return jsonify(word)
        else:
             return jsonify({}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/add', methods=['POST'])
def add_word():
    try:
        w0rd = request.json['word']
        accept = request.json['accept']
        id = uuid.uuid4()        
        word = Word(str(id), w0rd, accept)
        
        affected_row= WordModel.add_word(word)

        if affected_row == 1:
            return jsonify(word.id)
        else:
            return jsonify({'message': "Error on insert"}), 500
        return jsonify({})
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/delete/<id>', methods=['DELETE'])
def delete_word(id):
    try:
        
        word = Word(id)

        affected_row= WordModel.delete_word(word)

        if affected_row == 1:
            return jsonify(word.id)
        else:
            return jsonify({'message': "No word delete"}), 500
        return jsonify({})
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500