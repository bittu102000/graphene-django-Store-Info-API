## Directory Format
env  graph_ql  Readme.txt  requirement.txt   schema.txt(for all queries used in this API)



source env/bin/activate       //for Linux
env\Scripts\activate          //for Windows


## Install requirements for the project


pip install -r requirements.txt

## You can check for following dependencies installed in your environment using the following command

pip freeze

## aniso8601==7.0.0
## asgiref==3.4.1
## Django==3.2.8
## graphene==2.1.9
## graphene-django==2.15.0
## graphql-core==2.3.2
## graphql-relay==2.0.1
## promise==2.3
## pytz==2021.3
## Rx==1.6.1
## singledispatch==3.7.0
## six==1.16.0
## sqlparse==0.4.2
## text-unidecode==1.3

cd graph_ql
ls/--or--/dir
## db.sqlite3  graph_ql  manage.py  my_app
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
'''
Starting development server at http://127.0.0.1:8000/
''''
## Open your browser and copy the above link from terminal/cmd to browser as

http://127.0.0.1:8000/graphql
## You will then interact with Frontend as GraphiQL where you can run your Queries

## For accessing the database you can use http://127.0.0.1:8000/admin
## Username : bittu
## password : singh



