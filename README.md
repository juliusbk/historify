Historify
=========

To get up and running make sure you have Python 2.7 and pip installed. We also need libjpeg for PIL. You probably already have this, but if PIL won't compile, install this. On ubuntu, e.g., do

> pip uninstall PIL

> sudo apt-get install libjpeg8-dev

> pip install PIL

For all other requirements do

> pip install -r requirements.txt

in the main directory.

To run the app go to the webservice folder and do

> python app.py

The rest should be easy. Note that the app only takes jpegs, and the url cannot contain unicode, so only 0-9 and a-z in the url!
