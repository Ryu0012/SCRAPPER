from bs4 import BeautifulSoup
from wwr_ import wwr_job_scrapper
from save_to_file import save_to_file

keyword = input("keyword: ")
jobs = wwr_job_scrapper(keyword)

# save_to_file(keyword, jobs)
