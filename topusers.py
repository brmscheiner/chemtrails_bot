import tweepy,names,random

def isUntagged(screen_name):
	with open('tagged.txt','r') as f:
		for line in f.readlines():
			if screen_name in line:
				return False
	return True

def updateTaggedList(screen_name):
	with open('tagged.txt','r+') as f:
		f.write(screen_name+'\n')

def getTopUser(api):
	'''Find a user with over 10k followers and return their tweepy user object.'''
	found=False
	while not found:
		random_name = names.get_full_name()
		print(random_name)
		matches = api.search_users(random_name)
		if matches == []:
			continue
		print(matches[0].screen_name)
		for user in matches[0].friends():
			print("   testing "+user.screen_name)
			if user.followers_count > 10000:
				if isUntagged(user.screen_name):
					found=True
	updateTaggedList(user.screen_name)
	return user.screen_name