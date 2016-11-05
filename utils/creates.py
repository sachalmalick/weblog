from itertools import *
import sqlite3, datetime, itertools

#Create a completely new story

def create_story(u_username, u_title, u_recent):

#==============================================
    f = "../data/weblog.db"
    db = sqlite3.connect(f)
    c = db.cursor()
#==============================================

    params = (u_title, u_recent)

    c.execute("INSERT INTO stori (story_title, most_recent, number_edits, time_since) VALUES (?, ?, 1, 0)", params)
    c.execute("INSERT INTO full_stori (story_title, full_text) VALUES (?,?)", params)
    c.execute("SELECT story_id FROM stori WHERE story_title = ?", (u_title,))
    list_of_ids = list(itertools.chain.from_iterable(c))
    c.execute("UPDATE useri SET story_id = story_id || ? || ','  WHERE username= ?", (list_of_ids[0], u_username))
# Note: store timestamp as TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# Note: initiate users story_id with "," for this to work

    db.commit()
    db.close()

# Deletes an existing story

#create_story("sammi", "asdfasdf", "amany things")

def delete(u_title):
    #==============================================
    f = "../data/weblog.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    c.execute("DELETE from full_stori WHERE story_title = ?", u_title);
    c.execute("DELETE from stori WHERE story_title = ?", u_title);

# also need to delete this from the users string 

    db.commit()
    db.close()


# Adds to a story if its count of editors is < 15

def add_story(u_username, u_title, u_recent):
    #==============================================
    f = "../data/weblog.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    c.execute("SELECT number_edits FROM stori WHERE story_title = ?", (u_title,))
    list_of_edits = list(itertools.chain.from_iterable(c))

    if (list_of_edits[0]<16):
        c.execute("UPDATE stori SET most_recent = ?, number_edits = number_edits+1, time_since = 0, timestamp = CURRENT_TIMESTAMP WHERE story_title = ?", (u_recent, u_title))

        c.execute("UPDATE full_stori SET full_text = full_text||' '||? WHERE story_title = ?", (u_recent, u_title))

    db.commit()
    db.close()

# Checks if a user has edited yet

def check_story(u_username, u_id):
    #==============================================
    f = "../data/weblog.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    c.execute("SELECT story_id FROM useri WHERE username = ?", (u_username,))
    list_of_ids = list(itertools.chain.from_iterable(c))
    listH = list_of_ids[0].split(',')
    for x in listH:
        print(x)
        if x != '':
            if int(x) == int(u_id):
                db.commit()
                db.close()
                return True

    db.commit()
    db.close()
    return False 

#print(check_story("sammi", 18))
