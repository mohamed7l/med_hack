import requests,json,hashlib
import os
W="\033[0m"
R="\033[91m"
G="\033[92m"
Y="\033[93m"
B="\033[94m"
RS="\033[95m"
#################
def main():
	print R+" created: "+G+"by lassoued /"+R+ "email:" +G+"mlassoued97@gmail.com"
	print B+" _____               ___  ___    ___   ___"
	print "||----  || "+R+"v 1.0"+B+"    //==  ||\\\\  //||  ||=="
	print "||____  ||         ||     || \\\\// ||  ||  \\\\"
	print "||----  ||         ||	  ||      ||  ||   ||"
	print "||      ||=\\\\      ||     ||      ||  ||   ||"
	print "||      ||   || == ||     ||      ||  ||  //"
	print "||      ||=//       \\\\==  ||      ||  ||=="+W
	print "     												"
#################
def id():
	id=raw_input(W+"Email or Phone: "+R)
	pwd=raw_input(W+"Password: "+R)
	API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'
	sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
	data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
	x=hashlib.new("md5")
	x.update(sig)
	a=x.hexdigest()
	data.update({'sig':a})
	return data
#########################
def get_token():
	data=id()
	url = "https://api.facebook.com/restserver.php"
	try:
		r=requests.get(url,params=data)
		z=json.loads(r.text)
		cookie=open('cookie','w')
		cookie.write(z['access_token'])
		cookie.close()
		print G+'successful'+W
		menu2()
	except KeyError:
		os.remove("cookie")
		print R+'failed!!'+W
		menu1()
###################
def cookie():
	    global token
	    try:
	    	cookie=open("cookie","r")
	    	token=cookie.read()
	    	cookie.close()
	    	menu2()
	    except:
	    	menu1()
###########################
def menu1():
	print RS+"[1] "+Y+"login facebook"
	print RS+"[2] "+Y+"exit"
	chose1=raw_input(W+"=>: "+R)
	if chose1=="1":
		get_token()
	elif chose1=="2":
		print W+""
		exit()
	else:
		print R+"out of menu:"+W
		menu1()
#################	
def menu2():
	print RS+"[1] "+Y+"dump friends name&id   "+RS+"[7] "+Y+"edit post"
	print RS+"[2] "+Y+"dump friends emails    "+RS+"[8] "+Y+"delete post"
	print RS+"[3] "+Y+"dump friends phones    "+RS+"[9] "+Y+"comment"
	print RS+"[4] "+Y+"dump friends birthdays "+RS+"[10] "+Y+"logout and exit"
	print RS+"[5] "+Y+"id information         "+RS+"[11] "+Y+"exit"
	print RS+"[6] "+Y+"post"+W


	chose2=raw_input("chose one:"+R)
	if chose2== "1":
		print B+"wait......."+W
		dump_friends()
	elif chose2=="2":
		print B+"wait......."+W
		dump_emails()
	elif chose2=="3":
		print B+"wait......."+W
		dump_phones()
	elif chose2=="4":
		print B+"wait......."+W
		dump_dates()
	elif chose2=="5":
			id=raw_input(W+"inter target id:"+R)
			print B+"wait......."+W
			id_information(id)
	elif chose2=="6":
			post_id=raw_input(W+"inter target id:"+R)
			msg=raw_input(W+"inter the message: "+R)
			print B+"wait......."+W
			post(post_id,msg)
			print G+"successful posting"+W
	elif chose2=="7":
		post_id=raw_input(W+"inter post id:"+R)
		msg=raw_input(W+"inter the message: "+R)
		print B+"wait......."+W
		edit_post(post_id,msg)
		print G+"successful post edit"+W

	elif chose2=="8":
		post_id=raw_input(W+"inter post id:"+R)
		print B+"wait......."+W
		delete_post(post_id)
		print G+"successful post delete"+W

	elif chose2=="9":
		post_id=raw_input(W+"inter post id:"+R)
		msg=raw_input(W+"inter the message: "+R)
		print B+"wait......."+W
		comment(post_id,msg)
		print G+"successful comment"+W

	elif chose2=="10":
		print " "+W
		os.remove("cookie")

	elif chose2=="11":
		print ''+W
	else:
		print "out of menu:"
		menu2()		
