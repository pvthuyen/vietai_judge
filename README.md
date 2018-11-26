# vietai_judge
## Prerequisites
| Python | PostgreSQL |
|-------|-------|
| 3.6.5 | 10 |

## Setup
It's best if you setup everything under a virtual envinronment so that it does not conflict with other Python's dependencies.

- Install requirements: `pip install -r requirements.txt`
- Log into an interactive Postgres session: `sudo -u postgres psql`
- Create a new database for the project:
```
CREATE DATABASE vietai_judge;
CREATE USER vietai WITH PASSWORD '******';
ALTER ROLE vietai SET client_encoding TO 'utf8';
ALTER ROLE vietai SET default_transaction_isolation TO 'read committed';
ALTER ROLE vietai SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
\q
```
- Run the project in development mode: `python manage.py runserver`
