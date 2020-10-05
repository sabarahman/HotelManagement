from flask import Flask, render_template, request, session,make_response
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)
matid = []
flag = None
import pymysql
db = pymysql.connect("localhost", "root", "saba", "db_hotel",cursorclass=pymysql.cursors.DictCursor)
cur = db.cursor()
@app.route('/logout.html')
@app.route("/login")
@app.route('/')
def index():
    return render_template("login.html")

@app.route('/validate',methods = ['GET','POST'])
def validate():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        q = "select * from tbl_user_registration where username = '%s' and password = '%s'"%(username,password)
        print(q)
        cur.execute(q)
        res = cur.fetchall()
        print(len(res))

        if len(res) == 1:
            session['username'] = username
            return render_template('homepage.html',username=username)
        if len(res) == 0:
            q = "select * from tbl_admin where username = '{}' and password = '{}'".format(username,password)
            cur.execute(q)
            res = cur.fetchall()
            print(len(res))
            session['username'] = username
            if len(res) >= 1:
                return render_template('adminhome.html',username=session['username'])
            else:
                return("<html><body><script>alert(\"Invalid User Id or password\");window.location.href=\"login\";</script></body></html>") 

@app.route("/add",methods = ['GET','POST'])
def add():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        cfm_pwd = request.form.get('cfm_pwd')
        mobile = request.form.get('mobile')
        if password == cfm_pwd:
            q = "insert into tbl_user_registration(username,email,password,mobile) values('%s','%s','%s','%s')"%(username,email,password,mobile)
            cur.execute(q)
            db.commit()
            return("<html><body><script>alert(\"Registered Successfully\");window.location.href=\"login\";</script></body></html>") 
        else:
            return("<html><body><script>alert(\"Password Missmatch\");window.location.href=\"register\";</script></body></html>") 

@app.route('/register')
@app.route('/register.html')
def register():
    return render_template('register.html')

@app.route('/usrsearch.html')
def usrsearch():
    return render_template('usrsearch.html',username = session['username'])

@app.route("/homepage.html")
def home():
    return render_template('homepage.html',username=session['username'])

@app.route("/adminhome.html")
def adminhome():
    return render_template("adminhome.html",username=session['username'])

@app.route("/roomtype.html")
def roomtype():
    return render_template("roomtype.html",username=session['username'])

@app.route("/report.html")
def report():
    q = "select * from tbl_bookng"
    cur.execute(q)
    res = cur.fetchall()
    return render_template("report.html",username=session['username'],data = res)

@app.route("/check",methods=['POST','GET'])
def check():
    if request.method == 'POST':                
        checkin = request.form.get('checkin')
        checkout = request.form.get('checkout')
        q = "select room_type from tbl_room"
        cur.execute(q)
        r = cur.fetchall()
        d = {}
        for i in r:
        #     print(i)
            q = """
            SELECT COUNT(*) as count FROM tbl_bookng WHERE room_type = '{room_type}' AND  check_in >= '{checkin}' AND check_out <= '{checkout}' AND is_vacated = 0
            """.format(room_type=i['room_type'],checkin=checkin,checkout=checkout)
            cur.execute(q)
            res=cur.fetchall()
            d[i['room_type']] = res[0]['count']
        print(d)
        q = """
        select * from tbl_room
        """
        cur.execute(q)
        res=cur.fetchall()

        data = {}
        for i in range(len(res)):
            print(res[i])
            data[res[i]['room_type']] = res[i]['total_rooms'] - d[res[i]['room_type']]
        return render_template('usrsearchresult.html',username = session['username'],data=data)

@app.route("/bookroom.html")
def book():
    q = """
    select room_type from tbl_room
    """
    cur.execute(q)
    r = cur.fetchall()
    return render_template("bookroom.html",data=r,username=session["username"])

@app.route("/bookroom",methods=['POST','GET'])
def bookroom():
    if request.method == 'POST':
        no_of_guest = request.form.get('no_of_guest')
        roomtype = request.form.get('roomtype')
        checkin = request.form.get('checkin')
        checkout = request.form.get('checkout')
        q = """ insert into tbl_bookng (username,room_type,no_of_guest,check_in,check_out,is_vacated) 
        values('%s','%s','%s','%s','%s',0)"""%(session['username'],roomtype,no_of_guest,checkin,checkout)
        print(q)
        cur.execute(q)
        db.commit()
        return("<html><body><script>alert(\"Room Booked Successfully\");window.location.href=\"bookroom.html\";</script></body></html>") 

@app.route("/addroom",methods=['POST','GET'])
def addroom():
    if request.method == 'POST':
        q = """ select room_type from tbl_room
        """
        cur.execute(q)
        res = cur.fetchall()
        rooms = []
        for i in range(len(res)):
            rooms.append(res[i]['room_type'])  
        roomtype = request.form.get('roomtype')
        no_of_rooms = request.form.get('num_of_rooms')
        if roomtype in rooms:
            q = """
            update tbl_room set total_rooms = '%s' where room_type = '%s'
            """%(no_of_rooms,roomtype)
            cur.execute(q)
            db.commit()
            return("<html><body><script>alert(\"Room Type Updated Successfully\");window.location.href=\"roomtype.html\";</script></body></html>") 
        else:
            q = """
            insert into tbl_room (room_type,total_rooms) values ('%s','%s')
            """%(roomtype,no_of_rooms)
            cur.execute(q)
            db.commit()
            return("<html><body><script>alert(\"Room Type Added Successfully\");window.location.href=\"roomtype.html\";</script></body></html>") 

@app.route("/search",methods=["POST","GET"])
def search():
    if request.method == "POST":
        query = request.form.get('query')
        q = """ select * from tbl_bookng where username like '{query}%' or room_type like '{query}%' or no_of_guest like '{query}%' or check_in like '{query}%' or check_out like '{query}%'
        """.format(query=query)
        cur.execute(q)
        res = cur.fetchall()
        print(res)
        return render_template("report.html",username=session['username'],data = res)


if __name__ == '__main__':
    app.run(debug=True)
