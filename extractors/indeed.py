from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver

def get_page_count(keyword):
    browser = webdriver.Chrome()
    browser.get(f"https://kr.indeed.com/jobs?q={keyword}")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find("nav", attrs={"aria-label": "pagination"})
    if pagination == None:
        return 1
    pages = pagination.find_all('div', recursive=False)
    count = len(pages)
    if count >= 5:
        return 5
    else:
        return count

def extract_indeed_jobs(keyword):
    results = []
    pages = get_page_count(keyword)
    for page in range(pages):
        base_url = "https://kr.indeed.com/jobs"
        final_url = f"{base_url}?q={keyword}&start={page*10}"
        print("Requesting", final_url)
        browser = webdriver.Chrome()
        browser.get(final_url)
        soup = BeautifulSoup(browser.page_source, "html.parser")
        job_list = soup.find('ul', class_="css-zu9cdh")
        jobs = job_list.find_all('li', recursive=False)
        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")
            if zone == None:
                anchor = job.select_one("h2 a")
                title = anchor['aria-label']
                link = anchor['href']
                company = job.find("span", class_="companyName")
                location = job.find("div", class_="companyLocation")
                job_data = {
                    'link': f"https://kr.indeed.com/{link}",
                    'company': company.string,
                    'location': location.string,
                    'position': title,
                }
                results.append(job_data)
    return results

