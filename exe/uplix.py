import requests
from bs4 import BeautifulSoup
from re import findall
from wget import download
from json import loads
from sys import argv

def up(filename):
    files = {
        'file': open(filename, 'rb'),
    }

    response = requests.post('https://api.bayfiles.com/upload', files=files)

    return(loads(response.text.replace('\\',''))['data']['file']['metadata']['id'])


def dl(id):
    file = requests.get(f'https://bayfiles.com/{id}')    
    soup = BeautifulSoup(file.content,'html.parser')
    link = soup.find('a',{'id':'download-url'})
    link = findall('href="(.*)" id',link.decode())[0]
    download(link)

try:
        if argv[1] == 'up':
            print('please wait ...')
            print(f'file code : {up(argv[2])}')
        elif argv[1] == 'dl':
            print('please wait ...\n')
            dl(argv[2])
except:
    option = input('''please enter option : 
    [1] : (download)
    [2] : (upload)
    please enter option number :  ''')
    if option == '1' or option == 'download' or option == 'dl':
        key = input('please enter file key : ')
        print('please wait ...\n') 
        dl(key)
    if option == '2' or option == 'upload' or option == 'up':
        name = input('please enter file name : ')
        print('please wait ...')
        print(f'file code : {up(name)}')
    input()