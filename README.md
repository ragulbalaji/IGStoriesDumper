# IGStoriesDumper
## Bulk downloads your friends Instagram Stories; Instagram can you fix this!

Alec Garcia (@CaliAlec) reverse engineered the way the iOS instagram client interacts to serve up IG Stories. It seems to be very open and strangely Instagram NEVER DELETES UR CONTENT OFF THEIR SERVERS even after 24hours or you purposely delete them.

Apprently the permalinks that IG gives you lasts forever, so they arent really deleting ur data, just hiding it from you!!!

I think everyone should be well informed about this before making a decision to use their services.


## Using the code

1. `git clone <this.git>`
2. Using an extension like `EditThisCookie` on Chrome to fetch :
	- `ds_user_id`
	- `sessionid`
	- `csrftoken`
	Then put these in `config.py` under the appropiate key-value pairs

### Download stories
3. Run `python storydump.py` and watch as data gets dumped into `data/`

### Make a HTML stories dashboard of links
3. Run `python loglinks.py` and a HTML pages will be created in `links/`
4.  DO NOT DELETE `main.css` unless u want the formatting to look (more) fugly


## Referances
- https://medium.com/@calialec/chrome-ig-story-bribing-the-instagram-story-api-with-cookies-c813e6dff911
- https://github.com/CaliAlec/ChromeIGStory