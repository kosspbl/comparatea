# comparatea
Python web scraping project to compare e-commerce websites and display them on a website.

## Setup
In setup, you have to install flask and set up a virtual environment having all the required dependencies. Everything is explained on the Flask website :

<a href="https://flask.palletsprojects.com/en/2.1.x/installation/#python-version"><img src="https://flask.palletsprojects.com/en/2.1.x/_static/flask-icon.png"></a>
- Requirements : 
Here is quick setup in linux / mac os. First go to any desired directory : 
```
git clone https://github.com/kosspbl/comparatea
```
```
cd comparatea
```
Now we have successfully cloned the directory on our local system.
After this let's create a virtual environment to install all the python libraries.

```
python3 -m venv venv
```
```
. venv/bin/activate
```
Now we can install all the dependencies / libraries.
```
pip install Flask bs4 requests lxml
```
- Running :
Simply run the app.py python file...
```
python3 app.py
```
That's it! Now the web application would be deployed on your local server.
