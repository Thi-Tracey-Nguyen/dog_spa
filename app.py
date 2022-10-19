from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_marshmallow import Marshmallow
from datetime import date, timedelta
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://tracey:123456@127.0.0.1:5432/dog_spa'
app.config['JSON_SORT_KEYS'] = False
app.config['JWT_SECRET_KEY'] = 'something secure'

db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

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

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, default = 'user')
    email = db.Column(db.String, nullable = False, unique=True)
    password = db.Column(db.String, default = bcrypt.generate_password_hash('user123').decode('utf8'))
    is_admin = db.Column(db.Boolean, default = False)

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

    admin = User(
        name = 'admin',
        email = 'admin@dog_spa.com',
        password = bcrypt.generate_password_hash('admin123').decode('utf8'),
        is_admin = True
        )

    # add groomers into users table with default name = user, password = user123 and is_admin is false
    users = []
    for groomer in groomers:
        user = User(
            email = groomer.email
        )
        users.append(user)

    db.session.add_all(clients)
    db.session.add_all(groomers)
    db.session.add_all(bookings)
    db.session.add_all(users)
    db.session.add(admin)
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

# class UserSchema(ma.Schema):
#     class Meta:
#         fields = ('name', 'password')

def authorize():
    user_id = get_jwt_identity()
    stmt = db.select(User).where(User.id == user_id)
    user = db.session.scalar(stmt)
    return user.is_admin

@app.route('/')
def index():
    return 'Welcome to Dog Spa'

@app.route('/bookings/')
@jwt_required()
def bookings():
    if authorize():
        stmt = db.select(Booking)
        bookings = db.session.scalars(stmt)
        return BookingSchema(many=True).dump(bookings)
    else: 
        return {"Error": "Access denied"}, 403

@app.route('/booking/<int:booking_id>')
def booking_lookup(booking_id):
    stmt = db.select(Booking).filter_by(id = booking_id)
    bookings = db.session.scalar(stmt)
    return BookingSchema().dump(bookings)

@app.route('/bookings/groomer/<int:groomer_id>/')
def get_schedule(groomer_id):
    stmt = db.select(Booking).filter_by(groomer_id = groomer_id)
    schedule = db.session.scalars(stmt)
    return BookingSchema(many=True).dump(schedule)

@app.route('/auth/add_groomer/', methods=['POST'])
@jwt_required()
def add_groomer():
    if authorize():
        try: 
            groomer_info = GroomerSchema().load(request.json)
            new_groomer = Groomer(
                f_name = groomer_info['f_name'],
                l_name = groomer_info['l_name'],
                phone = groomer_info['phone'],
                email = groomer_info['email'],
            )
            new_user = User(
                email = request.json['email'],
            )
            db.session.add(new_groomer)
            db.session.add(new_user)
            db.session.commit()
            return GroomerSchema().dump(new_groomer), 201
        except IntegrityError:
            return {"Error": "Email already in use"}, 409
    else:
        return {"Error": "No permission"}, 403

@app.route("/auth/add_client/", methods=["POST"])
@jwt_required()
def add_client():
    #extract user's id out of the token so identify them
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id = user_id)
    user = db.session.scalar(stmt)
    if not user.is_admin:
        return {'Error': 'Unauthorized action'}, 404

    new_client = Client(
        name = request.json['name'],
        animal_type = request.json['animal_type'],
        breed = request.json['breed'],
        owner = request.json['owner'],
        phone = request.json['phone']
    )
    db.session.add(new_client)
    db.session.commit()
    return ClientSchema().dump(new_client), 201
        

@app.route('/auth/login/', methods=['POST'])
def login():
    stmt = db.select(User).where(User.email == request.json["email"])
    user = db.session.scalar(stmt)
    if user and bcrypt.check_password_hash(user.password, request.json['password']):
        token = create_access_token(identity=user.id, expires_delta = timedelta(days=1))
        return {"message": f"Log in successfully as {user.name}", "token": token}
    else:
        return {'message': 'Invalid username or password'}

# @app.route('/auth/new_user/', methods=['POST'])
# def new_user():
#     new_user = User(
#         name = request.json['name'],
#         password = bcrypt.generate_password_hash(request.json['password']).decode('utf8')
#     )
#     db.session.add(new_user)
#     db.session.commit()

#     return UserSchema(exclude=['password']).dump(new_user)

if __name__ == '__main__':
    app.run()