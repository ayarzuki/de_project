# Import necessary libraries
from bs4 import BeautifulSoup
import requests
import json
import csv
from datetime import datetime
# import pdb

# Specify the URL of the webpage to be scraped
# url = 'https://glints.com/id/en/opportunities/jobs/programming/14c33dd2-6879-46f9-b294-b3b2e9364200?utm_referrer=explore'
# url = 'https://glints.com/id/en/opportunities/jobs/digital-paid-advertising-associates/92198b26-5728-4eb4-a8be-31fd20fb7267?utm_referrer=explore'

# Define the headers to be used in the request
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Referer': 'https://glints.com/id/en/lowongan-kerja',
    'Sec-Ch-Ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"macOS"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}


def setup_csv():
    # Create or overwrite the CSV file with just the header row
    with open('job_data_jakarta.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Job Title', 'Job Category','Date Posted', 'Company Name', 'Job Location', 'Job Expired Date', 'Minimal Salary', 'Maximal Salary', 'Employment Type', 'Job URL'])


    # Send an HTTP GET request to the URL with the defined headers
    # response = requests.get(url, headers=headers)
def scrape_job_detail(job_url):
    response = requests.get(job_url, headers=headers)
        
    # Check for a valid response
    if response.status_code == 200:
        print(f"Success to retrieve {job_url}")
        # Parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the script tag with type "application/ld+json"
        script_tag = soup.find('script', {'type': 'application/ld+json'})

        # Load the JSON string from the script tag
        job_data = json.loads(script_tag.string)
        
        ## Name job
        # job_title = job_data['title']
        try:
            job_title = job_data['title']
        except Exception as e:
            job_title = ""
        ## job date posted
        date_str = job_data['datePosted']
        date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%fZ')
        job_date_posted = date_obj.strftime('%d-%m-%Y')

        ## job city location
        # job_location = job_data['jobLocation']['address']['addressLocality']
        try:
            job_location = job_data['jobLocation']['address']['addressLocality']
        except Exception as e:
            job_location = ""

        ## company hiring name
        company_hiring = job_data['hiringOrganization']['name']

        ## URL job
        # Find the <link> tag with rel="canonical"
        link_tag = soup.find('link', {'rel': 'canonical'})
        # Extract the URL from the href attribute of the <link> tag
        url_job = link_tag['href'] if link_tag else 'URL not found'

        # Extract job category
        job_category = json.loads(soup.find('script', {'type': 'application/json'}).string)["props"]["pageProps"]["initialOpportunity"]["hierarchicalJobCategory"]["parents"][0]["name"]

        # Job expired
        job_expired = job_data['validThrough']

        # Minimal Salary
        try:
            min_salary = job_data["baseSalary"]["value"]["minValue"]
        except Exception as e:
            min_salary = ""

        # Maximum Salary
        try:
            max_salary = job_data["baseSalary"]["value"]["maxValue"]
        except Exception as e:
            max_salary = ""

        # Tipe Pekerjaan / Employment Type
        employment_type = job_data["employmentType"]

        # Now let's create a CSV file (OLD METHOD)
        # with open('job_data.csv', mode='w', newline='', encoding='utf-8') as file:
        #     writer = csv.writer(file)
        #     # Write the header row
        #     writer.writerow(['Job Title', 'Job Category','Date Posted', 'Company Name', 'Job Location', 'Job Expired Date', 'Minimal Salary', 'Maximal Salary', 'Employment Type', 'Job URL'])
        #     # Write the data row
        #     writer.writerow([job_title, job_category, job_date_posted, company_hiring, job_location, job_expired, min_salary, max_salary, employment_type, url_job])

        # print('CSV file has been written successfully.')

        with open('job_data_jakarta.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([job_title, job_category, job_date_posted, company_hiring, job_location, job_expired, min_salary, max_salary, employment_type, url_job])

        print('Row has been written successfully.')


        ### This json file contain more information about jobs
        # script_tag_2 = json.loads(soup.find('script', {'type': 'application/json'}).string)
        # breakpoint()
        # Writing JSON data into a file
        # with open('more_data.json', 'w') as f:
        #     json.dump(script_tag_2, f, indent=4)
    else:
        print(f'Failed to retrieve page with status code: {response.status_code}')

def scrape_page(url):
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve {url}")
        return
    soup = BeautifulSoup(response.content, 'html.parser')
    # breakpoint()
    job_cards = soup.find_all('div', class_='JobCardsc__JobCardWrapper-sc-hmqj50-1 fnsbDp')
    for job_card in job_cards:
        a_tag = job_card.find('a')
        if a_tag:
            job_url = 'https://glints.com' + a_tag['href']
            print(f"Scraping job detail: {job_url}")
            scrape_job_detail(job_url)

def handle_pagination(base_url, start_page=1, end_page=50):
    for current_page in range(start_page, end_page + 1):
        url = f"{base_url}?page={current_page}" # For all jobs & Jakarta jobs
        # url = f"{base_url}&page={current_page}"
        print(f"Scraping page {current_page}: {url}")
        scrape_page(url)

# Set up the CSV file with headers before starting the pagination
setup_csv()
# Set your base URL here
# base_url = 'https://glints.com/id/en/lowongan-kerja'
# base_url = 'https://glints.com/id/en/opportunities/jobs/explore?country=ID&locationName=All+Cities%2FProvinces&lastUpdated=PAST_MONTH' # Monthly jobs
base_url = 'https://glints.com/id/en/job-location/indonesia/dki-jakarta' # Daerah Jakarta
handle_pagination(base_url)