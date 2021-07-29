from flask import Flask, render_template #追加
import pymysql #追加

app = Flask(__name__)

@app.route('/')
def hello():

    #db setting
    db = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='testdb',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
        )

    cur = db.cursor()
    sql = "select * from members"
    cur.execute(sql)
    members = cur.fetchall()

    cur.close()
    db.close()

    #return name
    return render_template('hello.html', title='flask test', members=members) #変更

## おまじない
if __name__ == "__main__":
    app.run(debug=True)