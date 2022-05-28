from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html", a = "lev")

@app.route('/user/<user_name>/<int:year>/<int:month>/<int:day>', methods=["GET", "POST"])
def user(user_name, year, month, day):
    return render_template("excercise.html", user_name=user_name,year=year, month=month, day=day)

if __name__ == '__main__':
    app.run(debug=True)