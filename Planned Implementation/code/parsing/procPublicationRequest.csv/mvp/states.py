class State:
    def run(self):
        # implement this for printing trace statements
        assert 0, "implement me"

    def next(self, input):
        assert 0, "implement me"

    def flush(self, record):
        raise Exception('Unexpected error, wrong state: {}!'.format(self))


class Adverts(State):

    def __init__(self):
        State.__init__(self)

        # Current key and Value
        # value can span multiple lines/paragraphs
        # so we have to build it up a chunk at a time.
        # The complete text of value is assumed when
        # a new key/value pair is detected
        self.key = None
        self.value = None

        # Current Advertisement
        self.advert = {}
        self.processingAdvert = False

    def run(self):
        print('Process ADVERTS')

    def flush(self, record):
        self.advert[self.key] = self.value.strip()
        record['adverts'].append(self.advert)

    def next(self, para, record):
        text = para.get_text(strip=True)
        if ':' in text:
            k, v = text.split(':', 1)
            k = k.strip()
            if k.lower().startswith('agency'):
                # the first time the code gets here
                # processingAdvert is False, set it to True
                # so that from now on getting here means
                # we've completed an Advertisement

                if self.processingAdvert:
                    # End of record reached
                    self.advert[self.key] = self.value.strip()
                    record['adverts'].append(self.advert)
                    self.advert = {}

                # yep, processing advertisements
                self.processingAdvert = True

            else:
                # A new key/value pair is detected,
                # store current key/value pair
                self.advert[self.key] = self.value.strip()

            # Initialize the current key/value pair
            self.key, self.value = k, v

        else:
            # A value can span multiple lines
            # keep adding chunks to the current value
            # until a new key/value pair is detected...
            if self.value:
                self.value += text   # Append to a previous value
            else:
                self.value = text    # Otherwise set value

        return self


class Preamble(State):
    def run(self):
        print('PREAMBLE')

    def next(self, para, record):
        text = para.get_text(strip=True).strip()
        if 'NOTICE IS HEREBY' in text:
            record['preamble'] = text
            return Adverts()
        return self


class Init(State):
    def run(self):
        print('INIT')

    def next(self, para, record):
        if para.find_all('u'):
            record['context'] = para.get_text(strip=True).strip()
            return Preamble()
        return self
