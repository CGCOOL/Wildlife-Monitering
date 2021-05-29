# Python code to illustrate Sending mail with attachments 
# from your Gmail account  
  
# libraries to be imported 
import smtplib
from threading import Thread
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

class EmailThread(Thread):
    def __init__(self,email_to,email_from,password,filename,image_path1,image_path2):
        Thread.__init__(self)
        self.email_to=email_to
        self.email_from=email_from
        self.password=password
        self.filename=filename
        self.image_path1=image_path1;
        self.image_path2=image_path2;
        
    def run(self):   
        fromaddr = self.email_from
        toaddr = self.email_to
           
        # instance of MIMEMultipart 
        msg = MIMEMultipart() 
          
        # storing the senders email address   
        msg['From'] = fromaddr 
          
        # storing the receivers email address  
        msg['To'] = toaddr 
          
        # storing the subject  
        msg['Subject'] = "Animal Monitered Updated excel Sheet"
          
        # string to store the body of the mail 
        body = "This is Yesterdays excel sheet and Data Viz"
          
        # attach the body with the msg instance 
        msg.attach(MIMEText(body, 'plain')) 
          
        # open the file to be sent  
        filename = self.filename
        attachment = open(filename, "rb") 
          
        # instance of MIMEBase and named as p 
        p = MIMEBase('application', 'octet-stream') 
          
        # To change the payload into encoded form 
        p.set_payload((attachment).read()) 
          
        # encode into base64 
        encoders.encode_base64(p) 
           
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
          
        # attach the instance 'p' to instance 'msg' 
        msg.attach(p) 
        
        filename2 = self.image_path1
        attachment = open(filename2, "rb") 
          
        # instance of MIMEBase and named as p 
        p = MIMEBase('application', 'octet-stream') 
          
        # To change the payload into encoded form 
        p.set_payload((attachment).read()) 
          
        # encode into base64 
        encoders.encode_base64(p) 
           
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename2) 
          
        # attach the instance 'p' to instance 'msg' 
        msg.attach(p)

        filename3 = self.image_path2
        attachment = open(filename3, "rb") 
          
        # instance of MIMEBase and named as p 
        p = MIMEBase('application', 'octet-stream') 
          
        # To change the payload into encoded form 
        p.set_payload((attachment).read()) 
          
        # encode into base64 
        encoders.encode_base64(p) 
           
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename3) 
          
        # attach the instance 'p' to instance 'msg' 
        msg.attach(p)

        # creates SMTP session 

        s = smtplib.SMTP('smtp.gmail.com', 587) 
          
        # start TLS for security 
        s.starttls() 
          
        # Authentication 
        s.login(fromaddr,self.password) 
          
        # Converts the Multipart msg into a string 
        text = msg.as_string() 
          
        # sending the mail 
        s.sendmail(fromaddr, toaddr, text) 
          
        # terminating the session 
        s.quit() 


def send1(email_to,email_from,password,filename,image_path1,image_path2):
    EmailThread(email_to,email_from,password,filename,image_path1,image_path2).start()




    
