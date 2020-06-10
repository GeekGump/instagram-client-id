''' 
github.com/razyar
'''

import instagram_private_api as api 
import sys


try:
	instagram = api.Client('your_username', 'your_password')
	print 'Login sucessfully'
except Exception as LoginError:
	print 'Cannot login right now, check this error message and for solve go to https://github.com/razyar'
	sys.exit(0)


# i write some commands for you but you can use idle or read docks

'''
instagram.user_incoming_requests()
instagram.user_follows(user_id)*
instagram.user_followed_by(user_id)*
instagram.follow_user(user_id)
instagram.unfollow_user(user_id)
instagram.block_user(user_id)
instagram.unblock_user(user_id)
instagram.approve_user_request(user_id)
instagram.ignore_user_request(user_id)
instagram.user_relationship(user_id)
'''
#you can get more commands help from my github page.
