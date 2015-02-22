import csv
import os
import sys
import re

from bs4 import BeautifulSoup
from ftfy import fix_text

ADDITIONAL_DESCRIPTION_TAGS = ['&nbsp;']

URL_REGEX = re.compile(r'\b(([\w-]+://?|www[.])[^\s()<>]+(?:\([\w\d]+\)|([^[:punct:]\s]|/)))')

def cleanup_tags(string, tags=ADDITIONAL_DESCRIPTION_TAGS):
    """
    Remove unhelpful tags from an input string; this is a very naive form of cleanup,
    and tags will probably be very helpful with some of the future tasks, but gotta
    start somewhere. It also converts to unicode and fixes html entities.
    """
    mystring = string
    for tag in tags:
        mystring = mystring.replace(tag,'')
    mystring = fix_text(mystring) #Transforms escaped characters into normal ones, ideally
    return mystring


def read_csv_to_dict(filename):
  if not os.path.isfile(filename):
    sys.exit(MISSING_FILE_ERROR.format(os.path.basename(filename), filename))

  list_of_dicts = []
  with open(filename, 'rU') as f:
    csv_reader = csv.DictReader(f)
    for line in csv_reader:
      list_of_dicts.append(line)

  return list_of_dicts


def extract_links(string):
  """
  Extracts all the links by looking through link tags and urls just floating around
  with no tag. Then normalizes links, removes duplicates and splits them up between
  urls and emails.
  """
  links = []
  for link in BeautifulSoup(string).find_all('a'):
    links.append(link.get('href'))
  string_wo_link_tags = BeautifulSoup(string).text
  links.extend([link[0] for link in URL_REGEX.findall(string_wo_link_tags)])

  urls = []
  emails = []
  for link in links:
    if '@' in link:
      emails.append(link.strip('mailto:'))
      continue
    elif not link.startswith('http'):
      link = 'http://' + link
    urls.append(link)

  return list(set(urls)), list(set(emails))


def extract_urls(filename):
  crol_doc = read_csv_to_dict(filename)

  for row in crol_doc:
    description = row["AdditionalDescription"]
    cleaned_description = cleanup_tags(description)

    urls, emails = extract_links(cleaned_description)
    
    if len(urls) != 0 or len(emails) != 0:
      print(urls, emails)


extract_urls('procPublicationRequest_Oct-Dec_2014_clean.csv')