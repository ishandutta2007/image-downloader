#cdoing=utf-8

def replace():
    f = open("C://Users//wu//Downloads//keyword.txt","r")
    lines = f.readlines()
    f.close()
    line_list = []
    for line in lines:
        if not line.strip():continue
        line_list.append(line)
    f = open("C://Users//wu//Downloads//keyword_1.txt","a")
    for line in line_list:
        if not line:continue
        line = line.replace("-",' ')
        f.write(line)
    f.close()

if __name__ == "__main__":
    replace()