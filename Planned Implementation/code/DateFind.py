import csv

import dateutil.parser
from itertools import chain
import re

import datetime
import time

# Add more strings that confuse the parser in the list
UNINTERESTING = set(chain(dateutil.parser.parserinfo.JUMP, 
                          dateutil.parser.parserinfo.PERTAIN,
                          ['a'],['<p>'],['</p>'],['&nbsp;'] ))

#open Clean version of Publication Request
reader = csv.DictReader(open("procPublicationRequest_Oct-Dec_2014_clean.csv"), delimiter=',')


def _get_date(tokens):
    for end in xrange(len(tokens), 0, -1):
        region = tokens[:end]
        if all(token.isspace() or token in UNINTERESTING
               for token in region):
            continue
        text = ''.join(region)
        try:
            date = dateutil.parser.parse(text, default=datetime.datetime(1900, 1, 1))
            return end, date
        except ValueError:
             pass
        except TypeError:
             pass
	except OverflowError:
             pass
			
def find_dates(text, max_tokens=50, allow_overlapping=False):
    tokens = filter(None, re.split(r'(\S+|\W+)', text))
    skip_dates_ending_before = 0
    for start in xrange(len(tokens)):
        region = tokens[start:start + max_tokens]
        result = _get_date(region)
        if result is not None:
            end, date = result
            if allow_overlapping or end > skip_dates_ending_before:
                skip_dates_ending_before = end
                yield date
		

fileobj = open("procPublicationRequest_Oct-Dec_2014_DateTimeExtract.csv", 'w')
print "Start Time " + time.strftime("%c")

try:
    fieldnames = ("RequestID","DateTimeValue")
    headers = dict( (n,n) for n in fieldnames )
    writer = csv.DictWriter(fileobj, delimiter=',', lineterminator='\n', fieldnames=headers)
    writer.writerow(headers)
    
    for row in reader:
        rowID = row["RequestID"]
        for date in find_dates(row["AdditionalDescription"], allow_overlapping=False):
            if date > datetime.datetime(1900, 12, 31):
                writer.writerow ({
                    'RequestID':rowID,
                    'DateTimeValue':date
                               })

finally:
    fileobj.close()
    print "End Time " + time.strftime("%c")
 
