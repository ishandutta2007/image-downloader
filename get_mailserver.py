#coding=utf-8


def get_mail():
    f = open("contacts_0610.csv")
    lines = f.readlines()
    f.close()

    d ={}
    for line in lines:
        mail = line.split("@")[1].strip()
        d[mail] = d.get(mail,0)+1

    print d

    print d.keys()

if __name__ == "__main__":
    get_mail()