from flask import Flask, redirect, url_for, request,render_template
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="mysql",
  database="MyPythonDatabase"
)
mycursor = mydb.cursor()
app = Flask(__name__)
@app.route('/',methods = ['POST', 'GET'])
def index():
  if request.method == 'POST': ##check if there is post data
         Name = request.form['txtName']
         Email = request.form['txtEmail']
         Phone = request.form['txtPhone']
         Msg = request.form['txtMsg']
         sql = "INSERT INTO contact (name,mail,phoneNum,message) VALUES (%s, %s, %s, %s)"
         val = (Name,Email,Phone,Msg)
         mycursor.execute(sql, val)
         mydb.commit()   
         return render_template("index.html")
  else:     
     return render_template("index.html")

@app.route('/loginPatient',methods = ['POST', 'GET'])
def loginPatient():
    if request.method == 'POST': ##check if there is post data
        email = request.form['email']
        password = request.form['password']
        mycursor.execute("SELECT * FROM members WHERE email = %s AND password = %s AND type = %s", (email, password,'patient'))
        account = mycursor.fetchone()
        print(account)
        # If account exists in accounts table in out database
        if account:    
            return render_template("patientTest.html")
        else:     
            return 'Not Logged in '
    return render_template("loginPatient.html")  
@app.route('/loginDoctor',methods = ['POST', 'GET'])
def loginDoctor():
    if request.method == 'POST': ##check if there is post data
        email = request.form['email']
        password = request.form['password']
        mycursor.execute("SELECT * FROM members WHERE email = %s AND password = %s AND type = %s ", (email, password,'doctor'))
        account = mycursor.fetchone()
        print(account)
        # If account exists in accounts table in out database
        if account:    
            return 'Logged in successfully!'
        else:     
            return 'Not Logged in '
    return render_template("loginDoctor.html")  
@app.route('/loginAdmin',methods = ['POST', 'GET'])
def loginAdmin():
    if request.method == 'POST': ##check if there is post data
        email = request.form['email']
        password = request.form['password']
        mycursor.execute("SELECT * FROM members WHERE email = %s AND password = %s AND type = %s ", (email, password,'admin'))
        account = mycursor.fetchone()
        print(account)
        # If account exists in accounts table in out database
        if account:    
             mycursor.execute("SELECT * FROM members")
           
             myresult = mycursor.fetchall()
             print(myresult)
             mycursor.execute("SELECT * FROM contact")
          
             myresult2 = mycursor.fetchall()
             print(myresult2)
             return render_template("admin.html",admindata=myresult,contact=myresult2) 
        else:     
            return 'Not Logged in '
    return render_template("loginAdmin.html")            

@app.route('/SignUpPatient',methods = ['POST', 'GET'])
def SignUpPatient():
    if request.method == 'POST': ##check if there is post data
         email = request.form['email']
         password = request.form['password']
         sql = "INSERT INTO members (email,password,type) VALUES (%s, %s, %s)"
         val = (email,password,'patient')
         mycursor.execute(sql, val)
         mydb.commit()   
         return render_template("index.html")
    else:     
     return render_template("SignUpPatient.html")

@app.route('/SignUpDoctor',methods = ['POST', 'GET'])
def SignUpDoctor():
    if request.method == 'POST': ##check if there is post data
         email = request.form['email']
         password = request.form['password']
         sql = "INSERT INTO members (email,password,type) VALUES (%s, %s, %s)"
         val = (email,password,'doctor')
         mycursor.execute(sql, val)
         mydb.commit()   
         return render_template("index.html")
    else:     
      return render_template("SignUpDoctor.html")



if __name__ == '__main__':
   app.run(debug=False,host='0.0.0.0')
   
