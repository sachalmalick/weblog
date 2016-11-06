import hashlib, sqlite3

#faciliates logins
def login(g_username, g_password):
    #===========OPENING THE DB=============
    f="data/weblog.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    #=================================================
    
    c.execute("SELECT password FROM users WHERE username="+"'"+g_username+"'"+";")
    pass_hold = c.fetchall()

    #the for loops only fire if there is something in pass_hold,
    #thus, if there is no account for that user, then pass_hold is empty
    #and as a result the for never fires and False is retuned
    #False is also returned if the password doesn't match the one in the db

    #=================CLOSE DB
    db.commit()
    db.close()
    #==============================
    
    for line in pass_hold:
        for entry in line:
            if(g_password == entry):
                #session[secret]=g_username
                return True
    return False


def make_account(g_username, g_password1, g_password2, email):

    #if(g_username or g_password1 or g_password2 or email == ""):
        #return False
    
    if(g_password1 != g_password2):
        return False
    
    #===========OPENING THE DB=============
    f="data/weblog.db"
    db = sqlite3.connect(f);
    c = db.cursor()
    #=================================================
    c.execute("SELECT username FROM users WHERE username="+"'"+g_username+"'"+";")
    hold = c.fetchall()

    #=============CLOSE DB
    db.commit()
    db.close()
    #=========================
    
    #the for loop only fires if there is something in hold, meaning double users
    for x in hold:
        return False

    #==============OPEN DB
    f="data/weblog.db"
    db = sqlite3.connect(f);
    c = db.cursor()
    #===============
    
    c.execute('INSERT INTO users VALUES("",'+'"'+g_username+'"'+','+'"'+g_password1+'"'+','+'"'+email+'"'+', "");')

    #===============CLOSE
    db.commit()
    db.close()
    #======================

    return True
    

















####################LOKED USEFL
#def getUsers():
 #   f = open("data/users.csv","r")
 #   #fText = f.read()
 #   array = f.readlines()#split("\n")
 #   users = {}
 #   print array
 #   for item in range(len(array)):
 #       array[item] = array[item].strip("\n").split(",")
 #       users[array[item][0]] = array[item][1]
 #   f.close()
 #   return users
#
#def addUser(user,pword):
#    f = open("data/users.csv","a")
#    f.write(str(user)+","+str(pword)+"\n")
#    f.close()
#    return str(user)+", "+str(pword)+"\n"
