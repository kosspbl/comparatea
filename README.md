<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/kosspbl/comparatea/blob/main/static/comparatea-light.png">
  <img alt="Comparatea logo" src = "https://github.com/kosspbl/comparatea/blob/main/static/comparatea-dark.png" height = "130px" >
</picture>

Python, Html & CSS web scraping project to compare products on different e-commerce websites and display them on our own website.

## Setup
In setup, you have to install Flask & BeautifulSoup. Set up a virtual environment having all the required dependencies. Everything is explained on the Flask website :arrow_down:

<a href="https://flask.palletsprojects.com/en/2.2.x/installation/"><img src = "https://user-images.githubusercontent.com/89385145/231574201-a823f3ec-ff4b-47f0-9677-6eb74c020cfd.png" height = "300px"></a>

## Requirements : 
Here is quick setup in Windows and Linux/Mac os . First go to any desired directory : 
```
git clone https://github.com/kosspbl/comparatea
```
```
cd comparatea
```
Now we have successfully cloned the directory on our local system.
After this let's create a virtual environment to install all the python libraries.

- On Linux/ Mac OS:
```
python3 -m venv venv
. venv/bin/activate
```
- On Windows
```
py -3 -m venv venv
venv\Scripts\activate
```
N
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
