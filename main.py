import firebase_management.firebase_manager

user_auth = firebase_management.firebase_manager.authentication()

user_auth.create_user("test@test.net", "test1", "test", "fafds123!")
