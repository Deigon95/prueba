from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route("/hora")
def hora():
    hora, minuto = datetime.now().hour, datetime.now().minute
    print(hora)
    print(minuto)
    return render_template("hora.html", hora=hora, minuto=minuto)


if __name__ == '__main__':
    app.run(debug=True)
