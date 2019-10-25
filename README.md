# Project
Minute Pitch 

## Author
[Ali Kheir](https://github.com/AliKheirAbdi)

## Author Contact details
* Email: akheirali(@)gmail.com


## Project Description
A Flask application that helps In life, you only have 60 seconds to impress someone.This app allows a user to submit an idea pitch.
## Screenshot
![image](https://github.com/AliKheirAbdi/pitchit/blob/master/app/pitchapp.png)

## Set up instructions
1. You need to have python3.7 installed, venv and pip
2. Set up the virtual environment and activate it.

    
    $ python3.7 -m venv virtual


    $ source virtual/bin/activate


3. Install all modules required

    $ pip install flask


    $ pip install flask-bootstrap


    $ pip install flask-script

4. Create an instance folder ```mkdir instance``` in the root directory and navigate to it ```cd instance```
5. Create a config.py file in the instance folder ```touch config.py```
6.Run manage.py to Launch in the server to view the application

## Development
Want to contribute? Great!
* Fork the repo
* Clone the repo in your machine but ensure you have all the necessary modules.(You can find them in the set up instructions above)
```https://github.com/AliKheirAbdi/pitchit.git```
* Create a new branch ```git branch contributions```
* Edit your changes in your branch
* Run the application

### Known bugs
The comment box is not working.
User welcome email not set up

## Technologies used
Python3.7
Bootstrap

## BDD
| Input        | Output           | Behavior  |
| ------------- |:-------------:| -----:|
| Click Register      | Fill out the reg form | user is created |
| Click Login     | Enter username and pwd   | Application logs user in |
| Submit Pitch| User fills out the form and submits | The new pitch is posted|
| Delete Pitch| Modal popup with the del button | The new pitch is posted| Appears on the home page
| Click Account| User bio is populated | User can edit their username and pwd|




# License
MIT license
