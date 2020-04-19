from smtplib import SMTP
import email.message
import sys, getopt

def sendmailg(gserver , gport ,guser, gpass , mailfrom , mailto , subject ,msg , ishtml = 0):
    print(gserver + gport + guser + gpass + mailfrom + mailto + msg )
    if gserver == '' :
        print('you must set the parameter server .')
        sys.exit(1)
    elif gport == '' :
        print('you must set the parameter port .')
        sys.exit(1)
    elif mailfrom == '' :
        print('you must set the parameter mailfrom .')
        sys.exit(1)
    elif mailto == '' :
        print('you must set the parameter mailto .')
        sys.exit(1)
    elif subject == '' :
        print('you must set the parameter subject .')
        sys.exit(1)
    elif msg == '' :
        print('you must set the parameter msg .')
        sys.exit(1)
    else:
        print(gserver + gport + guser + gpass + mailfrom + mailto + msg )

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

def ghelp():
    print ('test.py -s --server -p --port -u --user -k --password -f --mailfrom -t --mailto -d --subject -m --messege')
    sys.exit()

def main(argv):
    gserver = ''
    gport = ''
    guser = ''
    gpass = ''
    mailfrom = ''
    mailto = ''
    subject = ''
    msg = ''
    if len(argv) > 0:
        opts, args = getopt.getopt(argv,"hs:p:u:k:f:t:d:m:",["help","server=","port=","user=","password=","mailfrom=","mailto=","subject=","messege="])
    else:
        ghelp()
    
    for opt, arg in opts:
        print('arg = '+ arg + ' opt = '+ opt)
        if opt in ('-h', "--help"):
            ghelp()
        elif opt in ("-s", "--server"):
            gserver = arg
        elif opt in ("-p", "--port"):
            gport = arg
        elif opt in ("-u", "--user"):
            guser = arg
        elif opt in ("-k", "--password"):
            gpass = arg
        elif opt in ("-f", "--mailfrom"):
            mailfrom = arg
        elif opt in ("-t", "--mailto"):
            mailto = arg
        elif opt in ("-d", "--subject"):
            subject = arg
        elif opt in ("-m", "--messege"):
            msg = arg
        else:
            sys.exit(1)
        
    sendmailg(gserver , gport , guser, gpass , mailfrom , mailto , subject ,msg , 1)
    


if __name__ == "__main__":
    main(sys.argv[1:])
