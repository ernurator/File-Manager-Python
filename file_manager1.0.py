import os
from datetime import datetime

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


s = input('Enter directory in form C:/Users/.../Folder1/Folder2: ')
os.system('cls')
inFile = False


while True:
    if not inFile:
        printMenuDir()

        command = int(input())

        if command == 0:
            break

        elif command == 1:  #files list
            cnt = 0
            for item in os.scandir(s):
                if item.is_file():
                    cnt += 1
                    print(f'{convert_date(item.stat().st_mtime)} \t {item.name}')
            print(f'\n{cnt} file(-s)\n')
            input('Press ENTER to continue')
            os.system('cls')

        elif command == 2:  #dir-s list
            cnt = 0
            for item in os.scandir(s):
                if item.is_dir():
                    filecnt = 0
                    dircnt = 0
                    cnt += 1
                    for items in os.scandir(os.path.join(s, item.name)):
                        if items.is_dir():
                            dircnt += 1
                        elif items.is_file():
                            filecnt += 1
                    print(f'{convert_date(item.stat().st_mtime)} \t {item.name} \t {filecnt} files, {dircnt} dirs inside')
            print(f'\n{cnt} directory(-ies)\n')
            input('Press ENTER to continue')
            os.system('cls')

        elif command == 3:  #content list
            dircnt = 0
            filecnt = 0
            for item in os.scandir(s):
                if item.is_dir():
                    dircnt += 1
                elif item.is_file():
                    filecnt += 1
                print(f'{convert_date(item.stat().st_mtime)} \t {item.name}')
            print(f'\n{filecnt} files, {dircnt} dirs inside\n')
            input('Press ENTER to continue')
            os.system('cls')

        elif command == 4:  #renaming directory
            src = os.path.join(s, input('Enter directory name: '))
            dst = os.path.join(s, input('Enter new name: '))
            if os.path.exists(src):
                os.rename(src, dst)
                print('Directory successfully renamed\n')
            else:
                print('Directory is not found\n')
            input('Press ENTER to continue')
            os.system('cls')

        elif command == 5:  #create new file
            name = input('Enter file name: ')
            file = open(os.path.join(s, name), mode='w+')
            print(f'File {name} successfully created\n')
            file.close()
            input('Press ENTER to continue')
            os.system('cls')

        
        elif command == 6:  #create new dir
            name = input('Enter dir name: ')
            f_p = os.path.join(s, name)
            if not os.path.exists(f_p):
                os.mkdir(f_p)
                print(f'Directory {name} successfully created\n')
            else:
                print('Such directory already exists\n')
            input('Press ENTER to continue')
            os.system('cls')

        elif command == 7:  #go to file
            name = input('Enter file name: ')
            dst = os.path.join(s, name)
            if os.path.exists(dst):
                s = dst
                inFile = True
            else:
                print('File is not found\n')
                input('Press ENTER to continue')
            os.system('cls')




    else:
        printMenuFile()

        command = int(input())

        if command == 0:
            s, _ = os.path.split(s)
            inFile = False
            os.system('cls')
            
        elif command == 1: #file deleting
            os.remove(s)
            print('File deleted\n')
            s, _ = os.path.split(s)
            inFile = False
            input('Press ENTER to continue')
            os.system('cls')

        elif command == 2: #file renaming
            name = input('Enter new file name (without extension): ')
            name = os.path.join(os.path.split(s)[0], name) + os.path.splitext(s)[1]
            os.rename(s, name)
            s = name
            print('File successfully renamed\n')
            input('Press ENTER to continue')
            os.system('cls')

        elif command == 3: #file appending
            with open(s, mode='a') as file:
                file.write('\n')
                cont = input('Enter text, to finish print empty line: ')
                while cont != '':
                    file.write(f'{cont}\n')
                    cont = input()
            print('File successfully edited\n')
            print()
            input('Press ENTER to continue')
            os.system('cls')

        elif command == 4: #file rewriting
            with open(s, mode='w') as file:
                cont = input('Enter new text, to finish print empty line: ')
                while cont != '':
                    file.write(f'{cont}\n')
                    cont = input()
            print('File successfully edited\n')
            input('Press ENTER to continue')
            os.system('cls')
            
        elif command == 5: #file content
            with open(s) as file:
                print(f'\t{os.path.basename(s)}')
                print(file.read())
            print()
            input('Press ENTER to continue')
            os.system('cls')
