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



## License

This software is licensed under
[GNU Affero General Public License version 3](https://www.gnu.org/licenses/agpl-3.0.html)
