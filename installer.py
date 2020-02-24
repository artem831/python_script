#!/usr/bin/python
# autor artem
# v 0.0.1

from colorama import *
import os
os.system('clear')
t = '''

 	     ██
 ▄▄█████▄  ███████    ██▄████
 ██▄▄▄▄ ▀    ██       ██▀
  ▀▀▀▀██▄    ██       ██
 █▄▄▄▄▄██    ██▄▄▄    ██
  ▀▀▀▀▀▀      ▀▀▀▀    ▀▀

'''
lines = '---------------------------------------'
info = '''
версия:0.0.1
рут:не нужен
интернет нужен
лицензии:нет
автор:артём
сделано:в России
вк:нету
телеграмм:есть но не дам
'''
menu = '''
[1]-ddos
[2]-installers
[3]-exploits
[4]-spam
[5]-other
'''
ins = '''
[1]-darkfly
[2]-termux_bash_script
[3]-lazymux
'''
exp = '''
[1]-metasploit
[2]-routersploit
[3]-websploit
[4]-nmap
'''
d = '''
[1]-xerxes
[2]-ddos
[3]-goldeneye
[4]-hulk
[5]-hammer
'''
spy = '[1]-spymer'
def dos():
	os.system('clear')
	print(Fore.RED + d)
	da = input()
	if da == '1':
		os.system('git clone https://github.com/sepehrdaddev/Xerxes')
	elif da == '2':
		os.system('git clone https://github.com/Ha3MrX/DDos-Attack')
	elif da == '3':
		os.system('git clone https://github.com/jseidl/GoldenEye')
	elif da == '4':
		os.system('git clone https://github.com/grafov/hulk')
	elif da == '5':
		os.system('git clone https://github.com/cyweb/hammer')
def install():
	os.system('clear')
	print(Fore.RED + ins)
	inst = input()
	if inst == '1':
		os.system('git clone https://github.com/Ranginang67/DarkFly-Tool')
	elif inst == '2':
		os.system('git clone https://github.com/artem831/termux_bash_script')
	elif inst == '3':
		os.system('git clone https://github.com/Gameye98/Lazymux')

def exploit():
	os.system('clear')
	print(Fore.RED + exp)
	ex = input()
	if ex == '1':
		os.system('pkg install unstabel-repo')
		os.system('pkg install metasploit')
	elif ex == '2':
		os.system('git clone https://github.com/threat9/routersploit')
	elif ex == '3':
		os.system('git clone https://github.com/websploit/websploit')
	elif ex == '4':
		os.system('pkg install nmap')
def spa():
	os.system('clear')
	print(Fore.RED + spy)
	sp = input()
	if sp == '1':
		os.system('git clone https://github.com/FSystem88/spymer')




def main():
	print(Fore.GREEN + lines)
	print(Fore.RED + t)
	print(Fore.GREEN + lines)
	print(Fore.YELLOW + info)
	print(Fore.GREEN + lines)
	print(Fore.BLUE + menu)
	what = input('root@you|> ')
	if what == '1':
		dos()
	elif what == '2':
		install()
	elif what == '3':
		exploit()
	elif what == '4':
		spa()
	elif what == '5':
		pass
	else:
		print('ошибка')
main()
