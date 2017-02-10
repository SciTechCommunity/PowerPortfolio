# PowerPortfolio
![alt text][logo]

[logo]: https://img.shields.io/badge/License-MIT-yellow.svg "Logo Title Text 2"
A CSST project open to the public!

###To be created:
- Landing page
- Projects page
- Contact page
- Backend
- Styling

###Specializations that are a bonus:
- Any kind of HTML/CSS
- Python 3
- Jquery
- sqlalchemy
- flask
- bcrypt

The Power Portfolio is a free to use template created by the Tumblr Community / CSST team.

###Running PowerPortfolio on local Server

For development purposes you can run PowerPortfolio on a local server by doing the following:

 1. Create a virtual enviroment named venv
 
 ```
 python3 -m venv venv
 ```
 2. Activate the virtual enviroment:
 
 Windows:
 ```
 venv\Scripts\activate.bat
 ```
 
 \*nix:
 ```
 source venv/bin/activate
 ```
 3. The first time you run PowerPortfolio do:
 
 ```
 pip install -e .
 ```
 
 4. To run the app do:
 
 ```
 python -m portfolio
 ```

### Running Test
To run a test, first open 
```settings.cfg``` 
and change the DATABASE url to a testing database. 

Next run
```
python test.py
```

To move out of testing mode, change DATABASE in settings.cfg to the appropiate url.  
