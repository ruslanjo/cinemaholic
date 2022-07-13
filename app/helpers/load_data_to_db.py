#from app.setup_db import db
#from app.main import app
from app.dao.models.genre import Genre, Director

#print(1)
#with app.app_context():
#    db.create_all()

from app.config import Config
from app.main import create_app
from app.setup_db import db

if __name__ == '__main__':
    with create_app(Config()).app_context():
        db.create_all()
