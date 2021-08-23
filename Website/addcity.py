from app import db
from app import City

db.create_all()

seattle = City(name='Seattle')
london = City(name='London')
abuja = City(name='Abuja')
dubai = City(name='Dubai')

db.session.add_all([seattle, london, abuja, dubai])
db.session.commit()