import sqlite3

def check_story(g_username, story_id):
    #===============OPENING THE DB=========
    f = "../data/weblog.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    #=====================================

    c.execute("SELECT story_ids FROM users where username="+"'"+g_username+"'"+";")
    story_hold = c.fetchall()

    db.commit()
    db.close()

    for line in story_hold:
        for entry in line:
            if (g_username == entry):
                return False
    return True



def create_story(g_username, u_id, u_title, u_recent, u_editors, u_timesince, u_timestamp):
    #===============OPENING THE DB=========
    f = "../data/weblog.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    #=====================================

    params = (u_id, u_title, u_recent, u_editors, u_timesince, u_timestamp)
    params1 = (u_id, u_title, u_recent)
    params2 = (u_id, g_username)

    c.execute("INSERT INTO story (story_id, story_title, most_recent, number_edits, time_Since, timestamp) VALUES (?,?,?, ?, ?, ?)", params)
    c.execute("INSERT INTO full_story (story_id, story_title, full_text) VALUES (?,?,?)", params1)
    c.execute("INSERT INTO full_story (story_id, story_title, full_text) VALUES (?,?,?)", params1)
    c.execute("UPDATE users SET story_ids = story_ids + ? WHERE username = ?", params2)
    db.commit()
    db.close()


#create_story("user", 121, "title", "recentstuff", 4, 55,55);
#create_story("user", 122, "sharon story", "sharon went to the park", 4, 55,55);
