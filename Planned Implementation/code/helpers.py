from ftfy import fix_text
from bs4 import BeautifulSoup

ADDITIONAL_DESCRIPTION_TAGS = ['&nbsp;']

def cleanup_tags(string, tags=ADDITIONAL_DESCRIPTION_TAGS):
    """
    Remove unhelpful tags from an input string; this is a very naive form of cleanup,
    and tags will probably be very helpful with some of the future tasks, but gotta
    start somewhere. It also converts to unicode and fixes html entities.
    """
    #make this capable of being used with .apply to a column with nans
    if type(string) == float:
        return string
    mystring = string
    if type(mystring) != unicode:
        mystring = mystring.decode('utf-8')
    for tag in tags:
        mystring = mystring.replace(tag,'')
    mystring = BeautifulSoup(mystring).text
    mystring = fix_text(mystring) #Transforms escaped characters into normal ones, ideally
    return mystring