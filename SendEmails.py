# -*- coding: utf-8 -*-
"""
==============================================
Program : custom_mass_email/SendEmails.py
==============================================
Summary:
"""
__author__ = "Sadman Ahmed Shanto"
__date__ = "09/29/2021"
__email__ = "sadman-ahmed.shanto@ttu.edu"

import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from Emailer import Emailer


class SendEmails:
    """Docstring for SendEmails. """
    def __init__(self, csvFile):
        self.csvFile = csvFile
        self.data = self.getData()

    def getData(self):
        data = pd.read_csv(
            self.csvFile,
            delimiter=',',
            names=['email', 'name', 'program', 'university', 'availability'])
        return data

    def sendEmail(self):
        emailList = self.data['email'].values
        sms_list = ['8067900156@sms.mycricket.com']
        subjectLine = "Prospective Graduate Student"
        emailContent = ""
        salutation = "\nBest,\nSadman Ahmed Shanto\nResearch Assistant, Advanced Particle Detector Lab\nTeaching Assistant, \"Introduction to Quantum Information and Computing\"\nApplied Physics | Mathematics | Computer Science"
        pdf = "Sadman_Ahmed_Shanto_Grad_CV.pdf"
        sender = Emailer(emailList, sms_list, subjectLine, emailContent)
        for i in self.data.index:
            name = self.data['name'][i]
            email = self.data['email'][i]
            program = self.data['program'][i]
            uni = self.data['university'][i]
            content = "Dear Dr. {},\n\nI am Sadman Ahmed Shanto, a senior Applied Physics major with minors in Math and Computer Science from Texas Tech University. I am very interested in your research, and have recently applied to the {} program at {}. I was wondering if I could schedule a zoom meeting with you some time this month to get some of my questions answered and learn a little bit more about ongoing projects. If this is not possible, we can correspond through email instead. Please let me know what works for you and thank you for your time.\n\nHoping you are staying safe, and doing well.\n{}".format(
                name, program, uni, salutation)
            try:
                print("Emailing {}".format(email))
                sender.send_email_pdf_figs(pdf, subjectLine, content, email)
            except:
                print("email error for {}".format(email))


if __name__ == "__main__":
    SendEmails("FollowUp.csv").sendEmail()
