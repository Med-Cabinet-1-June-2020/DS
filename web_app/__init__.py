from flask import Flask
from web_app.routes.med_routes import med_routes


def create_app():
    app = Flask(__name__)

    # app.config["SECRET_KEY"] = SECRET_KEY
    # app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    # # db.init_app(app)
    # # migrate.init_app(app, db)

    app.register_blueprint(med_routes)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)