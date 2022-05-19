CREATE USER pkg_app WITH PASSWORD 'password' CREATEDB;
CREATE DATABASE pkg_db WITH OWNER pkg_app;


pipenv install alembic Flask-Migrate

pipenv run flask db init
pipenv run flask db migrate -m "create packages table"
pipenv run flask db upgrade
