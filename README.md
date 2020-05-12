# swiftOrg (API)


## Endpoints

All requests must be made to the base url: ``https://young-bayou-32734.herokuapp.com/`` (e.g: https://young-bayou-32734.herokuapp.com/all). You can try them out in your browser to further inspect responses.

Getting all entries:
```http
GET /all
```
```json
{"feed":{"feed":{"@xmlns":"http://www.w3.org/2005/Atom","entry":[{"author":{"name"}
````

## License

The data is available to the public strictly for educational and academic research purposes.

## Prerequisites

You will need the following things properly installed on your computer.

* [Python 3](https://www.python.org/downloads/) (with pip)
* [Flask](https://pypi.org/project/Flask/)
* [pipenv](https://pypi.org/project/pipenv/)

## Installation

* `git clone https://github.com/ihartsimafeichyk/swiftorgrss_json`
* `cd swiftorgrss_json`
* `pipenv shell`
* `pipenv install`

## Running / Development

* `flask run`
* Visit your app at [http://localhost:5000](http://localhost:5000).
