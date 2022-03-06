from numpy import less
from flask import Flask, render_template, request, redirect
import joblib, math

app = Flask(__name__)

model = joblib.load("student_mark_predictor.pkl")

@app.route("/", methods=['GET','POST'])
def FrontPage():
    val = 0
    hour = 0
    message = "no"
    if request.method == "POST":
        hour = request.form['pred']
        val = '{0:.3g}'.format(model.predict([[int(request.form['pred'])]])[0][0])
        if float(hour) > 24:
            message = "yes"
        if math.ceil(float(val)) > 100:
            val = 100
    return render_template('index.html', model=val, hour=hour, message=message)


# @app.route("/", methods=['GET','POST'])
# def FrontPage():
#     if request.method=="POST":
#         todo = Todo(title=request.form['title'], desc=request.form['desc'])
#         db.session.add(todo)
#         db.session.commit()
    # allTodo = Todo.query.all()
    # return render_template('index.html', allTodo = allTodo)

if __name__ == "__main__":
    app.run(debug=True,port=8000)