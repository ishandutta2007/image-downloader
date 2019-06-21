#codingutf-8

def write_to_file(name,content):
    f = open('F:\instagram3\%s.txt' % name,'w')
    print content
    content_lines = "\n".join(content).strip()
    f.write(content_lines)
    f.close()
    
if __name__ ==  "__main__":

    f = open("F:/instagram/niches/niches_new2.csv","r")
    lines = f.readlines()
    user_list = []
    for line in lines[:33]:
        if not line.replace("'","").replace(',',"").replace(",",'').strip():
            continue
        print line
        str_list = line.split(",")

        username = str_list[0]
        from hashtag import get_toptag

        keyword = str_list[3].replace('"', "")

        if not keyword:
            keyword = str_list[4].replace('"', "")
        keyword1 = keyword.split("+")[0]
        tag = get_toptag(keyword1)[:5]
        write_to_file(username,tag)
