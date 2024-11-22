# coding="utf-8"

from flask import Flask, jsonify, request, make_response
import mysql.connector

db = mysql.connector.connect(
    user='debian-sys-maint',
    password='TdvZYQtXDr3RBB0s',
    host='localhost',
    database='BUAA_BBS'
)

cursor = db.cursor()

# CREATE TABLE USERINFO (User_Id INT NOT NULL, User_Name VARCHAR(30) NOT NULL, User_Password VARCHAR(30) NOT NULL, PRIMARY KEY (User_Name))

# sql = "DROP TABLE IF EXISTS CONTENT"
#
# cursor.execute(sql)
# db.commit()

# 如果没有 CONTENT 数据表，则创建
# sql = "CREATE TABLE IF NOT EXISTS \
#        CONTENT (User_id INT NOT NULL, \
#        Title VARCHAR(255), \
#        Text VARCHAR(21845), \
#        Time DATETIME,  \
#        Position INT NOT NULL)"
#
# cursor.execute(sql)

app = Flask(__name__)

# 登录/注册接口

def request_register(User_Id, User_Name, User_Password):
    db = mysql.connector.connect(
        user='debian-sys-maint',
        password='TdvZYQtXDr3RBB0s',
        host='localhost',
        database='BUAA_BBS'
    )
    cursor = db.cursor()
    register_sql = "INSERT INTO USERINFO \
                    (User_Id, User_Name, User_Password) \
                    VALUES (%s, %s, %s)"
    register_data = (User_Id, User_Name, User_Password)
    try:
        cursor.execute(register_sql, register_data)
        db.commit()
        db.close()
        return ("Register Success!")
    except mysql.connector.Error as err:
        db.rollback()
        db.close()
        return (f"Error: unable to insert data{err}")

def request_GetUserInfo(User_Name):
    db = mysql.connector.connect(
        user='debian-sys-maint',
        password='TdvZYQtXDr3RBB0s',
        host='localhost',
        database='BUAA_BBS'
    )

    cursor = db.cursor()
    get_userinfo_sql = "SELECT * FROM USERINFO WHERE User_Name = %s"
    get_userinfo_data = (User_Name,)
    try:
        cursor.execute(get_userinfo_sql, get_userinfo_data)
        results = cursor.fetchone()
        if results is None:
            db.close()
            return "User not found"
        else:
            db.close()
            return results
    except mysql.connector.Error as err:
        db.close()
        return (f"Error: unable to get password{err}")

def request_GetLatestUserId():
    db = mysql.connector.connect(
        user='debian-sys-maint',
        password='TdvZYQtXDr3RBB0s',
        host='localhost',
        database='BUAA_BBS'
    )
    cursor = db.cursor()
    get_latest_user_id_sql = "SELECT MAX(User_Id) FROM USERINFO"
    try:
        cursor.execute(get_latest_user_id_sql)
        results = cursor.fetchone()
        db.close()
        return results[0] + 1
    except mysql.connector.Error as err:
        db.close()
        return (f"Error: unable to get latest user id{err}")

@app.route('/latest_user_id', methods=['GET'])
def latest_user_id():
    response = make_response(jsonify(request_GetLatestUserId()))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
@app.route('/login', methods=['OPTIONS'])
def login_options():
    response = make_response()
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response
@app.route('/register', methods=['OPTIONS'])
def register_options():
    response = make_response()
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response

@app.route('/login', methods=['POST'])
def login():
    Request = request.get_json()
    User_Name = Request['User_Name']
    data = request_GetUserInfo(User_Name)
    if data == "User not found":
        response = make_response(jsonify("User not found"))
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    else :
        response = make_response(jsonify(data))
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

@app.route('/register', methods=['POST'])
def register():
    Request = request.get_json()
    User_Id = Request['User_Id']
    User_Name = Request['User_Name']
    User_Password = Request['User_Password']
    response = make_response(jsonify(request_register(User_Id, User_Name, User_Password)))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


# 发布帖子接口

def getLatestPostId():
    db = mysql.connector.connect(
    user='debian-sys-maint',
    password='TdvZYQtXDr3RBB0s',
    host='localhost',
    database='BUAA_BBS'
    )

    cursor = db.cursor()
    get_latest_post_id_sql = "SELECT MAX(Post_Id) FROM CONTENT"
    try:
        cursor.execute(get_latest_post_id_sql)
        results = cursor.fetchone()
        db.close()
        if(type(results[0]) == type(None)):
            return 1
        return results[0] + 1
    except mysql.connector.Error as err:
        db.close()
        return (f"Error: unable to get latest post id{err}")

