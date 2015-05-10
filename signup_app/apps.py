from threading import Thread

from django.apps import AppConfig

from jobmailer.mailer import Mailer
from jobmailer.task_manager import TaskManager
from webscraperapp.scraper import scrapeMe


__author__ = 'shannon'


class SignupAppConfig(AppConfig):
    name = 'signup_app'
    verbose_name = "Signup App"

    def ready(self):
        if hasattr(self, 'ready_run'):
            return
        print("ready started")
        self.ready_run = True
        scraper = scrapeMe()
        mailer = Mailer()
        tm = TaskManager(scraper, mailer)

#For this prototype, we're using a thread and scheduler to trigger the once per day scraping and emails
#since it's the simplest solution. For the future production app, we would use something more robust like a Cron job.

        t = Thread(target=tm.send_mail_task)
        t.start()