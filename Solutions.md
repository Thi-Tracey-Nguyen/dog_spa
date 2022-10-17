Solutions

1. 
stmt = db.select(Client) 

clients = db.session.scalars(stmt) 

[print(client.name, client.breed) for client in clients]



2.
stmt = db.select(Client).where(Client.name == 'Archie') 

client = db.session.scalar(stmt) 

print(client.owner)



3.
stmt = db.select(Client).where(db.or_(Client.name == 'Smoke', Client.name == 'Kookoo')) 

clients = db.session.scalars(stmt).all() 

[print(client.name, client.owner) for client in clients]



4.
stmt = db.select(Client).where(Client.breed.like("%oodle")) 

clients = db.session.scalars(stmt).all() 

[print(client.name, client.owner) for client in clients]

5.
stmt = db.select(Client.animal_type).distinct() 

clients = db.session.scalars(stmt).all()

[print(client) for client in clients]

6.
stmt = db.select(Client.owner).distinct() 

clients = db.session.scalars(stmt).all() 
[print(client) for client in clients]

7. 
distinct = db.select(Client.owner).distinct()

stmt = db.select(db.func.count()).select_from(distinct) 

clients = db.session.scalars(stmt).all() 

[print(client) for client in clients]


8. Only fingure out Psql so far, not alchemy yet. 

select owner, max(number_of_pets) from human_clients, (select max(number_of_pets) m from human_clients) max_pet where number_of_pets = max_pet.m group by owner;

==> need to convert it into SQLAlchemy syntax somehow
