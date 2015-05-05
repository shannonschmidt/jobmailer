import urllib.request as ur #url.request lib for handling the url
from bs4 import BeautifulSoup #bs for parsing the page

import datetime
from signup_app.models import Topic

from webscraperapp.models import Job


class scrapeMe:
    today = datetime.date.today()

    def __init__(self, date_to_search=today):
        self.date_to_search = date_to_search

    def update_all_jobs(self):
        self.scrapenyn()
        self.scrapebridgespanblue()
        self.scrapebridgespanwhite()
        self.scrapephil()
        
    def scrapenyn(self):
        nyn_url = "http://nyncareers.jobboard.io/"
        full_url_req = ur.Request(nyn_url)
        full_url_response = ur.urlopen(full_url_req)
        soup = BeautifulSoup(full_url_response)
        posts_area = soup.find("div", id="jobs-table-container")
        smaller_posts_area = posts_area.find("div", id="jobs-table")
        posts_to_scrape = smaller_posts_area.find_all("div", class_="job")
        for each_post in posts_to_scrape:
            job_title = each_post.find("div", class_="title").get_text().strip()
            job_company = each_post.find("div", class_="company").get_text().strip()
            job_location = each_post.find("div", class_="location").get_text().strip()
            link_area = each_post.find('a')
            job_link_slug = link_area.get('href')
            job_link_slug_str = str(job_link_slug)
            job_link = "http://nyncareers.jobboard.io" + job_link_slug_str
            job_date = each_post.find("div", class_="date col-sm-2 col-xs-4").get_text().strip() + " 2015"
            job_datetime = datetime.datetime.strptime(job_date, "%d %b %Y")
            job_source = "New York Non-Profit Careers"

            db_job, created = Job.objects.get_or_create(posting_date=job_datetime, found_date=self.today, company=job_company, title=job_title, location=job_location, source=job_source, link=job_link)
            if created:
                db_job.save()
                print(db_job)
            else:
                print('nyn skipping - already in DB')


    def scrapebridgespanblue(self):
        url = "http://www.bridgespan.org/getdoc/fd15276e-ea9c-4ccb-ad0f-1c7c83b0bece/Search_Jobs.aspx"
        full_url_req = ur.Request(url)
        full_url_response = ur.urlopen(full_url_req)
        soup = BeautifulSoup(full_url_response)
        all_posts = soup.find_all("tr", class_="rgRow")
        for each_post in all_posts:
            job_title = each_post.find_all("td")[0].get_text().strip()
            job_company = each_post.find_all("td")[1].get_text().strip()
            job_location = each_post.find_all("td")[3].get_text().strip()
            job_location = job_location.replace("\n", "")
            job_location = job_location.replace("\r", "")
            job_location = job_location.replace("          ", " ")
            general_link_area = each_post.find_all("td")[0]
            link_area = general_link_area.find('a')
            job_link_slug = link_area.get('href')
            job_link_slug_str = str(job_link_slug)
            job_link = "http://www.bridgespan.org/" + job_link_slug_str[6:]
            job_date = each_post.find_all("td")[4].get_text().strip()
            job_datetime = datetime.datetime.strptime(job_date, "%m/%d/%Y")
            job_source = "Bridgespan Group"

            db_job, created = Job.objects.get_or_create(posting_date=job_datetime, found_date=self.today, company=job_company, title=job_title, location=job_location, source=job_source, link=job_link)
            if created:
                db_job.save()
                print(db_job)
            else:
                print('blue skipping - already in DB')
    
    def scrapebridgespanwhite(self):
        url = "http://www.bridgespan.org/getdoc/fd15276e-ea9c-4ccb-ad0f-1c7c83b0bece/Search_Jobs.aspx"
        full_url_req = ur.Request(url)
        full_url_response = ur.urlopen(full_url_req)
        soup = BeautifulSoup(full_url_response)
        all_posts = soup.find_all("tr", class_="rgAltRow")
        for each_post in all_posts:
            job_title = each_post.find_all("td")[0].get_text().strip()
            job_company = each_post.find_all("td")[1].get_text().strip()
            job_location = each_post.find_all("td")[3].get_text().strip()
            job_location = job_location.replace("\n", "")
            job_location = job_location.replace("\r", "")
            job_location = job_location.replace("          ", " ")
            general_link_area = each_post.find_all("td")[0]
            link_area = general_link_area.find('a')
            job_link_slug = link_area.get('href')
            job_link_slug_str = str(job_link_slug)
            job_link = "http://www.bridgespan.org/" + job_link_slug_str[6:]
            job_date = each_post.find_all("td")[4].get_text().strip()
            job_datetime = datetime.datetime.strptime(job_date, "%m/%d/%Y")
            job_source = "Bridgespan Group"
            db_job, created = Job.objects.get_or_create(posting_date=job_datetime, found_date=self.today, company=job_company, title=job_title, location=job_location, source=job_source, link=job_link)
            if created:
                db_job.save()
                print(db_job)
            else:
                print('white skipping - already in DB')
    
    def scrapephil(self):
        url = "https://philanthropy.com/jobSearch?action=rem&search_siteId=7&contextId=224&searchQueryString="
        full_url_req = ur.Request(url)
        full_url_response = ur.urlopen(full_url_req)
        soup = BeautifulSoup(full_url_response)
        all_posts = soup.find_all("div", class_="result")
        for each_post in all_posts:
            try:
                job_title = each_post.find("h4", class_="result-title").get_text().strip()
                job_company = each_post.find("h5", class_="organization").get_text().strip()
                job_details = each_post.find("dl", class_="col-md-5 details-left")
                job_date = job_details.find_all("dd")[0].get_text().strip()
                job_datetime = datetime.datetime.strptime(job_date, "%m/%d/%Y")
                job_location = job_details.find_all("dd")[1].get_text().strip()
                link_area = each_post.find("h4", class_="result-title")
                job_link_slug = link_area.find("a").get('href')
            except:
                pass
            else:
                job_link_slug_str = str(job_link_slug)
                job_link = "https://philanthropy.com" + job_link_slug_str
                job_source = "Chronicle of Philanthropy"
                db_job, created = Job.objects.get_or_create(posting_date=job_datetime, found_date=self.today, company=job_company, title=job_title, location=job_location, source=job_source, link=job_link)
                if created:
                    db_job.save()
                    print(db_job)
                    second_full_url_req = ur.Request(job_link)
                    second_full_url_response = ur.urlopen(second_full_url_req)
                    second_soup = BeautifulSoup(second_full_url_response)
                    field_area = second_soup.find_all("div", class_="col-md-6 job--details")[3].get_text().strip()
                    job_field = field_area[6:]
                    job_field = job_field.replace("\n                                            ","")
                    job_field_split = job_field.split(",")

                    for item in job_field_split:
                        item = item.strip()
                        try:
                            db_topic = Topic.objects.get(name=item)
                            db_job.topics.add(db_topic)
                            print("added " + item.lower() + " to " + job_company + " " + job_title)
                        except:
                            print("topic " + item.lower() + " is not in the database")

                else:
                    print('phil skipping - already in DB')