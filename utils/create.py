import sqlite3, datetime, pickle

def adapt_tuple(tuple):
    return pickle.dumps(tuple)    

sqlite3.register_adapter(tuple, adapt_tuple)
sqlite3.register_converter("tuple", pickle.loads)

def collate_tuple(string1, string2):
    return cmp(pickle.loads(string1), pickle.loads(string2))

con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)

con.create_collation("cmptuple", collate_tuple)

cur = con.cursor()



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

    for entry in story_hold:
        if (story_id == entry):
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
    c.execute("UPDATE users SET story_ids = story_ids + ? WHERE username = ?", params2)
    db.commit()
    db.close()

def update_story(g_username, u_id,  u_recent, u_timestamp):
    #===============OPENING THE DB=========
    f = "../data/weblog.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    #=====================================

    params1 = (u_recent, u_id)
    params2 = (u_recent, u_timestamp, u_id)
    params3 = (u_id, g_username)
    
    story_hold = c.execute("SELECT number_edits FROM story;")
    user_hold = c.execute("SELECT story_ids FROM users;")

    
    c.execute("UPDATE story SET most_recent = ?, number_edits += 1, time_since = 0, timestamp = ? WHERE story_id = ?;")
    #c.execute("UPDATE story SET most_recent = ?, number_edits += 1, time_since = 0, timestamp = ? WHERE story_id = ?;", params2)
    c.execute("UDPATE full_story SET full_text = full_text + ? WHERE story_id = ?;", params1)
    c.execute("UPDATE users SET story_ids = story_ids + ? WHERE username = ?;", params3)
    db.commit()
    db.close()

def delete(u_id):
    #===============OPENING THE DB=========
    f = "../data/weblog.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    #=====================================

create_story("sammi", 521, "title", "recentstuff", 4, 55,55);
create_story("user", 422, "sharon story", "sharon went to the park", 4, 55,55);
print (check_story("test", 11))
