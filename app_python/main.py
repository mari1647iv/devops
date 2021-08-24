from flask import Flask
from datetime import datetime
from pytz import timezone

app = Flask(__name__)


def moscow_time():
    return datetime.now(timezone('Europe/Moscow')).time()


@app.route("/")
def index():
    return "<div style='font-weight: bold; font-size: 30px; margin: 25px;'>" \
           + "Current time: " \
           + moscow_time().strftime("%H:%M:%S") \
           + " (MSK UTC)</div>"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
