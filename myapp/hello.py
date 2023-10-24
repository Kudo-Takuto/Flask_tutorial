from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def hello_world():
    name="Flask"
    return render_template("index.html",name_value=name)

@app.route('/good')
def good():
    name = "Good"
    return name

## おまじない
if __name__ == "__main__":
    app.run(debug=True)