from extractors.wwr import extract_wwr_jobs
from extractors.indeed import extract_indeed_jobs
from file import save_to_file

from flask import Flask

app = Flask("JobScrapper")


"""
keyword = input("직업을 입력 해주세요?")

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
jobs = indeed + wwr

save_to_file(keyword, jobs)

while (True):
    pass
"""
 






