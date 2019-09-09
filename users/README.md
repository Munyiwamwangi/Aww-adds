# Accolade

 ##Author: Munyi Mwangi

This is a web app that allows user to post their projects and have them rated based on design,usability and content.

## Project Approach

| Given       | Action       | Result  |
| ------------- |:-------------:| -----:|
| User wants to view a project and its details | They click on a project tile | They are redirected to the project's page with it's details listed |
| User wants to post a project | Given they are sign up, the enter the project's details and submit | The projects published for others to see  |
| User wants to rate other users' projects | They select the project and give the ratings for three categories  | The ratings are posted and an average returned |
| User wants to search for a project |  They enter the project's title in the search bar | They are redirected to a page with the search results |

## Getting Started

* Fork the repository
* Git clone the project to your local machine
* Set up a virtual environment in the project folder

* python3.6 -m venv --without-pip virtual

## Installing

Ensure that the MODE in the .env is set to development ('dev'), which will automatically set debug to true.
Now run the following command

python3.6 manage.py runserver

And view the site at the port provided which is most likely 127.0.0.1:8000

## Running the tests

To run the automated tests for this system, run the following command

python3.6 manage.py test album

## Deployment

To deploy on heroku:

* Have a Procfile in the project root;
* Update requirements.txt file with all the requirements in the project root;
* Have Gunicorn to requirements.txt;
* Have runtime.txt to specify the correct Python version in the project root;
* Ensure configuration whitenoise to serve static files.
* Add a heroku remote by logging in
* Configure all the settings in .env on heroku (set MODE to 'prod' on heroku)
* git push to heroku
* git push database and migrate to heroku server

## Technologies used

* Python3.6
* Django Web Framework
* Bootstrap4

## Versioning

Find all the versions used in the requirements.txt or run the following command to confirm:
```
pip freeze
```
### License 
MIT License
Copyright (c) 2019 Sarah Munini
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
Collapse



