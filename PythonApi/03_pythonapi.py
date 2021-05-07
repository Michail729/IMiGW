import psycopg2
import flask
import json
from flask import jsonify

app = flask.Flask(__name__)

con = psycopg2.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password = "kosowo123")


cur = con.cursor()
@app.route('/gettreatments', methods=['GET', 'POST'])
def gettreatments():
    msg_received = flask.request.get_json()
    msg_subject = msg_received["subject"]
    if msg_subject == "gettreatments":
        return treatments(msg_received)
    else:
        return "Invalid request."

@app.route('/getterrain', methods=['GET', 'POST'])
def getterrain():
    msg_received = flask.request.get_json()
    msg_subject = msg_received["subject"]
    if msg_subject == "terrain":
        return terrain(msg_received)
    else:
        return "Invalid request."


@app.route('/user', methods=['GET', 'POST'])
def user():
    msg_received = flask.request.get_json()
    msg_subject = msg_received["subject"]


    if msg_subject == "login":
        return login(msg_received)
    else:
        return "Invalid request."

def login(msg_received):
    login = msg_received["username"]
    password = msg_received["password"]

    select_query = "SELECT login FROM personaldata where login = " + "'" + login + "' and password = " + "'" + password + "'"
    
    cur.execute(select_query)
    records = cur.fetchall()

    if len(records) == 0:
        return "failure"
    else:
        select_query= "SELECT id FROM personaldata where login = " + "'" + login + "'"
        cur.execute(select_query)
        response = cur.fetchall()
        return jsonify(response)

def terrain(msg_received):
    userid = msg_received["userid"]
    
    select_query= "SELECT id, terrainname FROM terrain where userid = " + "'" + userid + "'"
    cur.execute(select_query)
    response = cur.fetchall()
    return jsonify(response)

def treatments(msg_received):
    terrainid = msg_received["terrainid"]
    
    select_query= "SELECT date, teratmentname, data1, data2 FROM treatments where terrainid = " + "'" + terrainid + "'"
    cur.execute(select_query)
    response = cur.fetchall()
    return jsonify(response)




app.run(host="192.168.8.106", port=5000, debug=True, threaded=True)



#for r in rows:
#    print (f"id {r[0]} login {r[1]} password {r[2]}")


cur.close()
#closing connection
con.close()