Hi, this started as my personal project for practicing the lession. It is neither perfect or complete. Feel free to use your own solutions.

1. After cloning the repo, install all the requirements in Requirements.txt.
2. Create a PostgreSQL database for this exercise and connect to it.
3. Then go back to the virtual environment and 
type in the terminal the below command to create and seed your tables.

``` flask create && flask seed```


There are 3 tables: clients, groomers and bookings in the database and they look like this:
![tables in the database](docs/dog_spa%20tables.png)

## Questions:

1. Print all clients' names and what type of animal they are
2. Return owner of Archie
3. Return the owners of Smoke and Kookoo
4. Return the clients' names and owners of 'oodle' dogs
5. Return all distinct animal_types
6. Print all the owners of clients
7. Count all the human clients
8. Return the name of owner(s) who owns the most pets as clients.