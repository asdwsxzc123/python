# coding:utf-8
import datetime,string
from ihome import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
# 创建flask应用对象
app = create_app('dev')

manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)
if __name__ == "__main__":
    # app.run(host='0.0.0.0',port=7788)
    # print(app.url_map)
    today = datetime.datetime.now() 
    print('0.0.0.0 -p 7788',today)
    manager.run()
# python manage.py runserver -h '0.0.0.0' -p 7788
# python manage.py db init
# python manage.py db migrate -m 'init'
#  python manage.py db upgrade




