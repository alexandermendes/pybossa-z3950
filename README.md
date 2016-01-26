# pybossa-z3950

[![Build Status](https://travis-ci.org/alexandermendes/pybossa-z3950.svg?branch=master)]
(https://travis-ci.org/alexandermendes/pybossa-z3950)
[![Coverage Status](https://coveralls.io/repos/alexandermendes/pybossa-z3950/badge.svg)]
(https://coveralls.io/github/alexandermendes/pybossa-z3950?branch=master)

A [PyBossa](https://github.com/PyBossa/pybossa) plugin that uses [Flask-Z3950](https://github.com/alexandermendes/Flask-Z3950) to provide [Z39.50](https://en.wikipedia.org/wiki/Z39.50) integration.


## Installation

Install the required development packages:

``` bash
sudo apt-get install libxml2-dev libxslt-dev python-dev lib32z1-dev
```

Install pybossa-z3950, remembering to **activate your virtual environment**:

``` bash
git clone https://github.com/alexandermendes/pybossa-z3950
cd pybossa-z3950
source /home/pybossa/pybossa/env/bin/activate
python setup.py install
```

Copy the [pybossa_z3950](pybossa_z3950) folder into your PyBossa
[plugins](https://github.com/PyBossa/pybossa/tree/master/pybossa/plugins) directory:

``` bash
cp -r pybossa_z3950 /home/pybossa/pybossa/pybossa/plugins
```

The plugin will be available after you next restart the server.


## Configuration

You can provide Z39.50 database configuration details by adding the following
variable to your main PyBossa configuration file:

``` Python
Z3950_DATABASES = ["loc": {"db": "Voyager", "host": "z3950.loc.gov", "port": 7090}]
```

The example above is enough to allow you to search to the Library of Congress
database. See the [Flask-Z3950 documentation](https://pythonhosted.org/Flask-Z3950/#configuration)
for more details.


## HTTP API

The API provided by this plugin can be used to search databases via the Z39.50 protocol and
retrieve results as JSON, HTML, MARCXML or raw string data.

By default, the API endpoints are located at:

``` HTTP
GET /z3950/search/<db>/marcxml
GET /z3950/search/<db>/json
GET /z3950/search/<db>/html
GET /z3950/search/<db>/raw
```

See the [Flask-Z3950 documentation](https://pythonhosted.org/Flask-Z3950/#http-api)
for full details.


## Testing

This plugin makes use of the PyBossa test suite while running tests. The
[Travis CI configuration file](.travis.yml) contains all of the required commands to set
up a test environment and run the tests.


## Contributing

See the [CONTRIBUTING](CONTRIBUTING.md) file for guidelines on how to suggest improvements,
report bugs or submit pull requests.
