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
   
stmt = db.select(Client.owner, db.func.count(Client.id)).select_from(Client).group_by(Client.owner).order_by(db.func.count(Client.id).desc()).limit(2) 

clients = db.session.execute(stmt).all() 

[print(client) for client in clients]
*Note: have to use db.session.execute()
