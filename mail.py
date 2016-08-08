#!python
#-*-coding:utf-8-*_

import smtplib
import socket
import dns.resolver

def getMXserver(domain):
	try:
		answers = dns.resolver.query(domain, 'MX')
		for rdata in answers:
			return str(rdata.exchange).rstrip('.')
	except:
		return None

socket.setdefaulttimeout(10)

sender = 'xxx@email.tuicool.com'
to = 'yy@126.com'
msg = b'Content-Type: text/plain; charset="utf-8"\r\n' \
      b'Subject: hello\r\n' \
      b'From: %s\r\n' \
      b'To: %s\r\n\r\n' \
      b'Hello, tanyi, I will arrived to ShenZhen tomorrow, will you come to the airport for me?\r\n.\r\n' %\
      (sender, to)

toHost = getMXserver(to.split('@')[1])
fromHost = sender.split('@')[1]
print('to host = ' + toHost + ', from host ' + fromHost)
server = smtplib.SMTP(toHost, 25, local_hostname=fromHost)
server.set_debuglevel(1)
server.starttls()
server.docmd('MAIL FROM:<%s> BODY=8BITMIME' % (sender))
server.docmd('RCPT TO:<%s>' % (to))
server.docmd('DATA')
server.send(msg)
data = server.getreply()
print(data)
server.quit()
