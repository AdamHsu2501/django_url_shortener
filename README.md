# django_url_shortener

![](https://i.imgur.com/eoURQfT.png)

URL Shortener Application
* Create a new URL from the URL inputed by users, then save URLs to database
* Redirect the original URL when user input new URL at address bar, and update usage times

<!-- GETTING STARTED -->
## Getting Started
### Prerequisites

* Python    
    1. [Install Python](https://www.python.org/)
    2. cmd:
        ```
        pip install pipenv
        ```

### Installation
Open cmd and follow the steps below
1. Clone the repo
   ```
   git clone https://github.com/AdamHsu2501/django_url_shortener.git
   ```
2. Into folder
   ```
   cd django_url_shortener
   ```
3. Install virtual environment
   ```
   pipenv install
   ```
4. Run virtual environment
   ```
   pipenv Shell
   ```
5. Into url_shortener folder
   ```
   cd url_shortener
   ```
6. Run server
   ```
   python manage.py runserver
   ```
7. Open broswer with http://127.0.0.1:8000/ 
