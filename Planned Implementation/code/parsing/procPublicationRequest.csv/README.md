# Summary
Todo...


## Pro tips for viewing ipython notebooks

* Installing the appropriate [extension](http://jiffyclub.github.io/open-in-nbviewer/) for your browser
   will give you a button to render and view any .ipynb files from github.

## DCAS Database Sample data:

1. [procPublicationRequestDMSSPortal Oct-Dec 2014.csv](http://goo.gl/mh67qm). This CSV has extra
   column fields for procurement content.
        
2. [procPublicationRequest Oct-Dec 2014 (2).csv](http://goo.gl/P7QP4H)
     

## Status

These are the different types of messages and their count that needs to be parsed.

AgencyName                                  | TypeOfNoticeDescription   | Message Count                          | Status
--------------------------------------------|--------------|------------|----------------------------------------|-----------------------------
Mayor's Office of Contract Services         | Notice                    |         64     | wip - Initial Parse. Needs Schema work
Mayor's Office of Contract Services         | Meeting                   |         3      | wip - Poorly structured source -- this will be difficult to parse. Argues the case for intervention at DCAS input/entry system.
Citywide Administrative Services            | Solicitation              |         101     | wip - Maybe no parsing needs to be done. Are the columns themselves enough to construct the schema?

