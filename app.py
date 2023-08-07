from flask import Flask,render_template,request
from flask_mysqldb import MySQL
app=Flask(__name__)
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="Drishti@123"
app.config['MYSQL_DB']="cv"

mysql=MySQL(app)
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=="POST":
        name=request.form['Name']
        subject=request.form['Subject']
        email=request.form['Email']
        message=request.form['Message']
        cur_obj=mysql.connection.cursor()
        cur_obj.execute("INSERT INTO creative(Name,Subject,Email,Message) VALUES(%s,%s,%s,%s)",(name,subject,email,message))
        mysql.connection.commit()
        cur_obj.close()
        return "Message sent Successfully!!"    
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)