######################
def menu3():
	print RS+"[1] "+Y+"go pack"
	print RS+"[2] "+Y+"logout and exit"
	print RS+"[3] "+Y+"exit"
	chose3=raw_input(W+"=>: "+R)
	if chose3=="1":
		menu2()
	elif chose3=="2":
		os.remove("cookie")
		exit()
	elif chose3=="3":
		exit()
	else:
		print R+"out of menu:"+W
		menu3()
##########################		
def dump_friends():
	global token

	url= "https://graph.facebook.com/me/friends"
	r=requests.get(url+"?access_token="+token)
	z=json.loads(r.text)
	for i in z["data"]:
		try:
			print W+i["name"]+" : "+G+i["id"]+W
		except:
			pass
	menu3()
          
####################
def dump_emails():
	global token
	url= "https://graph.facebook.com/"
	r= requests.get(url+"me/friends?access_token="+token)
	z=json.loads(r.text)
	for i in z["data"]:
		try:
			l = requests.get(url+i["id"]+"?access_token="+token)
			email=json.loads(l.text)
			print W+i["name"]+" : "+G+email["email"]+W
		except:
			pass
	menu3()
#####################
def dump_phones():
	global token
	url= "https://graph.facebook.com/"
	r =requests.get(url+"me/friends?access_token="+token)
	z=json.loads(r.text)
	for i in z["data"]:
		try:
			l = requests.get(url+i["id"]+"?access_token="+token)
			phone=json.loads(l.text)
			print W+i["name"]+" : "+G+phone["mobile_phone"]+W
		except:
			pass
	menu3()
######################
def dump_dates():
	global token
	url= "https://graph.facebook.com/"
	r=requests.get(url+"me/friends?access_token="+token)
	z=json.loads(r.text)
	for i in z["data"]:
		try:
			l = requests.get(url+i["id"]+"?access_token="+token)
			email=json.loads(l.text)
			print W+i["name"]+" : "+G+email["birthday"]+W
		except:
			pass
	menu3()
######################
def id_information(id):
	global token

	url= "https://graph.facebook.com/"+id
	r= requests.get(url+"?access_token="+token)
	z=json.loads(r.text)
	try:
			print W+"Name : "+G+z["name"]+W
	except: print W+"Name : "+G+"not found"
	try:
			print W+"Email : "+G+z["email"]+W
	except: print W+"Email : "+G+"not found"
	try:
			print W+"Phpne : "+G+z["mobile_phone"]+W
	except: print W+"Phone : "+G+"not found"
	try:
			print W+"Birthday : "+G+z["birthday"]+W
	except: print W+"Birthday : "+G+"not found"
	menu3()
#######################
def post(post_id,msg):
	global token
	url="https://graph.facebook.com/"+post_id+"/feed"
	data= {"access_token":token,"message":msg,"privacy":{"value":"SELF"}}
	r=requests.post(url,json=data)
	menu3()
##############
def edit_post(post_id,msg):
	global token
	url="https://graph.facebook.com/"+post_id
	data= {"access_token":token,"message":msg,"privacy":{"value":"SELF"}}
	r=requests.post(url,json=data)
	menu3()
#######################
def delete_post(post_id):
	global token
	url="https://graph.facebook.com/"+post_id
	data= {"access_token":token,"method":"delete"}
	r=requests.post(url,json=data)
	menu3()
#######################
def comment(post_id,msg):
	global token
	url="https://graph.facebook.com/"+post_id+"/comments"
	data= {"access_token":token,"message":msg}
	r=requests.post(url,json=data)
	menu3()	
######################
if __name__ ==	'__main__':
	main()
	cookie()