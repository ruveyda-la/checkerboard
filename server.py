from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', x=8, y=8,color1='rebeccapurple', color2='peachpuff')

@app.route('/<int:x>')
def length(x):
    return render_template("index.html", x=int(x) , y=8,color1='rebeccapurple', color2='peachpuff')


@app.route('/<int:x>/<int:y>')
def widthLength(x,y):
    return render_template("index.html", x=int(x), y=int(y),color1='rebeccapurple', color2='peachpuff')


@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def sizescolors(x,y,color1,color2):
    return render_template("index.html",  x=int(x), y=int(y), color1=color1, color2=color2 )









if __name__ == "__main__":
    app.run(debug=True)
