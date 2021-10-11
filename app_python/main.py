from flask import Flask
from datetime import datetime
from pytz import timezone
from os import path, makedirs

app = Flask(__name__)
filename = "cache/visits.txt"


def moscow_time():
    return datetime.now(timezone('Europe/Moscow')).time()

def mem_visit(time):
    if not path.exists(path.dirname(filename)):
        makedirs(path.dirname(filename))
    file = open(filename, "a")
    file.write(time.strftime("%H:%M:%S"))
    file.write("\n")
    file.close()

def get_visits_list():
    visits_list = "<ul style='font-weight: normal; font-size: 28px; margin: 40px;'>"
    if path.exists(filename):
        with open(filename, "r") as file:
            visits = file.readlines()
        for visit in visits:
            visits_list += "<li>"+visit+" (MSK UTC)</li>"
    visits_list += "</ul>"
    return visits_list

@app.route("/")
def index():
    time = moscow_time()
    mem_visit(time)
    return "<div style='font-weight: bold; font-size: 30px; margin: 25px;'>" \
           + "Current time: " \
           + time.strftime("%H:%M:%S") \
           + " (MSK UTC)</div>"

@app.route("/visits")
def visits_page():
    return "<div style='font-weight: bold; font-size: 30px; margin: 25px;'>" \
           + "App Visits " \
           + get_visits_list() \
           + "</div>"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
