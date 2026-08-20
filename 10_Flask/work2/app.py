from flask import Flask,render_template,request,redirect,url_for
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








@app.route("/index")
def index():
    students = Student.query.all()

    return render_template("index.html",students=students)


@app.route("/add", methods=["GET" , "POST"])
def add_student():

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        course = request.form["course"]
        age = request.form["age"]


        student = Student(
            name = name,
            email = email,
            course = course,
            age = age
        )
        db.session.add(student)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add_student.html")





@app.route("/update/<int:id>", methods = ["GET","POST"])
def update_student(id):

    student = Student.query.get(id)

    if request.method == "POST":
        student.name = request.form["name"]
        student.email = request.form["email"]
        student.course = request.form["course"]
        student.age = request.form["age"]

        db.session.commit()
        return redirect(url_for("index"))
    return render_template("update_student.html")
 




@app.route("/delete/<int:id>", methods = ["GET","POST"])
def delete_student(id):

    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for("index"))






if __name__ == "__main__":
    app.run(debug=True)