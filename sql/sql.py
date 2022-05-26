from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:ndu+1234@127.0.0.1:3306/crawl"
db = SQLAlchemy(app)

@app.route('/')
def index():
    return "Successfully loaded database!"

@app.route('/insert')
def insert():
    sql = "INSERT INTO news (article) VALUES('Hello World!')"
    db.engine.execute(sql)
    return "Successfully inserted into database!"

@app.route('/query')
def query():
    sql = "SELECT * FROM news ORDER BY ID;"
    news = db.engine.execute(sql)
    msg = ""
    for n in news:
        msg = msg + str(n['ID']) + '<br>'
        msg = msg + n['article'] + '<br>'
    return msg

@app.route('/delete/<int:newsID>')
def delete(newsID):
    sql = "DELETE FROM news WHERE ID = " + str(newsID) + ";"
    news = db.engine.execute(sql)
    return "Deleted successfully!"

@app.route('/update/<int:newsID>')
def update(newsID):
    sql = "UPDATE news SET article = 'Hello World!' WHERE ID = " + str(newsID) + ";"
    news = db.engine.execute(sql)
    return "Updated successfully!"

if __name__ == "__main__":
    app.run()