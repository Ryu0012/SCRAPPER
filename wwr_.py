
from requests import get
from bs4 import BeautifulSoup


def wwr_job_scrapper(keyword):
    jobs_data = []
    url = f"https://weworkremotely.com/remote-jobs/search?term={keyword}"
    try:
        response = get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            jobs = soup.find_all('section', class_="jobs")
            for job in jobs:
                job_posts = job.find_all('li')
                job_posts.pop(-1)
                for post in job_posts:
                    anchors = post.find_all('a')
                    anchor = anchors[1]
                    link = anchor.get('href')
                    link = f"https://weworkremotely.com/{link}"
                    companys = post.find_all(class_="company")
                    company = companys[0].string.replace(",", " ")
                    title = post.find(class_="title").string.replace(",", " ")
                    region = post.find(
                        class_="region").string.replace(",", " ")
                    # print(company, title, region)
                    job_data = {
                        'Company': company,
                        'Position': title,
                        'region': region,
                        'link': link,
                    }
                    jobs_data.append(job_data)
    except (IOError, AttributeError):
        pass
    return jobs_data
