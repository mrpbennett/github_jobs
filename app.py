from flask import Flask, render_template
from flaskext.markdown import Markdown
from forms import JobSearch
import requests

app = Flask(__name__)
Markdown(app, output_format="html5")

app.config.from_object("config.DevConfig")


def format_datetime(value):
    """Format date time object using jinja filters"""
    return value.strftime("%B %-d, %Y")


app.jinja_env.filters["datetime"] = format_datetime


data = {}

# get jobs data once submitted
def get_jobs(search):

    r = requests.get(f"https://jobs.github.com/positions.json?search={search}")
    if r != 200:
        data = r.json()
    else:
        print(f"ERROR: {r.status_code}, {r.reason}")

    return data


@app.route("/", methods=["GET", "POST"])
def home():

    jobs = {}

    form = JobSearch()
    if form.validate():

        search = form.search.data
        jobs = get_jobs(search)

    return render_template("home.html", form=form, jobs=jobs)


@app.route("/positions/<string:id>?markdown=true")
def job_post(id):

    r = requests.get(f"https://jobs.github.com/positions/{id}.json")
    if r != 200:
        data = r.json()
    else:
        print(f"ERROR: {r.status_code}, {r.reason}")

    return render_template("job.html", job=data)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
