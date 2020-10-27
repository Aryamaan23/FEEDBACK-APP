import smtplib
from email.mime.text import MIMEText

def send_mail(customer,dealer,rating,comments):
    port=2525
    smtp_server='smtp.mailtrap.io'
    login='a8de1ec55e6acf'
    password='bd3e77287dda91'
    message=f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Ratings: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_mail='pandeyaryamaan@gmail.com'
    receiver_mail='ap8209@srmist.edu.in'
    msg=MIMEText(message,'html')
    msg['Subject']='Lexus Feedback'
    msg['From']=sender_mail
    msg['To']=receiver_mail

    #Send email
    with smtplib.SMTP(smtp_server,port) as server:
        server.login(login,password)
        server.sendmail(sender_mail,receiver_mail,msg.as_string())



