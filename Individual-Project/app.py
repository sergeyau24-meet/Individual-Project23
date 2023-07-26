from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase
import pysurfline as surfAPI
import waves as w

Config = {
  "apiKey": "AIzaSyBpY6JY2UXe9E2eTMWfywHsmbsD-JES9Ps",
  "authDomain": "[indivproj-bdc2e.firebaseapp.com](https://www.google.com/search?q=indivproj-bdc2e.firebaseapp.com)",
  "projectId": "[indivproj-bdc2e](https://www.google.com/search?q=indivproj-bdc2e)",
  "storageBucket": "[indivproj-bdc2e.appspot.com](https://www.google.com/search?q=indivproj-bdc2e.appspot.com)",
  "messagingSenderId": "[27454404203](https://www.google.com/search?q=27454404203)",
  "appId": "[1:27454404203:web:f9196db12d407c96e9232e](https://www.google.com/search?q=1%3A27454404203%3Aweb%3Af9196db12d407c96e9232e)",
  "databaseURL": "https://indivproj-bdc2e-default-rtdb.europe-west1.firebasedatabase.app/"
}
fb = pyrebase.initialize_app(Config)
auth = fb.auth()
db = fb.database()


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


error = ''
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['Lemail']
        password = request.form['Lpassword']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home'))
        except:
            print('Auth login Failed')
    return render_template("login.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        # 
        login_session['user'] = auth.create_user_with_email_and_password(email, password)
        login_session['user']['name'] = username
        try:
            
            # print("vadim1")
            user = {'email': email, 'password' : password, 'username': username}
            UID = login_session['user']['localId']
            db.child('Users').child(UID).set(user)
            return redirect(url_for('home'))
        except:
            print('signup failed')

    return render_template("signup.html")

@app.route('/home', methods=['GET', 'POST'])
def home():
    uid = login_session['user']['localId']
    na = db.child('Users').child(uid).child('username').get().val()
    
    params = {
    "spotId": "584204204e65fad6a7709aad",
    "days": 5,
    "intervalHours": 3,
    }

    db1,catg = w.display(params)
    print(db1)
    



    return render_template("home.html", n  = na, r = db1, c = catg)
    
    





if __name__ == '__main__':
    app.run(debug=True)