#coding=utf-8

import os
def begin():
    pass

if __name__ == "__main__":
    f = []
    for (dirpath, dirnames, filenames) in os.walk("C://Users//wu//Documents//instagram//instagr"):
        for filename in filenames:
            if filename.endswith('csv'):
                f.append(os.path.join(dirpath, filename))

    lines = []
    for tmp in f:
        ftmp = open(tmp,"r")
        line = ftmp.readlines()
        print line
        ftmp.close()

    clean_files = []
    print lines
    for line in lines:
        print line
        url = line.split(" ")[1]
        if url.startswith("http"):
            clean_files.append(url)
    print clean_files

