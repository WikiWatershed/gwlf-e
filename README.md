# gwlf-e
Port of Generalized Watersheds Loading Functions - Enhanced (MapShed)

[![Build Status](https://travis-ci.org/WikiWatershed/gwlf-e.svg?branch=develop)](https://travis-ci.org/WikiWatershed/gwlf-e)

## Testing

Run `python setup.py test` from within the project directory.

To run a manual test againt the model output and the expected output from a known gms file, you can run `python compare_output.py` or `python compare_output.py results.json` from within the test directory.


## Deployments

Deployments to PyPi are handled through [Travis-CI](https://travis-ci.org/WikiWatershed/gwlf-e). The following git flow commands create a release using Travis:

``` bash
$ git flow release start 0.1.0
$ vim CHANGELOG.md
$ vim setup.py
$ git commit -m "0.1.0"
$ git flow release publish 0.1.0
$ git flow release finish 0.1.0
```

To kick off the deployment, you'll still need to push the local tags remotely
`git push --tags`

## License

This project is licensed under the terms of the Apache 2.0 license.
