<<<<<<< HEAD
import sqlite3
import os

f='../data/weblog.db' 

s='../data/story.db'
f_s='../data/full_story.db'
u='../data/users.db'


db = sqlite3.connect(f)
c = db.cursor()

def getTitle(int sid_input):
    c.execute("SELECT story_title FROM" + f_s + "WHERE story_id =(" + sid_input + ")")
    sTitle = c.fetchall()
    print (sTitle)

        
=======
def display(story_id):
