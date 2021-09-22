## To use this APP

go to the folder sicei in bash and write:

``` docker-compose build ```

then write:

``` docker-compose up -d ```

if the bash show error of connection to the DB pause the container and change the .env file in DB_HOST to 'sicei', save and run the container if the problem persist come back the 'sicei_db' value, save and run the container.

if you want to see the student endpoint go to

http://127.0.0.1:8000/api/student/