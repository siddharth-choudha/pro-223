import zipfile
import time

folderpath = input('Path to the file: ')
zipf = zipfile.ZipFile(folderpath)
global result
result = 0
global tried
tried = 0
c=0
if not zipf:
    print('the zipped file/folder is not password protected! You can successfully open it!')
else :
    starttime = time.time()
    wordListFile = open('wordlist.txt','r',errors = 'ignore')
    body = wordListFile.read().lower()
    words = body.split('\n')

    for i in range(len(words)):
        word = words[i]
        password = word.encode('utf-8').strip()
        c=c+1
        print('Trying to decode password by: {}'.format(word))
        try:
            with zipfile.ZipFile(folderpath,'r') as zf:
                zf.extractall(pwd=password)
                print("Success! The password is:"+ word)
                endtime = time.time()
                result = 1
            break
        except:
            pass


   
