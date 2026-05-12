#━━━━━━━━━━━#ToolStart#━━━━━━━━━━━━━
#Tool Admin  :- Jisan Hassan
#Tool Verson :- 0.1
#━━━━━━━━━━━#Import#━━━━━━━━━━━━━
import os,base64,marshal,time,requests,httpx,urllib.parse,subprocess,urllib.parse,glob,re,platform, sys, random, subprocess, threading, itertools,base64,uuid,zlib,re,json,uuid,subprocess,shutil,webbrowser,time,json,sys,random,datetime,time,re,subprocess,platform,string,json,time,re,random,sys,string,uuid,httpx
from string import * 
#━━━━━━━━━━━#Colors#━━━━━━━━━━━━━
W = '\033[1;37m'
G = '\033[1;32m'
C = '\033[1;36m'
R = '\033[1;31m'
Y = '\033[1;33m'
#━━━━━━━━━━━#Clear#━━━━━━━━━━━━━
def clear():
    os.system('clear')
    print(logo)
#━━━━━━━━━━━#linex#━━━━━━━━━━━━━
def linex():
	print(f"{W}────────────────────────────────────────────")
#━━━━━━━━━━━#Logo#━━━━━━━━━━━━━
logo = f"""
{W}        █████╗ ██╗    ██╗███╗   ███╗
       ██╔══██╗██║    ██║████╗ ████║
       ███████║██║ █╗ ██║██╔████╔██║
       ██╔══██║██║███╗██║██║╚██╔╝██║
       ██║  ██║╚███╔███╔╝██║ ╚═╝ ██║
       ╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝     ╚═╝
{W}────────────────────────────────────────────
{W}[{C}•{W}] FACEBOOK   {R}:{W} MD JISAN HASAN
{W}[{C}•{W}] FEATURE    {R}:{W} KIDS BYPASS
{W}[{C}•{W}] VERSION    {R}:{W} 1.0{G} PREMIUM 
{W}[{C}•{W}] GITHUB     {R}:{W} MR-AWM-149
{W}────────────────────────────────────────────"""
#━━━━━━━━━━━#Main#━━━━━━━━━━━━━
def Main():
	clear()	
	print(f"{W}[{G}1{W}]{R} MR OGGY TOOL BYPASS")
	print(f"{W}[{G}2{W}] JOIN OUR FACEBOOK GROUP")
	print(f"{W}[{G}3{W}] FOLLOW MY GITHUB PROFILE")
	print(f"{W}[{G}4{W}] REPORT DEVELOPER {W}({G}FB{W})")
	print(f"{W}[{R}0{W}] EXIT PROGRAM </>")
	print(f"{W}────────────────────────────────────────────")
	opt = input(f"{W}[{G}•{W}] SELECT </> : ")
	if opt=="1":
		print(f"{Y}PROCESSING BYPASS PLEASE WAIT...")
		time.sleep(10)
		try:
			import oggy
		except Exception as e:
			print(f"{R}ERROR : {e}")
	elif opt=="2":
		os.system('xdg-open https://facebook.com/groups/4538497673104082/')
	elif opt=="3":
		os.system('xdg-open https://github.com/MR-AWM-149')
	elif opt=="4":
		os.system('xdg-open https://www.facebook.com/profile.php?id=61589343792308')
	elif opt=="0":
		print(f"{R}EXIT DONE")
	else:
		print(f"{R}INVALID OPTION")
	
Main()
