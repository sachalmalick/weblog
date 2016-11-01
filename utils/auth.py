def getUsers():
    f = open("data/users.csv","r")
    #fText = f.read()
    array = f.readlines()#split("\n")
    users = {}
    print array
    for item in range(len(array)):
        array[item] = array[item].strip("\n").split(",")
        users[array[item][0]] = array[item][1]
    f.close()
    return users

def addUser(user,pword):
    f = open("data/users.csv","a")
    f.write(str(user)+","+str(pword)+"\n")
    f.close()
    return str(user)+", "+str(pword)+"\n"
