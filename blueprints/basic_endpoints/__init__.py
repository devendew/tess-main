from flask import Blueprint, request

blueprint = Blueprint('api', __name__, url_prefix='/api')


@blueprint.route('/', methods=['GET'])
def root():
    return {'message': 'Root!'}


@blueprint.route('/read_ocr', methods=['POST'])
def read_ocr():
    if request.method == "POST":
        return {
            'message': 'This endpoint should create an entity',
            'method': request.method,
            'body': request.json
        }
