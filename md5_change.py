import os


def change_md5(file_path):
    filename = open(file_path, 'rb').read()

    with open(file_path, 'wb') as new_file:

        new_file.write(filename+'\0')  #here we are adding a null to change the file content
    return new_file.name


if __name__ == "__main__":
    for root, dirs, files in os.walk("F://instagram//instagram-scraper"):

        for file in files:
            if file.endswith("jpg"):
                print root,file
                print os.path.join(root,file)
                change_md5(os.path.join(root,file))