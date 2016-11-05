import sqlite3, os, itertools

##s='../data/story.db'
##f_s='../data/full_story.db'
##u='../data/users.db'

    
def getTitle(sid_input):
#============ACCESSING THE DB========
    f="../data/weblog.db"  
    db = sqlite3.connect(f)
    c = db.cursor()
#====================================

    c.execute("SELECT story_title FROM full_stori WHERE story_id = ?", (sid_input,))
#    sTitle = c.fetchall()
    listH = list(itertools.chain.from_iterable(c))

#    print(sTitle)
    
    db.commit()
    db.close()

    return listH[0]
 #   for x in sTitle:
 #      for y in x:
 #           de_title=y
 #   return (de_title)

#print(getTitle(24))


def getFullText(sid_input):
#============ACCESSING THE DB========
    f="../data/weblog.db"
    db = sqlite3.connect(f)
    c=db.cursor()
#====================================

    c.execute("SELECT full_text FROM full_stori WHERE story_id = ?",(sid_input,))

    listH = list(itertools.chain.from_iterable(c))
    
    db.commit()
    db.close()

    return listH[0]

def getRecentText(sid_input):
#============ACCESSING THE DB========
    f="../data/weblog.db"
    db = sqlite3.connect(f)
    c=db.cursor()
#====================================

    c.execute("SELECT most_recent FROM stori WHERE story_id = ?",(sid_input,))

    listH = list(itertools.chain.from_iterable(c))
    
    db.commit()
    db.close()

    return listH[0]

def getNumberEdits(sid_input):
#============ACCESSING THE DB========
    f="../data/weblog.db"
    db = sqlite3.connect(f)
    c=db.cursor()
#====================================

    c.execute("SELECT number_edits FROM stori WHERE story_id = ?",(sid_input,))

    listH = list(itertools.chain.from_iterable(c))
    
    db.commit()
    db.close()

    return listH[0]

def getTimeSince(sid_input):
#============ACCESSING THE DB========
    f="../data/weblog.db"
    db = sqlite3.connect(f)
    c=db.cursor()
#====================================

    c.execute("SELECT time_since FROM stori WHERE story_id = ?",(sid_input,))

    listH = list(itertools.chain.from_iterable(c))
    
    db.commit()
    db.close()

    return listH[0]

def getTimeStamp(sid_input):
#============ACCESSING THE DB========
    f="../data/weblog.db"
    db = sqlite3.connect(f)
    c=db.cursor()
#====================================

    c.execute("SELECT timestamp FROM stori WHERE story_id = ?",(sid_input,))

    listH = list(itertools.chain.from_iterable(c))
    
    db.commit()
    db.close()

    return listH[0]





  
