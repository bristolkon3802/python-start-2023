from requests import get
from bs4 import BeautifulSoup
"""
웹 스크랩핑  - https://weworkremotely.com/ 데이터 추출
insert Beautifulsoup
"""


def extract_wwr_jobs(keyword):
  base_url = "https://weworkremotely.com/remote-jobs/search?term="
  res = get(f"{base_url}{keyword}")
  if res.status_code != 200:
    print("Can't request website")
  else:
    results = []
    soup = BeautifulSoup(res.text, "html.parser")
    jobs = soup.find_all('section', class_="jobs")
    for job_section in jobs:
      job_posts = job_section.find_all('li')
      job_posts.pop(-1)
      for post in job_posts:
        anchors = post.find_all('a')
        anchor = anchors[1]
        link = anchor['href']
        company, kind, region = anchor.find_all('span', class_='company')
        title = anchor.find('span', class_='title')
        #print(link, company.string, kind.string, region.string, title.string)
        #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        job_data = {
            'link': f"https://weworkremotely.com{link}",
            'company': company.string,
            'location': region.string,
            'position': title.string,
        }
        for each in job_data:
          if job_data[each] != None:
              job_data[each] = job_data[each].replace(",", " ")
        results.append(job_data)
    return results