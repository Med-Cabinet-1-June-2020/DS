from flask import Flask
# from web_app.routes.med_routes import med_routes
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME=os.getenv("DB_NAME")
DB_USER=os.getenv("DB_USER")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_HOST=os.getenv("DB_HOST")

print(DB_NAME,DB_USER, DB_PASSWORD, DB_HOST)

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print(connection)

cursor = connection.cursor()
print(cursor)

cursor.execute("SELECT * FROM medcabinet1;")

result = cursor.fetchall()
print(result)

# to save transactions
connection.commit()
cursor.close()
connection.close()

# def create_app():
#     app = Flask(__name__)

#     # app.config["SECRET_KEY"] = SECRET_KEY
#     # app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
#     # # db.init_app(app)
#     # # migrate.init_app(app, db)

#     app.register_blueprint(med_routes)

#     return app

# if __name__ == "__main__":
#     my_app = create_app()
#     my_app.run(debug=True)