import sched
from smtplib import SMTPRecipientsRefused
import time

__author__ = 'shannon'


class TaskManager:

    def __init__(self, scraper, mailer):
        self.scraper = scraper
        self.mailer = mailer
        self.interval = 60 * 60 * 24 #daily

    def send_mail_task(self, scheduler=None):
        # make a new scheduler only once & schedule this function immediately
        if scheduler is None:
            scheduler = sched.scheduler(time.time, time.sleep)
            scheduler.enter(0, 1, self.send_mail_task, ([scheduler]))
            scheduler.run()

        # reschedule this function to run again in a minute
        scheduler.enter(self.interval, 1, self.send_mail_task, ([scheduler]))

        # do whatever actual work this function requires, e.g.:
        self.scraper.update_all_jobs()
        self.mailer.email_each_user()

