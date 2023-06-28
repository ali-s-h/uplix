import os
import time

# # os.system('''
# # %SystemRoot%\System32\setx share ""
# # ''')
appname = 'uplix.exe'
command = 'share'
cwd = os.getcwd()

def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='>'):
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if iteration == total:
        print()
def loading():
    items = list(range(0, 40))
    l = len(items)

    loadbar(0, l, prefix='Progress:', suffix='Done', length=l)
    for i, item in enumerate(items):
        time.sleep(0.05)
        loadbar(i + 1, l, prefix='Progress:', suffix='Done', length=l)
def install():
    print('please wait ...')
    os.system(f'''
%SystemRoot%\System32\setx {command} "{cwd}\{appname}"
    ''')
    os.system('cls')
install()
loading()