import paramiko
import time
import os

ip='16.170.108.197'
uname='siva'
passwd='siva'
mo=paramiko.SSHClient()
mo.set_missing_host_key_policy(paramiko.AutoAddPolicy())
mo.connect(ip,username=uname,password=passwd)
location='C:\\Users\dell\\PycharmProjects\\pythonProject11\\Linux\\'+uname+'\\'

def take_dir_file(q,s):
    print(time.sleep(2.0))
    print('dividing the files and dirs....')
    print(time.sleep(2.0))
    if q not in s:
        print('i catch a dir file===',q)
        os.mkdir(location +str(q)[0:-1])
        print(time.sleep(3.0))
        operation_foor_dir(q)
    else:
        print('i catch a file===',q)
        print(time.sleep(2.0))
        operation_foor_file(q)

def operation_foor_dir(w):
    print('doing operation for dir...............',w)
    print(time.sleep(2.0))
    i,o,e=mo.exec_command('ls /home/siva/'+w)
    ii,oo,ee=mo.exec_command('ls /home/siva/'+w+'/*.*')
    files1=oo.readlines()
    fds1=o.readlines()
    if fds1==[]:
        print('nothing found inside---',w)
        print(time.sleep(2.0))
        temp='NOTHING INSIDE'+w
        return temp
    for i in fds1:
        print('i found some files inside---',w)
        print(time.sleep(2.0))
        ########print(time.sleep(2.0))
        print('dividing the files and dirs....')
        print(time.sleep(2.0))
        if i not in files1:
            print('i catch a dir file===', i)
            print(time.sleep(3.0))
            operation_foor_dir(i)
        else:
            print('i catch a file===', i)
            print(time.sleep(2.0))
            operation_f0r_file_inside_dir(i,w)

def operation_foor_file(z):
    print('i am doing file copying..........',z)
    print(time.sleep(2.0))
    i,o,e=mo.exec_command('cat '+z)
    a=o.readlines()
    f = open(location + str(z)[0:-1], 'w+')
    for j in a:
        f.write(j)
    print('file copying is completed....',z)
    print(time.sleep(2.0))

def operation_f0r_file_inside_dir(y,dir):
    print(' present i am inside  ====>>>>',dir)
    time.sleep(3.0)
    i,o,e=mo.exec_command('cat '+y)
    a=o.readlines()
    f=open(location + str(dir)[0:-1] + '\\' + str(y)[0:-1],'w+')
    for j in a:
        f.write(j)
    print('file copying completed')
    time.sleep(3.0)



import logging
logger=logging.getLogger('__name__')
logger.setLevel(logging.DEBUG)

formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

handler=logging.FileHandler('linux.log')
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

logger.addHandler(handler)

try:
    i, o, e = mo.exec_command('ls *.*')
    files = o.readlines()
    ii, oo, ee = mo.exec_command('ls')
    fds = oo.readlines()

    for i in fds:
        print('...........i am at first for loop....taking...', i)
        print(time.sleep(2.0))
        take_dir_file(i, files)
except Exception as e:
    logger.exception('here is the eror')
else:
    logger.info('NO ERROR OCCURED')