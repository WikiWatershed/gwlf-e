# gwlf-e
Port of Generalized Watersheds Loading Functions - Enhanced (MapShed)

## Installation

Install using `pip`:

```bash
$ pip install gwlf-e
```

## Development

Ensure you have Python 3.10 and [pipenv](https://pipenv.pypa.io/en/latest/) available. Then run:

```bash
$ pipenv sync
```

### Running Locally

```bash
$ pipenv run ./run.py --json test/integrationtests/input_4_output.json test/integrationtests/input_4.gms
```

### Testing

```bash
$ pipenv run nosetests
```

## Deployments

Create a new release using git flow:

```console
$ git flow release start 3.0.0
$ vim CHANGELOG.md
$ vim setup.py
$ git add CHANGELOG.md setup.py
$ git commit -m "3.0.0"
$ git flow release finish -p 3.0.0
```

When the tag is pushed up, [GitHub Actions](./.github/workflows/release.yml) will publish a release to PyPI.

## License

This project is licensed under the terms of the Apache 2.0 license.
