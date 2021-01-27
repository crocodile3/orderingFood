from flask import Blueprint

from app import db, app

route_imoc = Blueprint('imoc',__name__)


@route_imoc.route('/')
def index():
    return 'immoc index'


@route_imoc.route('/hello')
def hello():
    # from sqlalchemy import text
    # sql = text("select * from `user`")
    # res = db.engine.execute(sql)
    # for row in res:
    #     app.logger.info(row)

    return 'imoc hello'
