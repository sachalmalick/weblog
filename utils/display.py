import sqlite3, os, itertools

##s='../data/story.db'
##f_s='../data/full_story.db'
##u='../data/users.db'

#==================================
#
#
#    Accessor Methods
#       getTitle(sid_input)
#       getFullText(sid_input)
#       getMostRecent(sid_input)
#       getNumberEdits(sid_input)
#       getTimeSince(sid_input)
#       getTimestamp(sid_input)
#
#
#==================================
    
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

def getMostRecent(sid_input):
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

def getTimestamp(sid_input):
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

#==========================================
#
#
#
#      Misc Methods
#
#
#
#===========================================

def getKey(item):
    return item[1]

def mostRecentStories():
#============ACCESSING THE DB========
    f="../data/weblog.db"
    db = sqlite3.connect(f)
    c=db.cursor()
#====================================
    
    finalList = []

    c.execute("SELECT story_id, timestamp FROM stori")
    list_ids = c.fetchall()

    listH = sorted(list_ids, key=getKey)

    for x in listH:
        if len(finalList)<11:
            finalList.append(x[0])
    
    db.commit()
    db.close()

    return finalList

#print(mostRecentStories())


def userStories(u_username):
#============ACCESSING THE DB========
    f="../data/weblog.db"
    db = sqlite3.connect(f)
    c=db.cursor()
#====================================
    
    finalList = []

    c.execute("SELECT story_id FROM useri WHERE username = ?", (u_username,))
    listI = list(itertools.chain.from_iterable(c))
#    listH = listI[1:len(listI)-2]

    db.commit()
    db.close()

    return listI

print(userStories("sammi"))
