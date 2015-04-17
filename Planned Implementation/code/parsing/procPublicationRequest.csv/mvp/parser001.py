from bs4 import BeautifulSoup as Soup
import pandas as pd
# import numpy as np
# import re
# import pprint
import json

from states import Init
from schemas import NoticeType, SectionName
from schemas import Organization, Notice

import dateutil.parser
from datetime import datetime as dt

def parse_notice(soup):
    state = Init()
    record = {'adverts': []}

    for para in soup.find_all('p'):
        state = state.next(para, record)

    state.flush(record)
    return record


def scrape(row):
    output = None
    try:
        output = parse_notice(Soup(row.AdditionalDescription))
    except Exception:
        output = {'error': 'bad input: [{}]'.format(row.AdditionalDescription)}
    row['output'] = json.dumps(output)
    return row


def get_data_df(fn='../orig.procPublicationRequest.oct-dec-2014.csv'):
    rows = pd.read_csv(fn, header=0, sep='|', encoding='latin-1')
    # print(rows.columns)
    mocs = rows['AgencyName'] == "Mayor's Office of Contract Services"
    meets = rows['TypeOfNoticeDescription'] == "Notice"
    return rows[mocs & meets].apply(scrape, 1)

if __name__ == '__main__':
    cols = ['RequestID', 'StartDate', 'EndDate',
            'AgencyCode', 'AgencyName', 'AgencyDivision',
            'TypeOfNoticeCode', 'TypeOfNoticeDescription',
            'ShortTitle', 'SectionID', 'SectionName',
            'DueDate', 'ConfirmationNumber',
            'AdditionalDescription', 'output']

    rows = get_data_df()[:1]
    rows = rows.fillna('')
    # for rec in rows[['output', 'AdditionalDescription']].values:
    index = cols[:-2]
    index.sort()
    for rec in rows[cols].values:
        dic = dict(zip(cols, rec))
        # pprint.pprint(dic)
        if not isinstance(dic['AdditionalDescription'], str):
            dic['AdditionalDescription'] = str(dic['AdditionalDescription'])

        # pprint.pprint(json.loads(dic['output']).keys())
        for dx in index:
            print('{}: {}'.format(dx, dic[dx]))

        s_noticetype = NoticeType()
        s_noticetype.name = dic['TypeOfNoticeDescription']
        s_noticetype.id = dic['TypeOfNoticeCode']
        s_noticetype.validate()

        s_org = Organization()
        s_org.identifier = dic['AgencyCode']
        s_org.name = dic['AgencyName']
        s_org.classification = dic['AgencyDivision']
        # s_org.parent = dic['']
        s_org.validate()

        s_secname = SectionName()
        s_secname.id = dic['SectionID']
        s_secname.name = dic['SectionName']
        s_secname.validate()

        notice = Notice()
        notice.sectionName = s_secname
        notice.noticetype = s_noticetype
        notice.publishingOrganization = s_org
        notice.title = dic['ShortTitle']
        notice.endDate = dateutil.parser.parse(dic['EndDate'])
        notice.startDate = dateutil.parser.parse(dic['StartDate'])
        notice.createdAt = dt.strptime(str(dic['RequestID'])[:8], '%Y%m%d')
        # notice.lastUpdatedAt = dic['']
        # notice.printOut = dic['']
        # notice.otherInfo = dic['']

        notice.validate()
        print(json.dumps(notice.to_primitive(), indent=True))
        print('\n\n')
        # print (json.dumps(json.loads(dic['output']), indent=True))
        # print('\n\n')

'''
# AgencyCode: OCS
# AgencyDivision: Procurement
# AgencyName: Mayor's Office of Contract Services

    ConfirmationNumber: 20140930106
    DueDate: nan
# EndDate: 2014-10-07 00:00:00
    RequestID: 20140930106
# SectionID: 5
# SectionName: Special Materials
# ShortTitle: DOITT extension
# StartDate: 2014-10-07 00:00:00
# TypeOfNoticeCode: 13
# TypeOfNoticeDescription: Notice
'''
