from flask import Flask
from route import user
from exception import InvalidUsage


# 에러 핸들러 등록 (에러 발생시, 에러 화면 대신 에러 응답 처리를 하기 위함)
def register_errorhandlers(app):
    def errorhandler(error):
        response = error.to_json()
        response.status_code = error.status_code
        return response

    app.register_error_handler(InvalidUsage, errorhandler)


def create_app():
    app = Flask(__name__)
    app.register_blueprint(user.blueprint)
    register_errorhandlers(app)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
