Contributions are welcome and there are many ways to participate to the
project. You can contribute by:

- reporting bugs;
- suggesting enhancements or new features;
- improving the documentation.

Feel free to fork the code, play with it, make some patches and send us pull requests.

Before starting to contribute please install the Git hook scripts:

```bash
$ git clone https://github.com/informed-governance-project/portal
$ cd portal/
$ poetry install
$ pre-commit install
```

There is one main branch: what we consider as stable with frequent updates as
hot-fixes.

Features are developed in separated branches and then regularly merged into the
main stable branch.

If your contribution require some documentation changes, a pull-request in order
to update the documentation is strongly recommended.

Please, do not open directly a GitHub issue if you think you have found a
security vulnerability. See our
[security policy](https://github.com/informed-governance-project/portal/security/policy)
page.

[Flask](https://flask.palletsprojects.com) is used for the backend.
Please use [black](https://github.com/psf/black) for the syntax of your Python code.
