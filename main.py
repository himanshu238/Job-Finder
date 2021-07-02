from bs4 import BeautifulSoup
import requests

html_txt = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

soup = BeautifulSoup(html_txt, 'lxml')
job = soup.find('li', class_='clearfix job-bx wht-shd-bx')
# print(job.prettify())
company_text = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
# print(company_text)
skills = job.find('span', class_='srp-skills').strong.text.replace(' ', '')
# print(skills)
published_date = job.find(
    'span', class_='sim-posted').span.text

print(f'''
Company Name: {company_text}
Required Skills: {skills}
Published : {published_date}
''')
