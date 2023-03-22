from typing import Optional

from PyMultiDictionary import MultiDictionary
from flasgger import Swagger
from flask import Flask, g, jsonify
from flask_expects_json import expects_json

from schema import VALIDATION_SCHEMA

dictionary: MultiDictionary = MultiDictionary()
app: Flask = Flask(__name__)


@app.route(
    '/api/v1/word_synonyms',
    methods=['POST']
)
@expects_json(VALIDATION_SCHEMA)
def get_words_synonyms():
    """
    Route to get synonyms of pasted words.
    If the JSON Schema is not valid at POST request,
    400 Validation Error will be raised.
    """
    result = {
        "data": {
            "word_synonyms": {
            }
        },
        "status": "ok"
    }

    for i_word in g.data.get('words'):
        found_synonyms: list[Optional[str]] = dictionary.synonym(lang='en', word=i_word)
        result['data']['word_synonyms'][i_word] = found_synonyms

    return jsonify(result), 200


@app.errorhandler(400)
def bad_request_handler(error):
    """
    400 Status code error Handler.
    If the error is type ValidationError,
    response will contain "error" status and message
    with detailed information about error.
    """
    return jsonify(status="error", message=error.description)


if __name__ == '__main__':
    swagger = Swagger(app=app, template_file='open-api.yaml')
    app.run(host='0.0.0.0', port=5000)
