# MailServer
create your own smtp server, so that you can mail to anyone

Only can send email is not enough to be a email server. You should registered for SPF, and configure
dns reverse lookup(in ISP configure page) so that mail server like gmail will trust you and allow you to send email to it's users.


Sometimes, we need use DKIM(DomainKeys Identified Mail, http://www.dkim.org/).

If you completed all above, then you have one email that you can use to send mail to anyone in gmail or outlook, etc.

