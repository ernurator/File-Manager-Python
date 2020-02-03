import os
from datetime import datetime
from os import getcwd as curDir


def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    f_d = d.strftime('%d.%m.%Y\t%H:%M')
    return f_d


def printMenuDir():
    print('''Press 1 to see info about all files in directory
Press 2 to see all directories
Press 3 to list content of directory
Press 4 to rename directory
Press 5 to create new file in this dir
Press 6 to add new directory to this directory
Press 7 to work with file
Press 0 to exit
''')


def printMenuFile():
    print('''Press 1 to delete file
Press 2 to rename file
Press 3 to add content to file
Press 4 to rewrite the file content
Press 5 to see file content
Press 0 to go back
''')


def endOfCmd():
    input('Press ENTER to continue')
    os.system('cls')


os.chdir(input('Enter directory in form C:/Users/.../Folder1/Folder2: '))
os.system('cls')
inFile = False
curFile = ''


def fileList():
    file_list = [(item.stat().st_mtime, item.name)
                 for item in os.scandir(curDir()) if item.is_file()]
    for item in file_list:
        print(f'{convert_date(item[0])} \t {item[1]}')
    print(f'\n{len(file_list)} file(-s)\n')
    endOfCmd()


def dirList():
    dir_list = [item for item in os.scandir(curDir()) if item.is_dir()]
    for item in dir_list:
        filecnt = dircnt = 0
        for items in os.scandir(item):
            if items.is_dir():
                dircnt += 1
            elif items.is_file():
                filecnt += 1
        print(
            f'{convert_date(item.stat().st_mtime)} \t {filecnt} files, {dircnt} dirs inside \t {item.name}')
    print(f'\n{len(dir_list)} directory(-ies)\n')
    endOfCmd()


def contentList():
    cont_list = [item for item in os.scandir(curDir())]
    dircnt = filecnt = 0
    for item in cont_list:
        if item.is_dir():
            dircnt += 1
        elif item.is_file(): filecnt += 1
        print(f'{convert_date(item.stat().st_mtime)} \t {item.name}')
    print(f'\n{filecnt} files, {dircnt} dirs inside\n')
    endOfCmd()


def renameDir(src, dst):
    if not os.path.exists(src):
        print('Directory is not found\n')
    elif os.path.exists(dst):
        print(f'Directory {dst} already exists\n')
    else:
        os.rename(src, dst)
        print('Directory successfully renamed\n')
    endOfCmd()


def createFile(name):
    file = open(name, mode='w+')
    print(f'File {name} successfully created\n')
    file.close()
    endOfCmd()


def createDir(name):
    if not os.path.exists(name):
        os.mkdir(name)
        print(f'Directory {name} successfully created\n')
    else:
        print('Such directory already exists\n')
    endOfCmd()


def renameFile(name, cf) -> bool:
    if not os.path.exists(name):
        os.rename(curFile, name)
        print('File successfully renamed\n')
        return True
    else:
        print(f'File {name} already exists\n')
        return False
    

def appendFile():
    with open(curFile, mode='a') as file:
        file.write('\n')
        cont = input('Enter text, to finish print empty line: ')
        while cont != '':
            file.write(f'{cont}\n')
            cont = input()
    print('File successfully edited\n')
    endOfCmd()


def rewriteFile():
    with open(curFile, mode='w') as file:
        cont = input('Enter new text, to finish print empty line: ')
        while cont != '':
            file.write(f'{cont}\n')
            cont = input()
    print('File successfully edited\n')
    endOfCmd()


def readFile():
    with open(curFile) as file:
        print(f'\t{curFile}')
        print(file.read())
    print()
    endOfCmd()

while True:
    if not inFile:
        printMenuDir()

        command = int(input())

        if command == 0:
            break

        elif command == 1:  # files list
            fileList()

        elif command == 2:  # dir-s list
            dirList()

        elif command == 3:  # content list
            contentList()

        elif command == 4:  # renaming directory
            src = input('Enter directory name: ')
            dst = input('Enter new name: ')
            renameDir(src, dst)

        elif command == 5:  # create new file
            name = input('Enter file name: ')
            createFile(name)

        elif command == 6:  # create new dir
            name = input('Enter dir name: ')
            createDir(name)

        elif command == 7:  # go to file
            name = input('Enter file name: ')
            if os.path.exists(name):
                inFile = True
                curFile = name
            else:
                print('File is not found\n')
                input('Press ENTER to continue')
            os.system('cls')

    else:
        printMenuFile()

        command = int(input())

        if command == 0:
            curFile = ''
            inFile = False
            os.system('cls')

        elif command == 1:  # file deleting
            os.remove(curFile)
            print('File deleted\n')
            curFile = ''
            inFile = False
            endOfCmd()

        elif command == 2:  # file renaming
            name = input('Enter new file name (without extension): ')
            name = name + os.path.splitext(curFile)[1]
            if renameFile(name, curFile): curFile = name
            endOfCmd()

        elif command == 3:  # file appending
            appendFile()

        elif command == 4:  # file rewriting
            rewriteFile()

        elif command == 5:  # file content
            readFile()
