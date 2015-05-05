from smtplib import SMTPRecipientsRefused
import datetime
from django.core.mail import send_mail
from signup_app.models import User
from webscraperapp.models import Job

__author__ = 'shannon'

class Mailer:

    DEFAULT_FROM_ADDRESS = 'impactcareersdaily@gmail.com'
    DEFAULT_SUBJECT = 'New jobs for you!'

    def sendJobMail(self, user):
        today = datetime.date.today()

        #keep a normal message for non-html email clients
        message = "Check out today's new jobs for you!\n"
        #ideally we want users to receive the html stylized email
        html_message = self.get_html_message_start()

        #loop through all this users' topics and list the new jobs for that topic
        for topic in user.topics.all():
            message += "Topic: " + topic.name + "\n"
            html_message += """<h3>""" + topic.name + """</h3>"""
            if topic.job_set.all().filter(found_date=today).count() > 0:
                html_message += """<ul style="list-style-type: disc">"""
                for job in topic.job_set.all().filter(found_date=today)[:15]:#limiting to only 15 so users aren't overwhelmed
                    message += str(job) + "\n"
                    html_message += self.job_to_html(job)
                html_message += """</ul>"""
            else:
                message += "No new " + topic.name + " jobs for today, stay tuned tomorrow!"
                html_message += """<p>No new """ + topic.name + """ jobs for today, stay tuned tomorrow!</p>"""
        message += "\n\nAdditional jobs that may interest you: \n"
        html_message += """</br></br><h3>Additional jobs that may interest you</h3>"""
        html_message += """<ul style="list-style-type: disc">"""
        for job in Job.objects.filter(found_date=today).filter(topics=None)[:10]:
            message += str(job) + "\n"
            html_message += self.job_to_html(job)
        html_message += """</ul>"""
        html_message += self.get_html_message_end()

        self.send_mail(user.email, self.DEFAULT_FROM_ADDRESS, self.DEFAULT_SUBJECT, message, html_message)

    def send_mail(self, toAddress, fromAddress, subject, message, html_message=None):
        send_mail(subject, message, fromAddress, [toAddress], fail_silently=False, html_message=html_message)

    def email_each_user(self):
        for user in User.objects.all():
            print("trying to send to " + user.email)
            try:
                self.sendJobMail(user)
                print("mail sent to " + user.email)
            except SMTPRecipientsRefused:
                print("failed to send to " + user.email)

    def job_to_html(self, job):
        html = """\
            <li style="display: list-item"><b>"""
        html += job.company
        html += """\
            </b> is looking for a <a href="
                """
        html += job.link
        html += """\
            ">"""
        html += job.title
        html += """\
            </a> in <i>"""
        html += job.location
        html += """\
            </i></li>
        """
        return html

    def get_html_message_start(self):
        html = """\
            <html>
              <head></head>
              <body>
                <div style="background: #ffffff;">
                    <h1 style="text-align: center; background: rgba(104, 208, 60); color: #ffffff; padding: 10px;">Impact Careers Daily</h1>
                    <p>Check out today's new jobs for you!</p>

            """
        return html

    def get_html_message_end(self):
        html = """\

                </div>
              </body>
            </html>
                """
        return html