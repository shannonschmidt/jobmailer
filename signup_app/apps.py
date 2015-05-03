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

        #if we don't use a thread, this will render the signup page unresponsive
        #tm.send_mail_task()

        #todo: fix bug where ready() may be called twice and spawns 2 threads and sends double emails
        t = Thread(target=tm.send_mail_task)
        t.start()