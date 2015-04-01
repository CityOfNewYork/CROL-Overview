# City of Record Parsing

Make NYC's Notifications accessible

## Status

We are making grand plans.


## Roadmap

Create a parsing pileline to fascilitate incremental progress, where the
output from the first parse will be consumed by the second parsing effort.

Current Parse effort is to breakdown the records trying to match as many desired output schema
in text format (no parsing dates, street names, dollar amounts, etc)

Future steps would be to incorporate NER extraction for person and entities streetnames,


## Installation

You'll need the following:

- Linux, BSD, or MacOSX machine
- Python 3.4.3
- `virtualenv` or `virtualenvwrapper` (in order to install requirements without
  using `sudo`

### Python 3 installation

These instructions have not been tested on windows --  If you're able to get your
windows machine up to speed with these requirements, please document it here for the
next cool civic hacker.

1. You will have to install Python3 on your system in order to install it 
   to virtual environment. Get Python3 [here](https://www.python.org/downloads/)

2. Make the Python3 virtual environment:

        mkvirtualenv --python `which python3` --no-site-packages crow-parsing
        workon crow-parsing

3. Within the virtualenv, install the requirements:

    pip3.4 install -r requirements.txt