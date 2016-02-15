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

def getTopUser(api,n):
	'''Find a user with over n followers and return their tweepy user object.'''
	found=False
	while not found:
		random_name = names.get_full_name()
		print(random_name)
		matches = api.search_users(random_name)
		if matches == []:
			continue
		for user in matches[0].friends():
			print("   testing "+user.screen_name)
			if user.followers_count > n:
				if isUntagged(user.screen_name):
					found=True
					break
	updateTaggedList(user.screen_name)
	return user.screen_name