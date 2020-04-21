from smtplib import SMTP
import email.message
import sys

def sendmailg(gserver , gport ,guser, gpass , mailfrom , mailto , subject ,msg , ishtml = 0):
    #print(gserver + gport + guser + gpass + mailfrom + mailto + msg )
    mailmsg = email.message.Message()
    mailmsg['From'] = mailfrom
    mailmsg['To'] = mailto
    mailmsg['Subject'] = subject

    if ishtml == 1:
        mailmsg.add_header('Content-Type','text/html')
    else:
        mailmsg.add_header('Content-Type','text/plain')

    mailmsg.set_payload (msg)
    with SMTP(gserver , gport)  as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(guser, gpass)  
        smtp.set_debuglevel(1)
        smtp.sendmail(mailfrom, mailto,mailmsg.as_string())
        smtp.quit()

def main(argv):
    W  = '\033[0m'  # white (normal)
    R  = '\033[31m' # red
    G  = '\033[32m' # green
    O  = '\033[33m' # orange
    B  = '\033[34m' # blue
    P  = '\033[35m' # purple
    print('\t{}Welcome to mail sender framework ......{}'.format(G,G))
    print('\t{}you can use this framework for sending mails to a single email or email list{}'.format(R,R))
    print('\t{}1- Single Email . {}'.format(O,O))
    print('\t{}2- Multi Emails in file . {}'.format(O,O))    
    sendtype = -1
    while True:
        sendtype = int(input('\t{0}Enter Your choice : {1}'.format(B,B)))
        if sendtype > 2 or sendtype < 0 :
            print('{}\tYou Entered a wrong choice please insert a valid one .{}'.format(R,R))
        else:
            if sendtype == 1:
                print('{}\tyou choosed {} then you want send mail for single mail{}'.format(R,sendtype,R))
            else:
                print('{}\tyou choosed {} then you want send mail for Multi email from file{}'.format(R,sendtype,R))
            
            break
    gserver = input('\t{0}Enter The Smtp Server : {1}'.format(B,B))
    gport = int(input('\t{0}Enter The Smtp port : {1}'.format(B,B)))
    guser = input('\t{0}Enter The Smtp User : {1}'.format(B,B))
    gpass = input('\t{0}Enter The Smtp password : {1}'.format(B,B))
    mailfrom = input('\t{0}Enter The sender email : {1}'.format(B,B))
    if sendtype == 1 :
        mailto = input('\t{0}Enter The reciver email : {1}'.format(B,B))
    else:
        mailto = input('\t{0}Enter The recivers emails file : {1}'.format(B,B))
    subject = input('\t{0}Enter The Subject : {1}'.format(B,B))
    msg = input('\t{0}Enter The mail Body : {1}'.format(B,B))
    while True:
        ishtml = input('\t{0}is the message is html yes or no: {1}'.format(B,B))
        if ishtml == 'yes':
            intishtml = 1
            break
        elif ishtml == 'no' :
            intishtml = 0
            break
    if sendtype == 1 :
        sendmailg(gserver , gport , guser, gpass , mailfrom , mailto , subject ,msg , intishtml)
    else:
        f = open(mailto,'r')
        with line in f:
            sendmailg(gserver , gport , guser, gpass , mailfrom , line , subject ,msg , intishtml)
    

if __name__ == "__main__":
    main(sys.argv[1:])
