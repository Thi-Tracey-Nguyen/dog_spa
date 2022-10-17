from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://tracey:123456@127.0.0.1:5432/dog_spa'
app.config['JSON_SORT_KEYS'] = False

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

class Booking(db.Model):
    __tablename__ = 'bookings'
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
    ),
    Client(
        name= 'Meredith',
        animal_type= 'Cat',
        breed= 'Scottish fold',
        phone= '104722',
        owner= 'Taylor'
    ),
    Client(
        name= 'Olivia',
        animal_type= 'Cat',
        breed= 'Scottish fold',
        phone= '104722',
        owner= 'Taylor'
    ),
    Client(
        name= 'Pig',
        animal_type= 'Pig',
        breed= 'Miniature',
        phone= '247562',
        owner= 'Miley'
    ),
    Client(
        name= 'Toulouse',
        animal_type= 'Dog',
        breed= 'Beagel-Chihuahua',
        phone= '247432',
        owner= 'Ariana'
    ),
    Client(
        name= 'Dora',
        animal_type= 'Dog',
        breed= 'Labradoodle',
        phone= '364323',
        owner= 'Liam'
    ),
    Client(
        name= 'Smoke',
        animal_type= 'Horse',
        breed= 'Gidran',
        phone= '285732',
        owner= 'Channing'
    )
    ]

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

    bookings = [ 
    Booking(
        client_id= 1,
        groomer_id= 3,
        app_date= '2022-12-01',
        app_time= '12:35'
    ),
    Booking(
        client_id= 2,
        groomer_id= 1,
        app_date= '2022-11-28',
        app_time= '10:15'
    ),
    Booking(
        client_id= 3,
        groomer_id= 4,
        app_date= '2022-11-30',
        app_time= '13:00'
    ),
    Booking(
        client_id= 4,
        groomer_id= 2,
        app_date= '2022-12-12',
        app_time= '12:35'
    ),
    Booking(
        client_id= 1,
        groomer_id= 2,
        app_date= '2022-12-20',
        app_time= '14:25'
    ),
    Booking(
        client_id= 4,
        groomer_id= 1,
        app_date= '2023-01-28',
        app_time= '10:00'
    ),
    Booking(
        client_id= 3,
        groomer_id= 1,
        app_date= '2023-01-11',
        app_time= '10:10'
    ),
    Booking(
        client_id= 1,
        groomer_id= 3,
        app_date= '2023-01-12',
        app_time= '11:35'
    )]

    db.session.add_all(clients)
    db.session.add_all(groomers)
    db.session.add_all(bookings)
    db.session.commit()
    print('Tables seeded!')

class ClientSchema(ma.Schema):
    class Meta: 
        fields = ('id', 'name', 'animal_type', 'breed')
        # ordered = True

class BookingSchema(ma.Schema):
    class Meta: 
        fields = ('id', 'client_id', 'groomer_id', 'app_date', 'app_time')
        ordered = True

@app.cli.command('clients')
def get_clients():
    # Your code here
    
@app.route('/bookings/')
def bookings():
    stmt = db.select(Booking)
    bookings = db.session.scalars(stmt)
    bookings_details = []
    for booking in bookings:
        booking_details = dict({'id': booking.id, 'date' : booking.app_date})
        bookings_details.append(booking_details)
    return bookings_details

@app.route('/booking/<int:booking_id>')
def booking_lookup(booking_id):
    stmt = db.select(Booking).filter_by(id = booking_id)
    bookings = db.session.scalars(stmt)
    return BookingSchema(many=True).dump(bookings)

@app.route('/')
def index():
    return 'Welcome to Dog Spa'


if __name__ == '__main__':
    app.run()