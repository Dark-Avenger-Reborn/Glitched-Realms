import firebase_management.firebase_connect
from firebase_admin import auth

class authentication:
	def __init__(self):
		firebase_management.firebase_connect.get_admin()

	def create_user(self, email, username, displayname, password):
		user = auth.create_user(
		    email=email,
		    email_verified=False,
		    display_name='John Doe',
		    password=password,
		    disabled=False,
		)

		auth.set_custom_user_claims(user.uid, {'username': username})

		print(f"User created account with uid {user.uid}")

		return user.uid


