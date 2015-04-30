import urllib.request as ur #url.request lib for handling the url
from bs4 import BeautifulSoup #bs for parsing the page
import requests
from lxml import html
import datetime
import random

class scrapeMe():
    today = datetime.date.today()
    today_as_string = str(today)
    days_jobs_list = []
    
    def __init__(self, date_to_search=today_as_string):
        self.date_to_search = date_to_search
        self.scrapenyn()
        self.scrapebridgespanblue()
        self.scrapebridgespanwhite()
        self.scrapephil()
        
    def scrapenyn(self):
        job_dict = {}
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
            job_date = each_post.find("div", class_="date col-sm-2 col-xs-4").get_text().strip()
            #change dates of posts into same format as datetime
            job_month = job_date[-3:]
            if job_month == "Jan":
                job_month_num = "01"
            elif job_month == "Feb":
                job_month_num = "02"
            elif job_month == "Mar":
                job_month_num = "03"
            elif job_month == "Apr":
                job_month_num = "04"
            elif job_month == "May":
                job_month_num = "05"
            elif job_month == "Jun":
                job_month_num = "06"
            elif job_month == "Jul":
                job_month_num = "07"
            elif job_month == "Aug":
                job_month_num = "08"
            elif job_month == "Sep":
                job_month_num = "09"
            elif job_month == "Oct":
                job_month_num = "10"
            elif job_month == "Nov":
                job_month_num = "11"
            else:
                job_month_num = "12"
            job_day_of_month = job_date[:2]
            job_date = "2015-"+job_month_num+"-"+job_day_of_month
            job_source = "New York Non-Profit Careers"
            pk = random.randint(1,1000000000000000)
            job_dict = {"pk": pk, "Date": job_date, "Company": job_company, "Title": job_title, "Location": job_location, "Source": job_source, "Link": job_link}
            if job_date == self.date_to_search:
                scrapeMe.days_jobs_list.append(job_dict)
        self.addtolist()

    def scrapebridgespanblue(self):
        job_dict = {}
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
            job_date = job_date.replace("/","-")
            job_date_num = job_date[0:2]
            if job_date_num == "1-":
                job_date_num = "01"
            elif job_date_num == "2-":
                job_date_num = "02"
            elif job_date_num == "3-":
                job_date_num = "03"
            elif job_date_num == "4-":
                job_date_num = "04"
            elif job_date_num == "5-":
                job_date_num = "05"
            elif job_date_num == "6-":
                job_date_num = "06"
            elif job_date_num == "7-":
                job_date_num = "07"
            elif job_date_num == "8-":
                job_date_num = "08"
            elif job_date_num == "9-":
                job_date_num = "09"
            else:
                job_date_num = job_date_num
            job_date = job_date[-4:]+"-"+job_date_num+"-"+job_date[-7:-5]
            job_source = "Bridgespan Group"
            pk = random.randint(1,1000000000000000)
            job_dict = {"pk": pk, "Date": job_date, "Company": job_company, "Title": job_title, "Location": job_location, "Source": job_source, "Link": job_link}
            if job_date == self.date_to_search:
                scrapeMe.days_jobs_list.append(job_dict)
        self.addtolist()
    
    def scrapebridgespanwhite(self):
        job_dict = {}
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
            job_date = job_date.replace("/","-")
            job_date_num = job_date[0:2]
            if job_date_num == "1-":
                job_date_num = "01"
            elif job_date_num == "2-":
                job_date_num = "02"
            elif job_date_num == "3-":
                job_date_num = "03"
            elif job_date_num == "4-":
                job_date_num = "04"
            elif job_date_num == "5-":
                job_date_num = "05"
            elif job_date_num == "6-":
                job_date_num = "06"
            elif job_date_num == "7-":
                job_date_num = "07"
            elif job_date_num == "8-":
                job_date_num = "08"
            elif job_date_num == "9-":
                job_date_num = "09"
            else:
                job_date_num = job_date_num
            job_date = job_date[-4:]+"-"+job_date_num+"-"+job_date[-7:-5]
            job_source = "Bridgespan Group"
            pk = random.randint(1,1000000000000000)
            job_dict = {"pk": pk, "Date": job_date, "Company": job_company, "Title": job_title, "Location": job_location, "Source": job_source, "Link": job_link}
            if job_date == self.date_to_search:
                scrapeMe.days_jobs_list.append(job_dict)
        self.addtolist()
    
    def scrapephil(self):
        job_dict = {}
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
                job_location = job_details.find_all("dd")[1].get_text().strip()
                link_area = each_post.find("h4", class_="result-title")
                job_link_slug = link_area.find("a").get('href')
            except:
                pass
            else:
                job_link_slug_str = str(job_link_slug)
                job_link = "https://philanthropy.com" + job_link_slug_str
                #change dates of posts into same format as datetime
                job_date = job_date[-4:]+"-"+job_date[:2]+"-"+job_date[3:5]
                job_source = "Chronicle of Philanthropy"
                pk = random.randint(1,1000000000000000)
                second_full_url_req = ur.Request(job_link)
                second_full_url_response = ur.urlopen(second_full_url_req)
                second_soup = BeautifulSoup(second_full_url_response)
                field_area = second_soup.find_all("div", class_="col-md-6 job--details")[3].get_text().strip()
                job_field = field_area[6:]
                job_field = job_field.replace("\n                                            ","")
                job_field_split = job_field.split(",")
                try:
                    job_field_1 = newphrase[0].lower()
                except:
                    pass
                try:
                    job_field_2 = newphrase[1][1:].lower()
                except:
                    pass
                try:
                    job_field_3 = newphrase[2][1:].lower()
                except:
                    pass
                try:
                    job_field_4 = newphrase[3][1:].lower()
                except:
                    pass
                try:
                    job_field_5 = newphrase[4][1:].lower()
                except:
                    pass
                try:
                    job_field_6 = newphrase[5][1:].lower()
                except:
                    pass
                job_dict = {"pk": pk, "Date": job_date, "Company": job_company, "Title": job_title, "Location": job_location, "Source": job_source, "Link": job_link, "Field_1": job_field_1, "Field_2": job_field_2, "Field_3": job_field_3, "Field_4": job_field_4, "Field_5": job_field_5}
                if job_date == self.date_to_search:
                    scrapeMe.days_jobs_list.append(job_dict)
        self.addtolist()

    def addtolist(self):
        scrapeMe.days_jobs_list.append(self.days_jobs_list)
        return(scrapeMe.days_jobs_list)

scrapeEm = scrapeMe()

scrapeEm.days_jobs_list