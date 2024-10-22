import firebase_admin

def get_admin():
	cred = firebase_admin.credentials.Certificate("./serviceAccountKey.json")
	firebase_admin.initialize_app(cred)
