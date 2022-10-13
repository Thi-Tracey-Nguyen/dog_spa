from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://tracey:123456@127.0.0.1:5432/dog_spa'
app.config['JSON_SORT_KEY'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Client(db.Model): 
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    animal_type = db.Column(db.String)
    breed = db.Column(db.String)
    phone = db.Column(db.String)
    owner = db.Column(db.String)

class Groomer(db.Model):
    __tablename__ = 'groomers'
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String)
    l_name = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)

class Appointment(db.Model):
    __tablename__ = 'appointments'
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer)
    groomer_id = db.Column(db.Integer)
    app_date = db.Column(db.Date)
    app_time = db.Column(db.Time)


@app.cli.command('create')
def create_table():
    db.create_all()
    print('Tables created!')

@app.cli.command('drop')
def drop_table():
    db.drop_all()
    print('Tables dropped!')

@app.cli.command('seed')
def seed_table():
    clients = [
    Client(
        name= 'Oscar',
        animal_type= 'Dog',
        breed= 'Spoodle',
        phone= '123467',
        owner= 'Tracey'
    ),
    Client(
        name= 'Archie',
        animal_type= 'Cat',
        breed= 'Tabby',
        phone= '123467',
        owner= 'Tracey'
    ),
    Client(
        name= 'Joey',
        animal_type= 'Cat',
        breed= 'Tabby',
        phone= '473732',
        owner= 'Jehan'
    ),
    Client(
        name= 'Kookoo',
        animal_type= 'Bird',
        breed= 'Cockatiel',
        phone= '194422',
        owner= 'Sammy'
    )]

    groomers = [
    Groomer(
        f_name= 'Katrina',
        l_name= 'Ball',
        email= 'katrina_ball@dogspa.com',
        phone= '123469'
    ),
    Groomer(
        f_name= 'Chesley',
        l_name= 'Runolf',
        email= 'chesley_runolf@dogspa.com',
        phone= '557334'
    ),
    Groomer(
        f_name= 'Verona',
        l_name= 'Bogisi',
        email= 'verona_bogisi@dogspa.com',
        phone= '990348'
    ),
    Groomer(
        f_name= 'Zelma',
        l_name= 'Fay',
        email= 'elma_fay@dogspa.com',
        phone= '103635',
    )]

    appointments = [ 
    Appointment(
        client_id= 1,
        groomer_id= 3,
        app_date= '2022-12-01',
        app_time= '12:35'
    ),
    Appointment(
        client_id= 2,
        groomer_id= 1,
        app_date= '2022-11-28',
        app_time= '10:15'
    ),
    Appointment(
        client_id= 3,
        groomer_id= 4,
        app_date= '2022-11-30',
        app_time= '13:00'
    ),
    Appointment(
        client_id= 4,
        groomer_id= 2,
        app_date= '2022-12-12',
        app_time= '12:35'
    ),
    Appointment(
        client_id= 1,
        groomer_id= 2,
        app_date= '2022-12-20',
        app_time= '14:25'
    ),
    Appointment(
        client_id= 4,
        groomer_id= 1,
        app_date= '2023-01-28',
        app_time= '10:00'
    ),
    Appointment(
        client_id= 3,
        groomer_id= 1,
        app_date= '2023-01-11',
        app_time= '10:10'
    ),
    Appointment(
        client_id= 1,
        groomer_id= 3,
        app_date= '2023-01-12',
        app_time= '11:35'
    )]

    db.session.add_all(clients)
    db.session.add_all(groomers)
    db.session.add_all(appointments)
    db.session.commit()
    print('Tables seeded!')

class ClientSchema(ma.Schema):
    class Meta: 
        fields = ('id', 'name', 'animal_type', 'breed', 'owner', 'phone')

@app.cli.command('clients')
def get_clients():
    stmt = db.select(Client)
    clients = db.session.scalars(stmt)
    print(ClientSchema(many=True).dump(clients))

@app.route('/')
def index():
    return 'Welcome to Dog Spa'


if __name__ == '__main__':
    app.run()