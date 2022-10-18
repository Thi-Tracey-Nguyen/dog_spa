from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
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
    phone = db.Column(db.Integer)
    owner = db.Column(db.String)
    db.UniqueConstraint(name, phone)

class Groomer(db.Model):
    __tablename__ = 'groomers'
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String)
    l_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    phone = db.Column(db.Integer, unique=True)

class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer)
    groomer_id = db.Column(db.Integer)
    date = db.Column(db.Date)
    time = db.Column(db.Time)


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
        phone= 123467,
        owner= 'Tracey'
    ),
    Client(
        name= 'Archie',
        animal_type= 'Cat',
        breed= 'Tabby',
        phone= 123467,
        owner= 'Tracey'
    ),
    Client(
        name= 'Joey',
        animal_type= 'Cat',
        breed= 'Tabby',
        phone= 473732,
        owner= 'Jehan'
    ),
    Client(
        name= 'Kookoo',
        animal_type= 'Bird',
        breed= 'Cockatiel',
        phone= 194422,
        owner= 'Sammy'
    ),
    Client(
        name= 'Meredith',
        animal_type= 'Cat',
        breed= 'Scottish fold',
        phone= 104722,
        owner= 'Taylor'
    ),
    Client(
        name= 'Olivia',
        animal_type= 'Cat',
        breed= 'Scottish fold',
        phone= 104722,
        owner= 'Taylor'
    ),
    Client(
        name= 'Pig',
        animal_type= 'Pig',
        breed= 'Miniature',
        phone= 247562,
        owner= 'Miley'
    ),
    Client(
        name= 'Toulouse',
        animal_type= 'Dog',
        breed= 'Beagel-Chihuahua',
        phone= 247432,
        owner= 'Ariana'
    ),
    Client(
        name= 'Dora',
        animal_type= 'Dog',
        breed= 'Labradoodle',
        phone= 364323,
        owner= 'Liam'
    ),
    Client(
        name= 'Smoke',
        animal_type= 'Horse',
        breed= 'Gidran',
        phone= 285732,
        owner= 'Channing'
    )
    ]

    groomers = [
    Groomer(
        f_name= 'Katrina',
        l_name= 'Ball',
        email= 'katrina_ball@dogspa.com',
        phone= 123469
    ),
    Groomer(
        f_name= 'Chesley',
        l_name= 'Runolf',
        email= 'chesley_runolf@dogspa.com',
        phone= 557334
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
        phone= 103635,
    ), 
    Groomer(
        f_name = "Cherly",
        l_name = "Sansbury",
        email = "cherly.sansbury@dog_spa.com",
        phone = 767890
    ),
    Groomer(
        f_name = "Barbara",
        l_name = "Mar",
        email = "barbara.ma@dog_spa.com",
        phone = 239877
    ),
    Groomer(
        f_name = "John",
        l_name = "Torres",
        email = "john.torres@dog_spa.com",
        phone = 500982
    )
    ]

    bookings = [ 
    Booking(
        client_id= 1,
        groomer_id= 3,
        date= '2022-12-01',
        time= '12:35'
    ),
    Booking(
        client_id= 2,
        groomer_id= 1,
        date= '2022-11-28',
        time= '10:15'
    ),
    Booking(
        client_id= 3,
        groomer_id= 4,
        date= '2022-11-30',
        time= '13:00'
    ),
    Booking(
        client_id= 4,
        groomer_id= 2,
        date= '2022-12-12',
        time= '12:35'
    ),
    Booking(
        client_id= 1,
        groomer_id= 2,
        date= '2022-12-20',
        time= '14:25'
    ),
    Booking(
        client_id= 4,
        groomer_id= 1,
        date= '2023-01-28',
        time= '10:00'
    ),
    Booking(
        client_id= 8,
        groomer_id= 5,
        date= '2023-01-15',
        time= '16:40'
    ),
    Booking(
        client_id= 5,
        groomer_id= 6,
        date= '2023-01-02',
        time= '09:10'
    ),
    Booking(
        client_id= 7,
        groomer_id= 5,
        date= '2023-01-07',
        time= '15:30'
    ),
    Booking(
        client_id= 8,
        groomer_id= 7,
        date= '2023-01-09',
        time= '10:20'
    ),
    Booking(
        client_id= 1,
        groomer_id= 3,
        date= '2023-01-12',
        time= '11:35'
    )]

    db.session.add_all(clients)
    db.session.add_all(groomers)
    db.session.add_all(bookings)
    db.session.commit()
    print('Tables seeded!')

class ClientSchema(ma.Schema):
    class Meta: 
        fields = ('id', 'name', 'animal_type', 'breed', 'owner', 'phone')
        # ordered = True

class BookingSchema(ma.Schema):
    class Meta: 
        fields = ('id', 'client_id', 'groomer_id', 'date', 'time')
        ordered = True

class GroomerSchema(ma.Schema):
    class Meta: 
        fields = ('id', 'f_name', 'l_name', 'email', "phone")
        ordered = True

@app.route('/')
def index():
    return 'Welcome to Dog Spa'

@app.route('/bookings/')
def bookings():
    stmt = db.select(Booking)
    bookings = db.session.scalars(stmt)
    bookings_details = []
    for booking in bookings:
        booking_details = dict({'id': booking.id, 'date' : booking.date})
        bookings_details.append(booking_details)
    return bookings_details

@app.route('/booking/<int:booking_id>')
def booking_lookup(booking_id):
    stmt = db.select(Booking).filter_by(id = booking_id)
    bookings = db.session.scalars(stmt)
    return BookingSchema(many=True).dump(bookings)

@app.route('/bookings/groomer/<int:groomer_id>/')
def get_schedule(groomer_id):
    stmt = db.select(Booking).filter_by(groomer_id = groomer_id)
    schedule = db.session.scalars(stmt)
    return BookingSchema(many=True).dump(schedule)

@app.route('/add_groomer/', methods=['POST'])
def add_groomer():
    try: 
        groomer_info = GroomerSchema().load(request.json)
        new_groomer = Groomer(
            f_name = groomer_info['f_name'],
            l_name = groomer_info['l_name'],
            phone = groomer_info['phone'],
            email = groomer_info['email']
        )
        db.session.add(new_groomer)
        db.session.commit()
        return GroomerSchema().dump(new_groomer), 201
    except IntegrityError:
        return {"Error": "Email already in use"}, 409

@app.route("/add_client/", methods=["POST"])
def add_client():
    client_info = ClientSchema().load(request.json)
    new_client = Client(
        name = client_info['name'],
        animal_type = client_info['animal_type'],
        breed = client_info['breed'],
        owner = client_info['owner'],
        phone = client_info['phone']
    )
    db.session.add(new_client)
    db.session.commit()
    return ClientSchema().dump(new_client), 201

if __name__ == '__main__':
    app.run()