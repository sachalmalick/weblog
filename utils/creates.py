import sqlite3, datetime, uuid

#Create a completely new story

def create_story(u_username, u_title, u_recent):

#==============================================
    f = "../data/weblog.db"
    db = sqlite3.connect(f)
    c = db.cursor()
#==============================================

    curr_id = uuid.uuid1()

    params = (curr_id, u_title, u_recent)

    c.execute("INSERT INTO full_story (story_id, story_title, most_recent) VALUES (?, ?, ?)", params)
    c.execute("INSERT INTO story (story_id, story_title, most_recent, number_edits, time_since) VALUES (?,?,?,1,0)", params)
    c.execute("UPDATE users SET story_ids = story_ids || ',' || ? WHERE username= u_username", curr_id)
# Note: store timestamp as TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# UIUD replaces normal id as a "data type"    

    db.commit()
    db.close()

# Deletes an existing story

def delete(u_id):
    #==============================================
    f = "../data/weblog.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    c.execute("DELETE from full_story WHERE story_id = u_id");
    c.execute("DELETE from story WHERE story_id = u_id");

# also need to delete this from the users string 

    db.commit()
    db.close()


# Adds to a story if its count of editors is < 15

def add_story(u_username, u_id, u_recent):
    #==============================================
    f = "../data/weblog.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    if (c.execute("SELECT number_edits FROM story WHERE story_id = ?", u_id)<=15):
        c.execute("UPDATE story SET most_recent = ? WHERE story_id = ?", u_recent, u_id)
        c.execute("UPDATE story SET number_editors = number_editors+1 WHERE story_id = ?", u_id)
        c.execute("UPDATE story SET time_since = 0 WHERE story_id = ?", u_id)
# do i need to update timestamp from here???
        c.execute("UPDATE full_story SET full_text = full_text || ? WHERE story_id = ?", u_recent, u_uid)

    db.commit()
    db.close()

# Checks if a user has edited yet

def check_story(u_username, u_id):
    #==============================================
    f = "../data/weblog.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    storys = c.execute("SELECT story_ids FROM users WHERE user_id = ?", u_id)
    mylist = map(storys.split(',') )
    for x in mylist:
        if x == u_id:
            db.commit()
            db.close()
            return True

    db.commit()
    db.close()
    return False 

