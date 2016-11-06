import sqlite3, os, itertools

f = "data/weblog.db"

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
    #f="data/weblog.db"  
    db = sqlite3.connect(f)
    c = db.cursor()
#====================================

    c.execute("SELECT story_title FROM full_story WHERE story_id = ?", (sid_input,))
    sTitle = c.fetchall()
    #listH = list(itertools.chain.from_iterable(c))
    #print(sTitle)
    
    db.commit()
    db.close()

    #return listH[0]
    for x in sTitle:
       for y in x:
            de_title=y
            return (de_title)

#print(getTitle(24))


def getFullText(sid_input):
#============ACCESSING THE DB========
    #f="data/weblog.db"
    db = sqlite3.connect(f)
    c=db.cursor()
#====================================

    c.execute("SELECT full_text FROM full_story WHERE story_id = ?",(sid_input,))

    #listH = list(itertools.chain.from_iterable(c))   
    #return listH[0]

    sTitle = c.fetchall()
    
    db.commit()
    db.close()

    for x in sTitle:
       for y in x:
            de_title=y
            return (de_title)

def getMostRecent(sid_input):
#============ACCESSING THE DB========
    #f="data/weblog.db"
    db = sqlite3.connect(f)
    c=db.cursor()
#====================================

    c.execute("SELECT most_recent FROM story WHERE story_id = ?",(sid_input,))

    #listH = list(itertools.chain.from_iterable(c))
    #return listH[0]
    sTitle = c.fetchall()
    
    db.commit()
    db.close()

    for x in sTitle:
       for y in x:
            de_title=y
            return (de_title)
        

def getNumberEdits(sid_input):
#============ACCESSING THE DB========
    #f="data/weblog.db"
    db = sqlite3.connect(f)
    c=db.cursor()
#====================================

    c.execute("SELECT number_edits FROM story WHERE story_id = ?",(sid_input,))

    #listH = list(itertools.chain.from_iterable(c))
    sTitle = c.fetchall()
    
    db.commit()
    db.close()

    #return listH[0]
    for x in sTitle:
       for y in x:
            de_title=y
            return (de_title)


def getTimeSince(sid_input):
#============ACCESSING THE DB========
    #f="data/weblog.db"
    db = sqlite3.connect(f)
    c=db.cursor()
#====================================

    c.execute("SELECT time_since FROM story WHERE story_id = ?",(sid_input,))

    #listH = list(itertools.chain.from_iterable(c))
    #return listH[0]

    sTitle = c.fetchall()
    db.commit()
    db.close()

    for x in sTitle:
       for y in x:
            de_title=y
            return (de_title)
        

def getTimestamp(sid_input):
#============ACCESSING THE DB========
    #f="data/weblog.db"
    db = sqlite3.connect(f)
    c=db.cursor()
#====================================

    c.execute("SELECT timestamp FROM story WHERE story_id = ?",(sid_input,))

    #listH = list(itertools.chain.from_iterable(c))
    #return listH[0]

    sTitle = c.fetchall()
    #listH = list(itertools.chain.from_iterable(c))
    #print(sTitle)
    
    db.commit()
    db.close()

    for x in sTitle:
       for y in x:
            de_title=y
            return (de_title)

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

def mostRecentStories(num):
#============ACCESSING THE DB========
    #f="data/weblog.db"
    db = sqlite3.connect(f)
    c=db.cursor()
#====================================
    
    finalList = []

    c.execute("SELECT story_id, timestamp FROM story")
    list_ids = c.fetchall()

    listH = sorted(list_ids, key=getKey)

    for x in listH:
        if len(finalList)<num:
            finalList.append(x[0])
    
    db.commit()
    db.close()

    return finalList
print("eho")
print(mostRecentStories())

def getStories():
#============ACCESSING THE DB========
    #f="data/weblog.db"
    db = sqlite3.connect(f)
    c=db.cursor()
#====================================
    
    finalList = []

    c.execute("SELECT story_id, timestamp FROM story")
    list_ids = c.fetchall()

    listH = sorted(list_ids, key=getKey)

    finalLen = len(listH)

    for x in listH:
        if len(finalList)<finalLen:
            finalList.append(x[0])
    
    db.commit()
    db.close()

    return finalList
print("eho")
print(mostRecentStories())


def userStories(u_username):
#============ACCESSING THE DB========
    #f="../data/weblog.db"
    db = sqlite3.connect(f)
    c=db.cursor()
#====================================
    
    finalList = []

    c.execute("SELECT story_ids FROM users WHERE username = ?", (u_username,))
    #listI = list(itertools.chain.from_iterable(c))
    
    listI = c.fetchall()
    
    for list in listI:
        for item in list:
            print item
            item = str (item)
            holdList = item.split(",")
            for pieces in holdList:
                if(pieces != ""):
                    finalList.append(pieces)
    #listH = listI[1:len(listI)-2]
    
    db.commit()
    db.close()
    return finalList
    #return listI

print(userStories("sammi"))
