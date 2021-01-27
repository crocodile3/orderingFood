from flask import Flask

# from imoc import route_imoc

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.register_blueprint(route_imoc,url_prefix="/imoc")

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Cyh981134@139.9.78.33/mysql'

db = SQLAlchemy(app)


@app.route('/')
def index():
    from sqlalchemy import text
    sql = text("select * from `user`")
    res = db.engine.execute(sql)
    for row in res:
        app.logger.info(row)
    return "hello flask"


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)