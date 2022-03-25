import web  
import app
import pyrebase
import firebase_config as token 
import json


class Sensores:
   def GET (self):
        firebase= pyrebase.initialize_app(token.firebaseConfig)
        
        ba =firebase.database()
        sensores = ba.child("sensores").get()
        result = json.dumps(sensores.val()) 
        return result
