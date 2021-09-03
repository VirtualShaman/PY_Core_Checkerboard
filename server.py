from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def render():
    return render_template('index.html', row=8, column=8)

@app.route('/<int:column>')
def onlyY(column):
    return render_template('index.html', column=column, row=8)

@app.route('/<int:column>/<int:row>')
def XyY(column,row):
    return render_template('index.html', column=column, row=row)

@app.route('/<int:column>/<int:row>/<string:color1>/<string:color2>')
def withcolornow(column,row,color1,color2):
    return render_template('index.html', column=column, row=row, color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)
