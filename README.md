# Flask Dropbox OAuth Example

This project is a simple example of how to setup Dropbox OAuth in Flask projects.  

## Getting Started

1. Clone a copy of this repository
2. Change your upstream with `git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git`
3. Setup a virtual environment with `python3 -m venv env`
4. Activate the virtual environment with `source env/bin/activate`
5. Install the project dependencies with `pip install -r requirements.txt`
6. Add the following to the config.py file:
* Dropbox App Key
* Dropbox App Secret Key
7. Ensure that `http://localhost:5000/dropbox-authenticate-finish` is added as a redirect URI for your dropbox app.
8. Run the app with `heroku local` or `flask run`
9. Navigate to http://localhost:5000/authenticate
10. This will start the oauth process by redirecting you to dropbox!

### Prerequisites

* Python 3
* [Heroku Command Line](https://devcenter.heroku.com/categories/command-line) (optional)

## Running the tests

* Coming soon.

## Deployment

* Coming soon.

## Built With

* [Flask](http://flask.pocoo.org/)

## Authors

* **Salvatore Tosti** - *Initial work* - [SalvatoreTosti](https://github.com/SalvatoreTosti)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
