import firebase_management.firebase_connect
from firebase_admin import auth

class authentication:
	def __init__(self):
		firebase_management.firebase_connect.get_admin()

	def create_user(self, email, username, displayname, password):
		user = auth.create_user(
		    email=email,
		    email_verified=False,
		    display_name=displayname,
		    password=password,
		    disabled=False,
		)
		uid = user.uid

		auth.set_custom_user_claims(uid, {'username': username})

		print(f"User created account with uid {uid}")

		return uid


