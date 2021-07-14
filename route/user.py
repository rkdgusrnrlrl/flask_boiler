from flask import Blueprint, jsonify, request
from exception import InvalidUsage

blueprint = Blueprint('user', __name__)


def check_require_param(require_params, data):
    params_not_exist = []
    for pp in require_params:
        if pp not in data:
            params_not_exist.append(pp)

    if params_not_exist:
        raise InvalidUsage.require_param(params_not_exist)


@blueprint.route('/users', methods=['POST'])
def register_user():
    if not request.is_json:
        raise InvalidUsage.allow_json()

    require_param = ['id', 'password']
    dd = request.json

    # 필수 파라미터 체
    check_require_param(require_param, dd)

    # Database 처리

    # 응답값 처리
    return jsonify({
        'result': 'success'
    })
