import sqlite3
import os

f='../data/weblog.db' 

##s='../data/story.db'
##f_s='../data/full_story.db'
##u='../data/users.db'


db = sqlite3.connect(f)
c = db.cursor()

def getTitle(sid_input):
    c.execute("SELECT story_title FROM + full_story + WHERE story_id =(" + sid_input + ")")
    sTitle = c.fetchall()
    return (sTitle)

   
