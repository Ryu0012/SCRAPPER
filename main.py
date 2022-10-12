from bs4 import BeautifulSoup
from wwr_ import wwr_job_scrapper
from save_to_file import save_to_file
from flask import Flask, render_template


keyword = input("keyword: ")
jobs = wwr_job_scrapper(keyword)

# save_to_file(keyword, jobs)
app = Flask("job Scrapper")


@app.route("/")
def index():
    return render_template("index.html", name="lvu")


app.run("0.0.0.0")
