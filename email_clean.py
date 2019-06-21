#coding=utf-8

def clean():
    f = open("C://Users//wu//Downloads//contacts_0508.txt",'r')
    lines = f.readlines()
    f.close()

    f = open("C://Users//wu//Downloads//contacts_0517.txt",'w')

    for line in lines:
        line = line.strip(".").strip(",").strip("#").strip("!").strip("-").strip("~").strip("+").strip("-")
        f.write(line+"\n")
    f.close()

def split_email():
    f = open("C://Users//wu//Downloads//contacts_0508.txt", 'r')
    lines = f.readlines()
    f.close()

    f2 =open("C://Users//wu//Downloads//contacts_0517_2.txt", 'w')
    for line in lines:
        if line.find("@") !=-1:
            continue
        f2.write(line+"\n")
    f2.close()

split_email()


