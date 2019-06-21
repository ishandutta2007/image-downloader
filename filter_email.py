#coding=utf8
import os

def email_list():

    pass

if __name__ =="__main__":
    l = []
    for path, directories, files in os.walk('C://Users//wu//AppData//Roaming//rootjazz//Instadub//saved_data'):

        for index,name in enumerate(files):
            if name.lower().startswith("email"):
                f = open(os.path.join(path, name), "r")
                lines = f.readlines()

                f.close()
                for line in lines:
                    line = line.strip()
                    if line:
                        email = line.split("\t")[-1].strip()
                        l.append(email)


    f = open("F://instagram_email.txt","w")
    for l1 in l:
        f.write(l1+"\n")
    f.close()

    d = {}
    for tmp in l:
        end = tmp.split("@")[-1]
        d[end] = d.get(end,0)+1

    import operator
    sorted_x = sorted(d.items(), key=operator.itemgetter(1),reverse=True)
    print sorted_x[:25]
