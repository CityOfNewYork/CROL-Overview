# City Record Online Workgroup (CROW) - Parsing

## Where this went (2026 note)

This repository is a **historical record** of the City Record Online Workgroup (CROW), 2014–2017. The project succeeded:

* **CROL launched in 2014** under [Local Law 7 of 2014 (Intro 363-2014)](https://legistar.council.nyc.gov/LegislationDetail.aspx?ID=1681058&GUID=E88BD576-8918-4067-B42B-B2D26E76CD27) — the City Record is published online daily at [a856-cityrecord.nyc.gov](https://a856-cityrecord.nyc.gov/).
* **The data is open**: the [City Record Online dataset](https://data.cityofnewyork.us/City-Government/City-Record-Online/dg92-zbpx) on NYC Open Data carries 1M+ notices (2003–present; full multi-section coverage from 2013), updated daily.
* **Programmatic access**: BetaNYC maintains [nyc-record-mcp](https://github.com/BetaNYC/nyc-record-mcp), an MCP server over the City Record API.
* The **2008–2014 text-file archive** in `Current DCAS Implementation/` is preserved (with checksummed manifest) in a BetaNYC archive repository, in preparation for public release.
* The sister schema effort lives at [CROL-Schema](https://github.com/CityOfNewYork/CROL-Schema). (`CROL-PDF` and `CROL-Parsing` were earlier names of *this* repo.)

Code under `Planned Implementation/` is Python 2-era and **unmaintained** — kept for historical reference, not for use. Several community links below (talk.beta.nyc, Google Drive folders) are from 2014–2015 and may only exist in the [Wayback Machine](https://web.archive.org/).


This is the main repository containing efforts pertaining to the parsing efforts of CROW. For Notice Schema development, see  https://github.com/CityOfNewYork/CROL-Schema.

Disclaimer. In case of conflicting document versions, please refer to documents mentioned in GitHub as the latest version.

## Important Docs

* [Gold standard -  a human parsed file that showed the "correct" extraction of the different object.](https://docs.google.com/spreadsheets/d/1M-XbFTsVmbOn2LPyhyZchH0AiYGMaYcEXn1fypPyj-c/edit?usp=sharing)
* [The Main Schema -  a reference file that shows what all the output fields should be and where (the source) they can be derived from.](https://docs.google.com/spreadsheets/d/1str6vjjHS5EA_2ww9r4WjHA1t32Z00uLLbviegTc8WI/edit#gid=1430366155)
  * Preserved in this repo (2026 export): [`Planned Implementation/Main Schema (Output).xlsx`](Planned%20Implementation/Main%20Schema%20(Output).xlsx) — CSV versions: [main sheet](Planned%20Implementation/main-schema-main-schema.csv), [schema guide](Planned%20Implementation/main-schema-schema-guide.csv)

###Open Standard Links

* [Reference Standards.](https://docs.google.com/document/d/1USFMTHfrmBzDvNW08b2f6osyl9I375d7h47uGcvxXjY/edit)



## Community Links
* [Discussion List](https://web.archive.org/web/2015*/talk.beta.nyc/c/working-groups/city-record-online) *(discussion forum retired; Wayback captures*)
* [Ongoing Tasks](https://github.com/CityOfNewYork/CROL-PDF/issues)
* [Resources](https://drive.google.com/drive/#folders/0B98QOZfGax93eWQyOHB4dWRWczg)
* [Tools and Wiki](https://github.com/CityOfNewYork/CROL-PDF/wiki)
* [Download PDFs](https://github.com/CityOfNewYork/CROL-PDF#download-pdfs)
* [Press Release & News Articles](https://github.com/CityOfNewYork/CROL-PDF#press-releases-blog-posts-and-news-articles)

## About

As the City embarks on implementing Intro 363-2014 and unlocking its daily actions, we are working together with the Department of Citywide Services to publish the City Record as open, clean and structured data. At the same time, we are unlocking decades of historical information and making it accessible to all, at no charge. 

Our goal is to optimize the utility of City Record content by making accessible and structuring the data; addresses, dates, persons, subjects, agencies, contract types and more are parsed and made available as individual objects. This way, residents, organizations and small and large businesses alike will be able to access, interact and stay informed, whether through notifications, visualizations or other easy-to-use community tools.


### Project Partners
* City of New York
* BetaNYC
* Commune
* Citizens Union 
* Dev Bootcamp 
* Ontodia
* Socrata
* Sunlight Foundation


## Achieved Milestones

* Came together to form a CROW parsing and scraping volunteer team
* Set up collaboration framework with DCAS
* Scraped PDFs from 2008 - 2014
* Proposed public notice schema
* Added “addresses” and “time & dates” fields to the City’s input workflow

## Tasks
For a list of current tasks, please see Issues.

### Phase 1: Parsers and Schema
* Develop a set of collaboratively produced open source library parsers to populate the Public Notice Data Standard schema using the DCAS pipeline 

* Work with DCAS to implement the pipeline into the City’s workflow by August 1, and use that as their way of publishing the City Record data

* Publish a Public Notice Data Standard and documentation on an interactive website

### Phase 2: PDF Scraping
* Scrape the archival PDFs
* Apply and modify the parsers to be able to parse and structure the data in the PDFs


## Press Releases, Blog Posts, and News Articles

### Blog Posts
* [BetaNYC Statement](https://beta.nyc/2014/08/07/betanycs-statement-on-the-signing-of-nycs/)

### Press Releases / News Articles 
* [City Hall Press Release](http://www1.nyc.gov/office-of-the-mayor/news/393-14/mayor-bill-de-blasio-signs-two-transparency-bills-law-public-private-partnership-to)
* [Citizens Union Statement](http://us3.campaign-archive1.com/?u=ca0fb41d668202ba6cc542ca8&id=91fa752d3f&e=[UNIQID])
* [Gotham Gazette](http://www.gothamgazette.com/index.php/government/5211-de-blasio-embraces-civic-tech-bill-city-record-online)
* [CM Ben Kallos Press Release](http://benkallos.com/press-release/mayor-bill-de-blasio-signs-two-transparency-bills-law-announces-public-private-partner)
* [TechPresident](http://techpresident.com/news/25231/new-york-city-and-silicon-valley-local-government-innovation-gets-outside-help)
