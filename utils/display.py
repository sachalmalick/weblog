import sqlite3
import os



##s='../data/story.db'
##f_s='../data/full_story.db'
##u='../data/users.db'

    
def getTitle(sid_input):
    f="data/weblog.db"  
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute("SELECT story_title FROM full_story WHERE story_id =" + str(sid_input) + ";")
    sTitle = c.fetchall()

    print(sTitle)
    
    db.commit()
    db.close()
    for x in sTitle:
        for y in x:
            de_title=y
    return (de_title)
    
    #return (sTitle)


   
