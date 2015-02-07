# We extract names and acronyms for agencies from the dataset
# http://data.beta.nyc/dataset/city-record-sample-database/resource/2fa3e0e9-afda-4f27-8d76-07aba1d55823

AGENCIES = """Office of the Mayor,OOM
Board of Elections,NYCBOE
Campaign Finance Board,CFB
Office of the Actuary,OACT
Employees' Retirement System,NYCERS
Borough President - Manhattan,MBP
Borough President - Bronx,BXBP
Borough President - Brooklyn,BKBP
Borough President - Queens,QBP
Borough President - Staten Island,SIBP
Comptroller,OOC
Office of Emergency Management,OEM
Tax Commission,NYCTC
Law Department,NYCLD
Art Commission,ARTC
City Planning,DCP
Investigation,DOI
New York Public Library,NYPL
Public Library - Brooklyn,BKPL
Public Library - Queens,QPL
Education,NYCDOE
Teachers' Retirement System,TRS
School Construction Authority,SCA
Civilian Complaint Review Board,CCRB
Police,NYPD
Fire Department,FDNY
Board of Standards and Appeals,BSA
Administration for Children's Services,ACS
Human Resources Administration,HRA
Homeless Services,DHS
Correction,DOC
Board of Correction,BOC
Human Resources Administration,HRA
Supreme Court,SC
Public Advocate,NYCPA
City Council,CC
City Clerk,CCLK
Aging,DFTA
Cultural Affairs,DCLA
Financial Information Services Agency,FISA
Mayor's Office of Criminal Justice,MOCJ
Juvenile Justice,DJJ
Office of Payroll Administration,OPA
Independent Budget Office,IBO
Equal Employment Practices Commission,EEPC
Civil Service Commission,CSC
Landmarks Preservation Commission,LPC
Districting Commission,NYCDC
Taxi and Limousine Commission,TLC
Office of Labor Relations,OLR
Human Rights Commission,HRC
New York City Police Pension Fund,NYCPPF
Youth and Community Development,DYCD
Conflicts of Interest Board,COIB
Office of Collective Bargaining,OCB
Brooklyn Museum,BKM
Probation,DOP
Small Business Services,DSBS
Housing Preservation and Development,HPD
Buildings,DOB
Health and Mental Hygiene,DOHMH
Health and Hospitals Corporation,HHC
Administrative Trials and Hearings,OATH
Environmental Protection,DEP
Sanitation,DSNY
Business Integrity Commission,BIC
Finance,DOF
Transportation,DOT
Parks and Recreation,DPR
Design and Construction,DDC
Citywide Administrative Services,DCAS
Information Technology and Telecommunications,DOITT
Department of Records and Information Services,DORIS
Consumer Affairs,DCA
District Attorney - New York County,DANY
District Attorney - Bronx County,DABX
District Attorney - Kings County,DAKC
District Attorney - Queens County,DAQ
District Attorney - Richmond County,DAR
Office of Special Narcotics Prose,OSNP
County Clerk - New York,CLKM
County Clerk- Bronx,CLKBX
County Clerk - Kings,CLKK
County Clerk - Queens,CLKQ
County Clerk - Richmond,CLKR
Public Administrator - New York County,PA/M
Public Administrator - Bronx County,PA/X
Public Administrator - Kings County,PA/K
Public Administrator - Queens County,PA/Q
Public Administrator - Richmond County,PA/R
Housing Authority,NYCHA
Brooklyn Bridge Park,BBP
Board of Education Retirement System,BERS
Build NYC Resource Corporation,BNYCRC
Housing and Community Renewal,NYSDCHR
Changes In Personnel,CIP
Criminal Justice Coordinator,CJC
City Planning Commission,CPC
Deferred Compensation Plan Board,DCPB
Environmental Control Board,ECB
Industrial Development Agency,NYCIDA
Mayor's Fund to Advance New York City,MFANYC
Mayor's Office of Environmental Coordination,MOEC
Mayor's Office of Operations,MOO
Office of Administrative Tax Appeals,OATA
Brooklyn Navy Yard Development Corp.,BNYDC
Battery Park City Authority,BPCA
Economic Development Corporation,EDC
Upper Manhattan Empowerment Zone,UMEZDC
Technology Development Corporation,TDC
Triborough Bridge and Tunnel Authority,TBTA
Port Authority of New York and New Jersey,PANYNJ
Water Board,NYCWB
City University,CUNY
Chief Medical Examiner,OCME
Community Assistance Unit,CAU
Office of Management and Budget,OMB
Educational Construction Fund,ECF
Staten Island Rapid Transit Operating Authority,SIRT
Marketing Development Corp,MDC
Hudson River Park Trust,HRPT
Metropolitan Transportation Authority,MTA
NYC & Company,NYCC
Rent Guidelines Board,RGB
Franchise And Concession Review Committee,FCRC
Mayor's Office of Environmental Remediation,MOER
Banking Commission,NBC
Board Meetings,BM
Community Boards,NCB
Design Commission,NDC
Loft Board,NYCLB
Mayor's Office of Contract Services,MOCS
Procurement Policy Board,PPB
City Record,DCAS
Trust for Governors Island,TFGI
BROOKLYN COMMUNITY BOARD 18,BKCB"""
(agency_names, agency_abbrs) = zip(*map(lambda x:x.split(','), AGENCIES.split('\n')))

import re

AGENCIES_REGEX = re.compile("|".join(agency_names))
def extractAgencyNames(str):
    return AGENCIES_REGEX.findall(str, re.IGNORECASE)

AGENCIES_ACRONYM_REGEX = re.compile("|".join(agency_abbrs))
def extractAgencyAcronyms(str):
    return AGENCIES_ACRONYM_REGEX.findall(str, re.IGNORECASE)

PHONE_NUMBER_REGEX = re.compile("[(]\d\d\d[)] \d\d\d-\d\d\d\d")
def extractPhoneNumbers(str):
    return PHONE_NUMBER_REGEX.findall(str)

MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December"
DATE_REGEX = re.compile("(?:%s) (?:\d\d?), (?:\d\d\d\d)" % MONTHS)
def extractDate(str):
    return DATE_REGEX.findall(str, re.IGNORECASE)

TAG_RE = re.compile(r'<[^>]+>')
def cleanHtml(html):
    return TAG_RE.sub('', html).replace('&nbsp;', ' ')

nypl = open('nypl_hmtl.csv').read()
items = nypl.split('\n')[1:]
for item in items:
  clean_item = cleanHtml(item)
  print clean_item
  print extractAgencyNames(clean_item)
  print extractAgencyAcronyms(clean_item)
  print extractDate(clean_item)
  print extractPhoneNumbers(item)
  print
