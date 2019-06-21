#coding=utf-8


def merge():
    f1 = open("C://Users//wu//Downloads//iGramTool//iGramTool//Data//FemaleFirstName.txt",'r')
    lines1 = f1.readlines()
    f1.close()


    f2 = open("C://Users//wu//Downloads//iGramTool//iGramTool//Data//LastName.txt",'r')
    lines2 = f2.readlines()
    f2.close()

    f3 = open("C://Users//wu//Downloads//iGramTool//iGramTool//Data//FullName.txt","w")
    lines3 = [str(x[0]).strip() +"." + x[1].strip() +"@gmail.com" for x in zip(lines1, lines2)]
    print lines3

    for line in lines3:
        f3.write(line+"\n")
    f3.close()

if __name__ == "__main__":
    merge()