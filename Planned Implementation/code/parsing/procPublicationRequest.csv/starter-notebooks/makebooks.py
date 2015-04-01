import pandas as pd
import json
csv = '../procPublicationRequest Oct-Dec 2014 (Updated) - Sheet1-2.csv'
src = 'starter.ipynb.template'

template = json.load(open(src,'r'))
template = json.dumps(template)

df = pd.read_csv(csv, header=0)
table = df[["AgencyName", "TypeOfNoticeDescription", "RequestID"]]
table = pd.DataFrame(table.groupby(["AgencyName", "TypeOfNoticeDescription"])["RequestID"].count())
table.columns = ['Message Count']
table = table.sort(['Message Count'], ascending=[0])

for dx in range(table.count()[0]):
    agency, notice = table.iloc[dx].name
    fnout = '{}-{}'.format(''.join([a.capitalize() for a in agency.replace("'",'').split(' ')]), notice.lower().replace(' ',''))
    fnout = '{}.ipynb'.format(fnout)
    print(fnout)
    dump = template.replace('{{AGENCY}}', agency).replace('{{TYPEOFNOTICEDESCRIPTION}}', notice)
    open(fnout,'w').write(dump)
