import smtplib

server = smtplib.SMTP('smtp.webfaction.com',587)
server.set_debuglevel(True)
server.ehlo()

server.has_extn('STARTTLS')

server.esmtp_features.keys()

server.starttls()
server.ehlo()
server.login("crisewing_demobox","s00p3rs3cr3t")

from_addr = "Maria Korchagin <maria.korchagin@gmail.com>"
to_addrs = "demo@crisewing.com"
subject = "this is a test"
message = "a message from python smtplib"

template = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
headers = template % (from_addr, to_addrs, subject)

email_body = headers + message

server.sendmail(from_addr, [to_addrs,], email_body)

server.close()
del server





