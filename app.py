from flask import Flask,render_template,request,session,json,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

with open('configure.json','r') as c:
    params=json.load(c) ["params"]

app.secret_key="super-secret-key"

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/property"
# initialize the app with the extension
db= SQLAlchemy(app)



class Accounts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(20))
    password= db.Column(db.String(80))
    re_password= db.Column(db.String(80))
    date = db.Column(db.String(12))
    role = db.Column(db.String(20))    

@app.route('/')
def index():
    detai = Details.query.all()
    return render_template('index.html',detai=detai)

@app.route('/index2')
def index2():
    detai = Details.query.all()
    return render_template('index2.html',detai=detai)

@app.route('/logout')
def logout():
    session.clear
    return redirect(url_for("index"))

@app.route('/login',methods=["GET","POST"])
def login():
     if request.method == "POST":
        email = request.form["email"]
        password = request.form["passw"]
        # role=Accounts.query.filter_by(role='Tenant')
        # role1=Accounts.query.filter_by(role1='Landlord')

        login =  Accounts.query.filter_by(email=email, password=password).first()
        if login is not None:
           return redirect(url_for("landlord"))
        
        # notlogin =  Accounts.query.filter_by(name=name, password=password,role=role).first()
        # if notlogin is not None:
        #     return render_template('tenant.html')
     return render_template('login.html')

@app.route('/register',methods=["GET","POST"])
def register():
     if request.method == "POST":
        uname = request.form.get('name')
        email = request.form.get('email')
        passw  = request.form.get('passw')
        re_passw  = request.form.get('re_password')
        role  = request.form.get('role')

        register = Accounts(name = uname, email = email, password = passw,re_password =re_passw ,role=role,date=datetime.now())
        db.session.add(register)
        db.session.commit()
        return redirect(url_for("login"))
     return render_template('register.html')


@app.route('/register2',methods=["GET","POST"])
def register2():
     if request.method == "POST":
        uname = request.form.get('name')
        email = request.form.get('email')
        passw  = request.form.get('passw')
        re_passw  = request.form.get('re_password')
        role  = request.form.get('role')

        register1 = Accounts(name = uname, email = email, password = passw,re_password =re_passw ,role=role,date=datetime.now())
        db.session.add(register1)
        db.session.commit()
        return redirect(url_for("userlogin"))
     return render_template('register2.html')

@app.route('/about',methods=["GET","POST"])
def about():
    return render_template('about.html')

@app.route('/price')
def price():
    detai = Details.query.filter_by(price="10000").all()
    return render_template('price.html',detai=detai)


@app.route('/newoffer')
def newoffer():
   
    return render_template("newoffer.html")

@app.route('/newoffer2')
def newoffer2():
   
    return render_template("newoffer2.html")

class Details(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    location = db.Column(db.String(80))
    contact_no = db.Column(db.Integer)
    area = db.Column(db.Integer)
    price = db.Column(db.Integer)
    img = db.Column(db.String(12))
    surround = db.Column(db.String(20))
    type = db.Column(db.String(20))
    owner = db.Column(db.String(20))
    debt = db.Column(db.String(20))
    subject = db.Column(db.String(20))
    date = db.Column(db.String(20))
     

@app.route('/landlord',methods=["GET","POST"])
def landlord():
     if(request.method=='POST'):
        name=request.form.get('name')
        location=request.form.get('location')
        contact_no=request.form.get('contact_no')
        area=request.form.get('area')
        price=request.form.get('price')
        surround=request.form.get('surround')
        owner=request.form.get('owner')
        debt=request.form.get('debt')
        type=request.form.get('type')
        subject=request.form.get('subject')
        img=request.form.get('img')
        entry = Details(subject=subject,type=type,debt=debt,owner=owner,surround=surround,name=name,location=location,contact_no=contact_no,date=datetime.now(),area=area,price=price,img=img)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for("index2"))
     return render_template('landlord.html')



@app.route('/userlogin',methods=["GET","POST"])
def userlogin():
    if request.method=="POST":
        email=request.form.get('email')
        password=request.form.get('passw')
       
        
        login =  Accounts.query.filter_by(email=email, password=password).first()
        if login is not None:
             return redirect(url_for("index2"))
        entry = Accounts(email=email,date=datetime.now(),password=password)
        db.session.add(entry)
        db.session.commit()
    return render_template('userlogin.html')


class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    contact_no = db.Column(db.Integer)
    address = db.Column(db.String(12))
    date = db.Column(db.String(20))


@app.route('/contact',methods=["GET","POST"])
def contact():
    if(request.method=='POST'):
        name=request.form.get('name')
        email=request.form.get('email')
        contact_no=request.form.get('contact_no')
        address=request.form.get('address')
        entry = Contacts(name=name,email=email,contact_no=contact_no,date=datetime.now(),address=address)
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html')

@app.route('/clay')
def clay():
    detai = Details.query.filter_by(type="clay").all()
    return render_template('clay.html',detai=detai)



@app.route('/black')
def black():
    detai = Details.query.filter_by(type="black").all()
    return render_template('black.html',detai=detai)


@app.route('/red')
def red():
    detai = Details.query.filter_by(type="red").all()
    return render_template('red.html',detai=detai)



@app.route('/loamy')
def loamy():
    detai = Details.query.filter_by(type="loamy").all()
    return render_template('loamy.html',detai=detai)



@app.route('/dashboard',methods=["GET","POST"])
def dashboard():
    if request.method=="POST":
        username=request.form.get('email')
        userpass=request.form.get('passw')
        if (username == params['admin_user'] and  userpass == params['admin_pass']):
            contacts = Contacts.query.all()
            accounts = Accounts.query.all()
            details = Details.query.all()
        return render_template("dashboard.html",contacts=contacts,accounts=accounts,details=details)
    return render_template("admin.html",params=params)

if __name__ == '__main__':
    app.run(debug=True , port=5000)