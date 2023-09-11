from flask import *
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/index')
def index():
    return "Hello there"
@app.route('/ind')
def ind():
    return "Hello there"
@app.route('/inde')
def inde():
    return "Hello there"
@app.route('/name')
def name():
    return "Hello there"
@app.route('/createaccount', methods=["GET" ,"POST"])
def createaccount():
    if request.method =="GET":
        return render_template('account.html')
    else:
        username = request.form["username"]
        email = request.form["email"]
        phone_number = request.form["phone"]
        location = request.form["location"]

    
        connection = pymysql.connect(host='localhost',user='root',password='',database='MpesaTestDB')

        mycursor = connection.cursor()

        myquery = '''
        insert into thistable(username,email,phone_number,location)
        values (%s,%s,%s,%s)
        '''

        mycursor.execute(myquery,(username,email,phone_number,location))

        connection.commit()
        return "saved successfully"

app.run(debug=True)