from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

# Database Model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    course = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"{self.id} - {self.name}"

# Create DB
with app.app_context():
    db.create_all()

# --- ROUTES ---

# HOME PAGE (Read + Create)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        course = request.form['course']
        new_student = Student(name=name, email=email, course=course)
        db.session.add(new_student)
        db.session.commit()
        return redirect('/')
    students = Student.query.all()
    return render_template('index.html', students=students)

# DELETE
@app.route('/delete/<int:id>')
def delete(id):
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return redirect('/')

# UPDATE
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    student = Student.query.get(id)
    if request.method == 'POST':
        student.name = request.form['name']
        student.email = request.form['email']
        student.course = request.form['course']
        db.session.commit()
        return redirect('/')
    return render_template('update.html', student=student)

if __name__ == '__main__':
    app.run(debug=True)
