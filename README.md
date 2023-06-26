# Governance platform

## Description

Portal for the Informed Governance project.
See more information about the architecture
[here](https://github.com/informed-governance-project/architecture#overview).


## Installation

### Get the code and install the dependencies

```bash
$ git clone https://github.com/informed-governance-project/proxy.git
$ cd proxy
$ npm ci
$ poetry install --only main
```

### Configure the application

```bash
$ poetry shell

# Configure production settings:
$ cp proxy/config_dev.py proxy/config.py

$ python manage.py collectstatic

$ python manage.py migrate
```


## Usage

Two different interfaces are available. A command line interface and a Web based interface (API).

### Command line interface

Create a new access to a module for an authenticated user:

```bash
$ python manage.py create_access --username=john --module_name=monarc --module_path=monarc --token=SecureToken
New access created.
```

Revoke a user's access to a specified service:

```bash
$ python manage.py revoke_access --username=john --module_name=monarc
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

You can look at the documentation of the API:
http://127.0.0.1:8000/api/v1/swagger-ui/



## License

This software is licensed under
[GNU Affero General Public License version 3](https://www.gnu.org/licenses/agpl-3.0.html)
