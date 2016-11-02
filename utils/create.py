def check_story(g_username, story_id):
    #===============OPENING THE DB=========
    f = "data/weblog.db"
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


def create_story(g_username, ID, TITLE, RECENT, EDITRS, TIMESINCE, TIMESTAMP)):
    #===============OPENING THE DB=========
    f = "data/weblog.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    #=====================================

    c.execute("INSERT INTO story (story_id, story_title, most_recent, number_edits, time_since, timestamp) VALUES (ID, TITLE, RECENT, EDITRS, TIMESINCE, TIMESTAMP)")
    c.execute("INSERT INTO full_story (story_id, story_title, full_text) VALUES (ID, TITLE, full_text+RECENT)")
    db.commit()
    db.close()


