import requests, os, wget
import config

print "Instagram Stories DATA Dumper\nRagul Balaji 2017\n\n"

r = requests.get("https://i.instagram.com/api/v1/feed/reels_tray/", cookies=config.mycookies, headers=config.myheaders).json()

for u in r['tray']:
	label = u['user']['full_name'] + " - " + u['user']['username'] + " " + str(u['id'])

	print "[*] Grabbing " + u['user']['full_name'] + "'s Story\n"

	if not os.path.exists("./data/" + label):
		os.makedirs("./data/" + label)

	r2 = requests.get("https://i.instagram.com/api/v1/feed/user/"+str(u['id'])+"/reel_media/", cookies=config.mycookies, 
headers=config.myheaders).json()

	wget.download(r2['user']['profile_pic_url'], "./data/" + label + "/profilepic.jpg")

	for m in r2['items']:
		if 'video_versions' in m:
			#print m['video_versions'][0]['url']
			wget.download(m['video_versions'][0]['url'], "./data/" + label + "/")
		else:
			#print m['image_versions2']['candidates'][0]['url']
			wget.download(m['image_versions2']['candidates'][0]['url'], "./data/" + label + "/")
