import sqlite3
import os

##s='../data/story.db'
##f_s='../data/full_story.db'
##u='../data/users.db'

    
def getTitle(sid_input):
#============ACCESSING THE DB========
    f="../data/weblog.db"  
    db = sqlite3.connect(f)
    c = db.cursor()
#====================================

    c.execute("SELECT story_title FROM full_story WHERE story_id = ?", (sid_input,))
    sTitle = c.fetchall()

    print(sTitle)
    
    db.commit()
    db.close()
    for x in sTitle:
        for y in x:
            de_title=y
    return (de_title)


def getFullText(sid_input):
#============ACCESSING THE DB========
    f="../data/weblog.db"
    db = sqlite3.connect(f)
    c=db.cursor()
#====================================

    c.execute("SELECT full_text FROM full_story WHERE story_id =" + str(sid_input) + ";")
    sFText c.fetchall()

    print (sFText)
    
    db.commit()
    db.close()
    for x in sFText:
        for y in x:
            de_fText=y
    return (de_fText)


def getuser(sid_input):
#============ACCESSING THE DB========
    f="../data/weblog.db"
    db = sqlite3.connect(f)
    c=db.cursor()
#===================================

    c.execute("SELECT full_text FROM full_story WHERE story_id =" + str(sid_input) + ";")
    sFText c.fetchall()

    print (sFText)
    
    db.commit()
    db.close()
    for x in sFText:
        for y in x:
            de_fText=y
    return (de_fText)

def getEmail(sid_input):
#============ACCESSING THE DB========
    f="../data/weblog.db"
    db = sqlite3.connect(f)
    c=db.cursor()
#===================================

    c.execute("SELECT full_text FROM full_story WHERE story_id =" + str(sid_input) + ";")
    sFText c.fetchall()

    print (sFText)
    
    db.commit()
    db.close()
    for x in sFText:
        for y in x:
            de_fText=y
    return (de_fText)

def getRecentAdd(sid_input):
#============ACCESSING THE DB========
    f="../data/weblog.db"
    db = sqlite3.connect(f)
    c=db.cursor()
#====================================

    c.execute("SELECT full_text FROM full_story WHERE story_id =" + str(sid_input) + ";")
    sFText c.fetchall()

    print (sFText)
    
    db.commit()
    db.close()
    for x in sFText:
        for y in x:
            de_fText=y
    return (de_fText)


