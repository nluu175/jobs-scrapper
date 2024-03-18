import os
from dotenv import load_dotenv

from linkedin_scraper import JobSearch, actions, Person
from selenium import webdriver


load_dotenv()

linkedin_email = os.getenv("LINKEDIN_EMAIL")
linkedin_password = os.getenv("LINKEDIN_PASSWORD")


driver = webdriver.Chrome()
actions.login(driver, linkedin_email, linkedin_password)


# job_search = JobSearch(driver=driver, close_on_complete=False, scrape=False)
# # job_search contains jobs from your logged in front page:
# # - job_search.recommended_jobs
# # - job_search.still_hiring
# # - job_search.more_jobs

# job_listings = job_search.search(
#     "Software Developer"
# )  # returns the list of `Job` from the first page


# print(job_listings)
person = Person("https://www.linkedin.com/in/ln-minh/", driver=driver)
