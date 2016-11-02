<<<<<<< HEAD
import sqlite3
import os

f='../data/weblog.db' 

os.remove(f)

db = sqlite3.connect(f)
c = db.cursor

def getTitle(int story_id){
        
=======
def display(story_id):
    
>>>>>>> effe7eae975846de61dc58f174e20dd69ef9c29f