def request_Insert(User_id, Title, Text, Time, DATABASE):
    position = -1
    match DATABASE:
        case "study":
            position = 1
        case "sport":
            position = 2
        case "entertainment":
            position = 3
        case "comment":
            position = 4
        case _:
            position = -1
    if position == -1:
        return "Invalid DATABASE"
    Max_Post_id = getLatestPostId()
    db = mysql.connector.connect(
        user='debian-sys-maint',
        password='TdvZYQtXDr3RBB0s',
        host='localhost',
        database='BUAA_BBS'
    )
    cursor = db.cursor()
    insert_sql = "INSERT INTO CONTENT \
                  (User_id, Title, Text, Time, Position, Post_Id) \
                  VALUES (%s, %s, %s, %s, %s, %s)"
    insert_data = (User_id, Title, Text, Time, position, Max_Post_id)
    try:
        cursor.execute(insert_sql, insert_data)
        db.commit()
        db.close()
        return ("Insert Success!")
    except mysql.connector.Error as err:
        db.rollback()
        db.close()
        return (f"Error: unable to insert data{err}")

def request_Delete(Post_Id):
    db = mysql.connector.connect(
        user='debian-sys-maint',
        password='TdvZYQtXDr3RBB0s',
        host='localhost',
        database='BUAA_BBS'
    )

    cursor = db.cursor()
    delete_sql = "DELETE FROM CONTENT WHERE Post_Id = %s"
    delete_data = (Post_Id,)
    try:
        cursor.execute(delete_sql, delete_data)
        db.commit()
        db.close()
        return ("Delete Success!")
    except mysql.connector.Error as err:
        db.rollback()
        db.close()
        return (f"Error: unable to delete data{err}")

def request_read(DATABASE):
    match DATABASE:
        case "study":
            position = 1
        case "sport":
            position = 2
        case "entertainment":
            position = 3
        case "comment":
            position = 4
        case _:
            position = -1
    db = mysql.connector.connect(
        user='debian-sys-maint',
        password='TdvZYQtXDr3RBB0s',
        host='localhost',
        database='BUAA_BBS'
    )

    cursor = db.cursor()
    if position == -1:
        db.close()
        return "Invalid DATABASE"
    if position != 4:
        read_sql = "SELECT * FROM CONTENT WHERE Position = %s" \
                    % (position,)
        try:
            cursor.execute(read_sql,)
            results = cursor.fetchall()
            db.close()
            return results
        except mysql.connector.Error as err:
            db.close()
            return (f"Error: unable to read data{err}")

    else:
        pass

def request_GetName_by_Id(User_id):
    db = mysql.connector.connect(
        user='debian-sys-maint',
        password='TdvZYQtXDr3RBB0s',
        host='localhost',
        database='BUAA_BBS'
    )

    cursor = db.cursor()
    get_name_sql = "SELECT User_Name FROM USERINFO WHERE User_Id = %s"
    get_name_data = (User_id,)
    try:
        cursor.execute(get_name_sql, get_name_data)
        results = cursor.fetchone()
        db.close()
        if results is None:
            return "User not found"
        return results[0]
    except mysql.connector.Error as err:
        db.close()
        return f"Error: unable to get name{err}"


@app.route('/delete_post', methods=['OPTIONS'])
def delete_post_options():
    response = make_response()
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response

@app.route('/delete_post', methods=['POST'])
def delete_post():
    Request = request.json
    Post_Id = Request['Post_id']
    response = make_response(jsonify(request_Delete(Post_Id)))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/get_name_by_id', methods=['OPTIONS'])
def get_name_by_id_options():
    response = make_response()
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response

@app.route('/get_name_by_id', methods=['POST'])
def get_name_by_id():
    Request = request.json
    User_id = Request['User_id']
    response = make_response(jsonify(request_GetName_by_Id(User_id)))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

# TODO: 实现评论功能

@app.route('/study', methods=['GET'])
def study():
    response = make_response(jsonify(request_read("study")))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/sport', methods=['GET'])
def sport():
    response = make_response(jsonify(request_read("sport")))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/entertainment', methods=['GET'])
def entertainment():
    response = make_response(jsonify(request_read("entertainment")))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/publishpost', methods=['OPTIONS'])
def publishpost_options():
    response = make_response()
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response

@app.route('/publishpost', methods=['POST'])
def study_post():
    Request = request.json
    User_id = Request['User_id']
    Title = Request['Title']
    Text = Request['Text']
    Time = Request['Time']
    DATABASE = Request['DATABASE']
    response = make_response(jsonify(request_Insert(User_id, Title, Text, Time, DATABASE)))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


# TODO: 实现评论功能

if __name__ == '__main__':
    app.run()