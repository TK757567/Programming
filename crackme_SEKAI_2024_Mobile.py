import pyrebase
import requests

# Firebase configuration
config = {
  "apiKey": "AIzaSyCR2Al5_9U5j6UOhqu0HCDS0jhpYfa2Wgk",
  "authDomain": "crackme-1b52a.firebaseapp.com",
  "databaseURL": "https://crackme-1b52a-default-rtdb.firebaseio.com",
  "storageBucket": "crackme-1b52a.appspot.com",
  "projectId": "crackme-1b52a"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(config)

# Authenticate with email and password
auth = firebase.auth()
email = "admin@sekai.team"
password = "s3cr3t_SEKAI_P@ss"
user = auth.sign_in_with_email_and_password(email, password)

# Retrieve the UID
uid = user['localId']
print("UID:", uid)

print(config["databaseURL"])

firebase_database = requests.get(f"{config['databaseURL']}/users/{uid}/flag.json?auth={user['idToken']}")

print(firebase_database.content)
