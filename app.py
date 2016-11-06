#Always in School Squad: Felix Rieg-Baumhauer, Asher Lasday, Sahron Lin, Sachal Malick
#Softdev pd8
#HW10 -- Da ARt of Storytellin'
#2016-11-01


#import the fxns--from utils
import utils.auth, utils.display, utils.create, hashlib, os
from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)

app.secret_key = os.urandom(32)
secret = 'secret_cookie_key'

n_in_feed=20#THIS IS THE NUMBER OF STORIES IN FEED THAT WE DISPLAY(n-1)are displayed

#========================================ROUTAGE

@app.route("/")
def index():
    if (secret in session):
        name = session[secret]
        list_ur_stories=utils.display.userStories(name)
        print "bump"
        print (list_ur_stories)
        list_of_titles=[]
        list_of_stories=[]
        dict_article={}
        
        article = []
        for num in list_ur_stories:
            title1 = utils.display.getTitle(num)
            full_text = utils.display.getFullText(num)
            hold = []
            hold.append(title1)
            hold.append(full_text)
            article.append(hold)
            dict_article[num]=hold
            #list_of_titles.append(title1)
            #list_of_stories.append(full_text)
        print list_of_titles
        print dict_article
        return render_template('index.html', article=dict_article)#article=article, list_stories=list_ur_stories)#list_of_title)
    #redirect(url_for("log_em_in"))
    return render_template('auth.html', action_type='login')


#@app.route("/login")
#def log_em_in():
#    return render_template('auth.html', action_type='login')

@app.route("/login", methods=["POST"])
def log_em_in():
    given_user = request.form["username"]
    given_pass = request.form["password"]

    hashPassObj = hashlib.sha1()
    hashPassObj.update(given_pass)
    hashed_pass = hashPassObj.hexdigest()

    are_u_in = utils.auth.login(given_user, hashed_pass)

    if(are_u_in == True):
        session[secret]=given_user
        return redirect(url_for('index'))#return render_template('index.html')
    #else:
    #return redirect(url_for("log_em_in"))
    return render_template('auth.html', action_type='login')
    #return redirect(url_for("log_em_in"))
    
@app.route("/logout")
def log_em_out():
    print session
    session.pop(secret)
    return redirect(url_for("index")) #redirect(url_for("log_em_in"))

@app.route("/show_make_story")
def make_us_one():
    return render_template("feed.html", action="make")

@app.route("/make_story", methods=['POST'])
def lets_make():
    name = session[secret]
    title = request.form['title']
    text = request.form['text']
    
#THIS SHOULD BE A LIST OF ALL STORIES THAT USER HAS NOT TOUCHED
    list_of_nums = utils.display.mostRecentStories(n_in_feed)#list of 10 recent ones
    num = max(list_of_nums)
    num+=1

    ###$$TIMESTAMP MUST BE DONE HERE
    
    utils.create.create_story(name,num,title,text,1,0,100)
    return redirect(url_for("index"))

#similar mechanic to "/"
@app.route("/feed")
def feed_em_new_ones():
    if (secret in session):
        name = session[secret]

        list_other_stories=[]
        list_other_stories=utils.display.mostRecentStories(n_in_feed)####

        list_of_titles=[]
        list_of_stories=[]
        article = []
        dict_article={}
        for num in list_other_stories:
            title = utils.display.getTitle(num)
            most_recent = utils.display.getMostRecent(num)
            hold = []
            hold.append(title)
            hold.append(most_recent)
            article.append(hold)
            dict_article[num]=hold
        return render_template('feed.html', article=dict_article, action = "edit")
        
        #title1 = utils.display.getTitle(0)
        #return render_template("feed.html", article_title=title1)
    return redirect(url_for("index"))

#to return from feed to / or index
@app.route("/return_home")
def return_to_home():
    return redirect(url_for("index")) 


@app.route("/make_account")
def make_dat_account():
    return render_template('auth.html', action_type="mk_act")


@app.route("/create_account", methods = ['POST'])
def create_dat_account():
    wanted_user = request.form["username"]
    email = request.form["email"]
    wanted_pass1 = request.form["password1"]
    wanted_pass2 = request.form["password2"]

    hashPassObj1 = hashlib.sha1()
    hashPassObj1.update(wanted_pass1)
    hashed_pass1 = hashPassObj1.hexdigest()

    hashPassObj2 = hashlib.sha1()
    hashPassObj2.update(wanted_pass2)
    hashed_pass2 = hashPassObj2.hexdigest()

    is_user_now = utils.auth.make_account(wanted_user, hashed_pass1, hashed_pass2, email)

    if(is_user_now == True):
        #return redirect(url_for("log_em_in"))
        return redirect(url_for("index")) #redirect(url_for("log_em_in"))
    #else
    return render_template('auth.html', action_type='mk_act')

@app.route("/edit", methods = ['POST'])
def edit_dat_post():
    edit=request.form["edit"]
    num=request.form["id"]
    print num
    time_s=utils.display.getTimestamp(num)
    utils.create.update_story(session[secret],num,edit,time_s)
    return redirect(url_for("index"))


#======================================END__OF__ROUTAGE


if __name__ == "__main__":
    app.debug = True
    app.run() 




