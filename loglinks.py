import requests, os, time
import config

print "Instagram Stories Link Logger\nRagul Balaji 2017\n\n"

r = requests.get("https://i.instagram.com/api/v1/feed/reels_tray/", cookies=config.mycookies, headers=config.myheaders).json()

for u in r['tray']:
	label = u['user']['full_name'] + " - " + u['user']['username'] + " " + str(u['id'])

	print "[*] Grabbing " + u['user']['full_name'] + "'s Story"

	filename = "./links/" + label + '.html'

	append_write = 'w' # make a new file by default

	if os.path.exists(filename):
		append_write = 'a' # append if already exists
	
	userfile = open(filename, append_write)

	r2 = requests.get("https://i.instagram.com/api/v1/feed/user/"+str(u['id'])+"/reel_media/", cookies=config.mycookies, headers=config.myheaders).json()

	if append_write == 'w':
		userfile.write("<link rel='stylesheet' href='main.css'>")
		userfile.write("<h1>" + label.encode('utf-8') + "</h1><br>")
		userfile.write("Profile Pic: <img src='" + r2['user']['profile_pic_url'] + "'><br>")

	userfile.write("<h3>" + time.strftime("%d-%m-%Y %H:%M") + "</h3><br>")
	for m in r2['items']:
		if 'video_versions' in m:
			userfile.write("<video src='" +  m['video_versions'][0]['url'] + "' autoplay loop controls poster='" + m['image_versions2']['candidates'][0]['url'] + "'></video>")
		else:
			userfile.write("<img src='" +  m['image_versions2']['candidates'][0]['url'] + "'>")

	userfile.write("<br>")
	userfile.close()