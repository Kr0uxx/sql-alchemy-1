from data.users import User
import data.db_session as db_session


db_session.global_init("db/blogs.db")
db_sess = db_session.create_session()

user = User()

user.surname = "Scott"
user.name = "Ridley"
user.age = 21
user.position = "captain"
user.speciality = "research engineer"
user.address = "module_1"
user.email = "scott_chief@mars.org"

db_sess.add(user)

user = User()

user.surname = "Obama"
user.name = "Barak"
user.age = 22
user.position = "recruit"
user.speciality = "scientist"
user.address = "module_2"
user.email = "Obama_sc@mars.org"

db_sess.add(user)

user = User()

user.surname = "Mercury"
user.name = "Freddie"
user.age = 30
user.position = "vice captain"
user.speciality = "doctor"
user.address = "module_1"
user.email = "Fred@mars.org"

db_sess.add(user)

user = User()

user.surname = "Michelin"
user.name = "Andre"
user.age = 23
user.position = "recruit"
user.speciality = "constructor"
user.address = "module_2"
user.email = "Andre_builder@mars.org"

db_sess.add(user)

db_sess.commit()
