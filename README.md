# gwlf-e
Port of Generalized Watersheds Loading Functions - Enhanced (MapShed)

[![Build Status](https://travis-ci.org/WikiWatershed/gwlf-e.svg?branch=develop)](https://travis-ci.org/WikiWatershed/gwlf-e)

## Installation

Install using `pip`. Ensure `numba` is installed first:

```bash
$ pip install numba==0.38.1
$ pip install gwlf-e
```

## Testing

Run `python setup.py test` from within the project directory.

To run a manual test againt the model output and the expected output from a known gms file, you can run `python compare_output.py` or `python compare_output.py results.json` from within the test directory.


## Deployments

Deployments to PyPi are handled through [Travis-CI](https://travis-ci.org/WikiWatershed/gwlf-e). The following git flow commands create a release using Travis:

``` bash
$ git flow release start 0.1.0
$ vim CHANGELOG.md
$ vim setup.py
$ git add CHANGELOG.md setup.py
$ git commit -m "0.1.0"
$ git flow release publish 0.1.0
$ git flow release finish 0.1.0
```

After you've completed the `git flow` steps, you'll need to push the changes from your local `master` and `develop` branches back to the main repository.

```bash
$ git checkout develop
$ git push origin develop
$ git checkout master
$ git push origin master
# Trigger PyPi deployment
$ git push --tags
```

## License

This project is licensed under the terms of the Apache 2.0 license.
