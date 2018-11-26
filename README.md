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
# remember to update your database credentials here: https://github.com/pvthuyen/vietai_judge/blob/0818b61c51935f60987b75852b90c575958dd840/vietai_judge/settings.py#L78
ALTER ROLE vietai SET client_encoding TO 'utf8';
ALTER ROLE vietai SET default_transaction_isolation TO 'read committed';
ALTER ROLE vietai SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
\q
```
- Run the project in development mode: `python manage.py runserver`
