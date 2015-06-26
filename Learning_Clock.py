#!/usr/bin/python -i
import os
import sys
import time
def peep(intervall,dauer):
	i=intervall
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.1,1000))
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.1,1200))

	while i<=dauer:
		time.sleep(intervall)
		os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (1,700))
		i=i+intervall
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.1,1200))
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.1,1000))

def peep_ad(endif,Intervall1,Intervall2,komment1,komment2,dauer):
#	i=max(Intervall1,Intervall2)
	i=0
	if dauer==0:
		return	
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.1,1000))
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.1,1200))
	print("Timer gestartet")
	if endif=="max":	
		print"maximal duration"
		while i<dauer:
			if i<dauer:	
				if Intervall1 > 0:
					print(komment1)
					time.sleep(Intervall1)
					i=i+Intervall1
					os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (1,700))
			else:
				break
			if i<dauer:
				if Intervall2 > 0:
					print(komment2)
					time.sleep(Intervall2)
					os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (1,700))
					i=i+Intervall2
			else:
				break
	elif endif=="min":
		print"minimal duration"
		while i<=dauer:
			if (i+Intervall1)<=dauer:	
				if Intervall1 > 0:
					print(komment1)
					time.sleep(Intervall1)
					i=i+Intervall1
					os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (1,700))
			else:
				break
			if (i+Intervall2)<=dauer:
				if Intervall2 > 0:
					print(komment2)
					time.sleep(Intervall2)
					os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (1,700))
					i=i+Intervall2
			else:
				break
	
	else:
		print"default: minimal duration"
		while i<=dauer:
			if (i+Intervall1)<=dauer:	
				if Intervall1 > 0:
					print(komment1)
					time.sleep(Intervall1)
					i=i+Intervall1
					os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (1,700))
			else:
				break
			if (i+Intervall2)<=dauer:
				if Intervall2 > 0:
					print(komment2)
					time.sleep(Intervall2)
					os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (1,700))
					i=i+Intervall2
			else:
				break
	rest=dauer-i
	if rest>60:
		rest=rest/60
		rest=str(rest)+"m"
	elif rest>3600:
		rest=rest/3600
		rest=str(rest)+"h"
	else:
		rest=str(rest)+"s"
	print"Restzeit: ",rest
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.1,1200))
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.1,1000))



while True:
	try:
		dauer_s=raw_input("Gesamtdauer: ")
		if dauer_s[:3]=="max":
			endif="max"
			dauer_s=dauer_s[3:]
		elif dauer_s[:3]=="min":
			endif="min"
			dauer_s=dauer_s[3:]
		else:
			endif="0"
		if dauer_s[-1]=="h":
			dauer=int(dauer_s[:-1])*3600
		elif dauer_s[-1]=="m":
			dauer=int(dauer_s[:-1])*60
		else:
			dauer=int(dauer_s)
	except ValueError:
		continue
	break
if dauer==0:
	sys.exit()	
while True:	
	try:
		IntervallGr_s=raw_input("Dauer des ersten Intervalles: ")
		komment1=raw_input("Kommentar: ")	
		if IntervallGr_s[-1]=="h":
			IntervallGr=int(IntervallGr_s[:-1])*3600
		elif IntervallGr_s[-1]=="m":
			IntervallGr=int(IntervallGr_s[:-1])*60
		else:
			IntervallGr=int(IntervallGr_s)
	except ValueError:
		continue
	break

while True:	
	try:
		IntervallKl_s=raw_input("Dauer des zweiten Intervalles: ")
		komment2=raw_input("Kommentar: ")	
		if IntervallKl_s[-1]=="h":
			IntervallKl=int(IntervallKl_s[:-1])*3600
		elif IntervallKl_s[-1]=="m":
			IntervallKl=int(IntervallKl_s[:-1])*60
		else:
			IntervallKl=int(IntervallKl_s)
	except ValueError:
		continue
	break
peep_ad(endif,IntervallGr,IntervallKl,komment1,komment2,dauer)
os._exit(0)

