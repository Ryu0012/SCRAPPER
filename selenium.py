from requests import get
from bs4 import BeautifulSoup

# li = ["https://www.jumpit.co.kr/", "https://career.programmers.co.kr/job?page=1&tags=Python&order=recent"]

keyword = "python"
url = "https://career.programmers.co.kr/job?page=1&tags=Python"

jobs_data = []
try:
    response = get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        jobs = soup.find_all(class_="list-position-item")
        for job in jobs:
            post_list = job.find('h5', class_="position-title")
            post = post_list.find('a')
            title = post.string
            link = post.get('href')
            print(title, link, "\n")

except (IOError, AttributeError):
    print("error")
    pass
