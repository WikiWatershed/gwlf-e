# gwlf-e
Port of Generalized Watersheds Loading Functions - Enhanced (MapShed)

## Testing

Run `python setup.py test` from within the project directory.


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
