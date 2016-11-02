#Always in School Squad: Felix Rieg-Baumhauer, Asher Lasday, Sahron Lin, Sachal Malick
#Softdev pd8
#HW10 -- Da ARt of Storytellin'
#2016-11-01


#import the fxns--from utils
import utils.auth, hashlib, os
from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)

app.secret_key = os.urandom(32)
secret = 'secret_cookie_key'

#========================================ROUTAGE

@app.route("/")
def index():
    if (secret in session):
        return render_template('index.html')
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

@app.route("/logout")
def log_em_out():
    print session
    session.pop(secret)
    return redirect(url_for("index")) #redirect(url_for("log_em_in"))


@app.route("/make_account")
def make_dat_account():
    return render_template('auth.html', action_type="mk_act")


@app.route("/create_account", methods = ['POST'])
def create_dat_account():
    wanted_user = request.form["username"]
    wanted_pass = request.form["password"]

    hashPassObj2 = hashlib.sha1()
    hashPassObj2.update(wanted_pass)
    hashed_pass = hashPassObj2.hexdigest()

    is_user_now = utils.auth.make_account(wanted_user, hashed_pass)

    if(is_user_now == True):
        #return redirect(url_for("log_em_in"))
        return redirect(url_for("index")) #redirect(url_for("log_em_in"))
    #else
    return render_template('auth.html', action_type='mk_act')
    
#======================================END__OF__ROUTAGE


if __name__ == "__main__":
    app.debug = True
    app.run() 




