from flask import jsonify


class InvalidUsage(Exception):
    status_code = 500
    ERROR_MESSAGE = {
        'allow_json': 'allow only json format',
        'require_param': 'require parameter'
    }

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_json(self):
        return jsonify({"message": self.message})

    @classmethod
    def allow_json(cls):
        mm = cls.ERROR_MESSAGE['allow_json']
        return cls(message=mm, status_code=400)

    @classmethod
    def require_param(cls, require_params=[]):
        mm = cls.ERROR_MESSAGE['require_param']
        if require_params:
            ss = ', '.join(require_params)
            mm += f'({ss})'

        return cls(message=mm, status_code=400)
