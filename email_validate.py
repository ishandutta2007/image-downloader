#coding=utf-8
import requests,json

def validate():
    unclean = open("C://Users//wu//Downloads//contacts_0508.txt")
    lines = unclean.readlines()
    f = open("clean_email_0520.txt", "w")

    for line in lines:
        line = line.strip().strip("@").strip("-").strip(".").strip("+").strip("!")
        #line = "descuaula@gmail.com"
        url = "https://emailverifier.co/apiv1/verify/"
        resp = requests.post(url,data={"email":line})
        content = resp.content
        print type(content)
        print content
        json_content = json.loads(content)
        print type(json_content)
        status = json_content.get("valid")
        print line,status
        if status :
            f.write(line+"\n")

    f.close()

if __name__ == "__main__":
    validate()