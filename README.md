pybossa-z3950
*************

[![Build Status](https://travis-ci.org/alexandermendes/pybossa-z3950.svg?branch=master)]
(https://travis-ci.org/alexandermendes/pybossa-z3950)
[![Coverage Status](https://coveralls.io/repos/alexandermendes/pybossa-z3950/badge.svg)]
(https://coveralls.io/github/alexandermendes/pybossa-z3950?branch=master)

A PyBossa plugin for [Z3950](https://en.wikipedia.org/wiki/Z39.50) integration.

The plugin imports and initialises [Flask-Z3950](https://github.com/alexandermendes/Flask-Z3950),
making use of the default view functions to implement Z39.50 search capabilities. Some additional
functionality is added to allow you to easily integrate those search capabilities into your
PyBossa projects.


## Installation

Firstly, install some required development packages:

```
sudo apt-get install libxml2-dev libxslt-dev python-dev lib32z1-dev
```

Now, install pybossa-z3950, copy the [pybossa_z3950](pybossa_z3950)
folder into your PyBossa [plugins](https://github.com/PyBossa/pybossa/tree/master/pybossa/plugins)
directory and reboot the PyBossa server:

```
git clone https://github.com/alexandermendes/pybossa-z3950.git
cd pybossa-z3950
python setup.py install
cp -r pybossa_z3950 /home/pybossa/pybossa/plugins
# Now Restart your server
```


## Configuration

The configuration variables can be added to your main PyBossa configuration file:

|     Setting     |                  Purpose              |
|-----------------|---------------------------------------|
| Z3950_DATABASES | Z39.50 database configuration details |


Refer to the [Flask-Z3950 documentation](https://pythonhosted.org/Flask-Z3950/#configuration)
for more details.


## Usage

The plugin sets up an API that can be used to search databases via the Z39.50 protocol.
Results can be returned in MARCXML, JSON, HTML, or as raw data. For details about
how this API works refer to the [Flask-Z3950 documentation](https://pythonhosted.org/Flask-Z3950/).
By default, the API endpoints are located at:

```
GET /z3950/search/<db>/marcxml
GET /z3950/search/<db>/json
GET /z3950/search/<db>/html
GET /z3950/search/<db>/raw
```


## Testing

Just run the following command:

```
$ python setup.py test
```


## Contributing

For guidelines on how to suggest improvements, report bugs or submit pull
requests see the
[CONTRIBUTING](https://github.com/alexandermendes/Flask-Z3950/blob/master/CONTRIBUTING.md) file.
