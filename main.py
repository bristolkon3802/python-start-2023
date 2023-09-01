from extractors.wwr import extract_wwr_jobs
from extractors.indeed import extract_indeed_jobs
from file import save_to_file

from flask import Flask, render_template

app = Flask("JobScrapper")

@app.route("/")
def home():
    return render_template("home.html",name="Bing")

@app.route("/hello")
def hello():
    return 'hello you!'

app.run("127.0.0.1")

"""
keyword = input("직업을 입력 해주세요?")

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
jobs = indeed + wwr

save_to_file(keyword, jobs)

while (True):
    pass
"""
 






