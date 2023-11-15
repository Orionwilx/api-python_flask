from flask import Flask
from flask_cors import CORS
from config import config

#routes
from routes import word

app = Flask(__name__)

CORS(app)

def page_not_found(error):
    return "<h1>Not Fount page<h1>", 404

if __name__=='__main__':
    app.config.from_object(config['development'])

    #Blueprints
    app.register_blueprint(word.main, url_prefix='/api/words')

    #Error handlers
    app.register_error_handler(404, page_not_found)
    app.run(host='0.0.0.0')