from database import mail
from flask_mail import Message
from datetime import datetime
import pytz

class CommonUtils():
    def __init__(self):
        self.name = 'Mahesh'

    #=======================================================================================================
    #    Send Mail with provided info
    #=======================================================================================================
    def sendMail(self, subject, html, recipients):
        try:
            msg = Message(subject=subject, html=html, recipients=recipients)
            # mail.connect()
            mail.send(msg)
            return True
        except Exception as err:
            print(err)
            return False

    def getCurrentDateTime(self):
        # it will get the time zone 
        # of the specified location
        IST = pytz.timezone('Asia/Kolkata')
        datetime_ist = datetime.now(IST)
        # datetime_ist.strftime('%Y:%m:%d %H:%M:%S %Z %z')
        return datetime_ist
