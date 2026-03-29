from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def course_page():
    courses = ["Python", "JavaScript", "Java", "C++", "Ruby"]
    logged_in = True
    username = "Gaurav" 
    return render_template('course.html', courses=courses, logged_in=logged_in, username=username)

if __name__ == '__main__':
    app.run(debug=True)
    