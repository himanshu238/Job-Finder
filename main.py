from os import times
from bs4 import BeautifulSoup
import requests
import time

domain = input('Enter any specific domain: ')
location = input('Enter the location where you are intrested to work: ')
unknown = input('Enter unfamiliar skills: ').split()
print('')
print('Searching for jobs....')
print('')


def get_data():

    html_txt = requests.get(
        f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={domain}&txtLocation={location}').text

    soup = BeautifulSoup(html_txt, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    # print(job.prettify())

    for job in jobs:
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_text = job.find('h3', class_='joblist-comp-name').text
            company_text = ' '.join(company_text.split())
            # print(company_text)
            skills = job.find(
                'span', class_='srp-skills').text.replace(' ', '')
            # print(skills)
            more_info = job.header.h2.a['href']
            exp = job.find(
                'ul', class_='top-jd-dtl clearfix').li.text.replace(' ', '')

            for i in unknown:
                if i.lower() not in skills.lower():
                    print(
                        '---------------------------------------------------------------------')
                    print(f'Company Name: {company_text}')
                    print(f'Experience Required: {exp[11:]}')
                    print(f'Required Skills: {skills.strip()}')
                    print(f'More Info: {more_info}')
                    print('')


if __name__ == '__main__':
    while True:
        get_data()
        print('will restart in 10 minutes.')
        time.sleep(10*60)
