from flask import Flask, render_template, request, redirect, url_for, session
import re

import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=21fecfd8-47b7-4937-840d-d791d0218660.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31864;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=mqm10930;PWD=0W28Fba9aWlL3Gtd",'','')

app = Flask(__name__)
app.secret_key = 'as'
@app.route("/")
def Home():
    return render_template("Home.html")
@app.route('/' methods=['GET','POST'])
@app.route('/register',methods=['GET','POST'])
def Register():
    msg=""
    if request.method == 'POST':
        username=request.form['username']
        address=request.form['address']
        email=request.form['email']
        phone=request.form['phone']
        password=request.form['password']
        sql= "SELECT * FROM registers WHERE username=?;"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)

    if account:
        msg="User already exists"
      return render_template('Register.html', msg=msg)
    else:
      insert_sql = "INSERT INTO registers VALUES (?,?,?,?,?)"
      prep_stmt = ibm_db.prepare(conn, insert_sql)
      ibm_db.bind_param(prep_stmt, 2, username)
      ibm_db.bind_param(prep_stmt, 3, address)
      ibm_db.bind_param(prep_stmt, 4, email)
      ibm_db.bind_param(prep_stmt, 5, phone)
      ibm_db.bind_param(prep_stmt, 6, password)
      ibm_db.execute(prep_stmt)
      msg='You have successfully registered'
     return render_template('Login.html', msg="msg")
else:
    msg='Please fill out the form'
    return render_template('Register.html',msg=msg)       

@app.route('/Login', methods=['GET', 'POST'])
def Login():
    global userid
    msg = ' '
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        query = "select * from user1 where username=? and password=?"
        stmt = ibm_db.prepare(connection, query)
        ibm_db.bind_param(stmt, 1, username)
        ibm_db.bind_param(stmt, 2, password)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            session['Loggedin'] = True
            session['id'] = account['USERNAME']
            session['username'] = account['USERNAME']
            msg = 'Logged in Successfully'
            return render_template('About.html', msg=msg, username=str.upper(username))
        else:
            msg = 'Incorrect Username or Password'
            return render_template('Login.html', msg=msg)
    else:
        msg = 'PLEASE FILL OUT OF THE FORM'
        return render_template('Login.html', msg=msg)


    
@app.route("/About")
def About():
    return render_template("About.html")

if __name__ == "__main__" :
    app.run(debug=True)
