from flask import Flask
from flask_sqlalchemy import SQLAlchemy                                                                                                                        # type: ignore[reportMissingImports]

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:Jasil%402004@localhost:3306/newstudent_db"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Model 
class Student(db.Model):
    id = db.Column(
        db.Integer,
        primary_key = True
    )

    name = db.Column(
        db.String(100),
        nullable = False
    )

    email = db.Column(
        db.String(100),
        unique = True,
        nullable = False
    )

    age = db.Column(
        db.Integer
    )

    course = db.Column(
        db.String(100),

    )



# create Table
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return "Flask + MySQL Working !!! "


if __name__ == "__main__":
    app.run(debug=True)