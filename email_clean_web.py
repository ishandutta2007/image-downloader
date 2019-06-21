#coding=utf-8


from email_validator import validate_email, EmailNotValidError



def begin(email):
    f = open("clean_email_0607.txt",'w')
    try:
        v = validate_email(email)  # validate and get info
        email = v["email"]  # replace with normalized form
        f.write(email+"\n")
    except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
        print str(e)

    f.close()


if __name__ == "__main__":
    f = open("C://Users//wu//Desktop//email_bad.txt")
    lines = f.readlines()
    f.close()
    for line in lines:

        email = line.strip()
        begin(email)

