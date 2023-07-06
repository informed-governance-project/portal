# Governance platform - Portal

## Description

Portal for the
[Informed Governance project](https://github.com/informed-governance-project).

See more information about the architecture
[here](https://github.com/informed-governance-project/architecture#overview).


## Installation

### Prerequisites

Generally speaking, requirements are the following:
- A GNU/Linux distribution. Tested on Debian Bookworm;
- Python version >= 3.9. Tested with Python 3.11;
- A PostgreSQL server for persistent storage. Tested with PostgreSQL 15.3.


### Get the code and install the dependencies

```bash
$ git clone https://github.com/informed-governance-project/portal.git
$ cd portal
$ npm ci
$ poetry install --only main
```

### Configure the application

```bash
$ poetry shell

# Configure production settings:
$ cp portal/config_dev.py portal/config.py

$ python manage.py collectstatic

$ python manage.py migrate
```


## Usage

Two different interfaces are available. A command line interface and a Web based interface (API).

### Command line interface

Create a new module and a token access for an existing user:

```bash
$ python manage.py module_create --name monarc --path monarc --upstream http://127.0.0.1:5000/
New module created.

$ python manage.py access_create --username=john --module_name=monarc --token=SecureToken
New access created.
```

Revoke a user's access to a specified service:

```bash
$ python manage.py access_revoke --username=john --module_name=monarc
Access revoked.
```

### API

It is possible to create new accesses via the API. Below is an example:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/externaltoken/' \
  -H 'accept: application/json' \
  -H 'Authorization: Basic dG90bzpwYXNzd29yZA==' \
  -H 'Content-Type: application/json' \
  -H 'X-CSRFTOKEN: xj4Rk9PNbcavn5Sy3qSgnX2RzqepddKaxO3xyxyaKTxPueEuJ7QihevwJJjF2swa' \
  -d '{
  "username": "john",
  "module_name": "MONARC",
  "module_path": "monarc",
  "token": "SecureToken"
}'
```

Only an admin user is able to use this endpoint.

The user must already be in the database.

Revoke a user's access:

```bash
curl -X 'DELETE' \
  'http://127.0.0.1:8000/api/v1/externaltoken/5' \
  -H 'accept: */*' \
  -H 'Authorization: Basic dG90bzpwYXNzd29yZA==' \
  -H 'X-CSRFTOKEN: GmsOTMfZ2UbyyWRP25uxYY1cSDmvB3zEGRru7aYmBBySF5DLIMszSfuR2WrLqilE'
```


You can look at the documentation of the API:
http://127.0.0.1:8000/api/v1/swagger-ui/



## License

This software is licensed under
[GNU Affero General Public License version 3](https://www.gnu.org/licenses/agpl-3.0.html)
