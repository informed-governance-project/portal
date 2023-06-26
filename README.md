# Governance platform


## Description

- portal for the Informed Governance project;
- management of users permissions;



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
