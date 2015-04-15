# City Record Parsing
Building a pipeline between the internal City Record data structure and the optimized public notice schema.


## Status

Finalizing end-to-end MVP parsing libraries


## Roadmap

Create a parsing pileline to fascilitate incremental progress, where the
output from the first parse will be consumed by the second parsing effort.

Current Parse effort is to breakdown the records trying to match as many desired output schema
in text format (no parsing dates, street names, dollar amounts, etc)

Future steps would be to incorporate NER extraction for person and entities streetnames,

## Getting Started

We're using iPython notebooks to share our work as we break down the large ProProcPublicationRequest.csv 
into smaller portions. Each notebook in the [ProcPublicationRequest.csv](https://github.com/CityOfNewYork/CROL-PDF/tree/master/Planned%20Implementation/code/parsing/procPublicationRequest.csv)
folder breaks out one notice type of one Agency to parse for salient key value paris. 

##Tools
- Python 3.4.3
- iPython - A command shell for interactive computing
- iPython Notebook - .ipnyb file type, launches locally in Jupyter or online in nbViewer. Allows you to view and edit ipython scripts with explanitory text.

### Installation

These instructions have not been tested on windows --  If you're able to get your
windows machine up to speed with these requirements, please document it here for the
next cool civic hacker.

You'll need the following:

- Linux, BSD, or MacOSX machine
- Python 3.4.3
- `virtualenv` or `virtualenvwrapper` (in order to install requirements without
  using `sudo`

1. You will have to install Python3 on your system in order to install it 
   to virtual environment. Get Python3 [here](https://www.python.org/downloads/)

2. Make the Python3 virtual environment:

        mkvirtualenv --python `which python3` --no-site-packages crow-parsing
        workon crow-parsing

3. Within the virtualenv, install the requirements:

        pip3.4 install -r requirements.txt

4. Now, with iPython insallted you may view all notebooks in the directory using:

        ipython notebook

