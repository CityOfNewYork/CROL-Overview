# Record Types and Schemas #

Working doc using records from 8/7/2014 City Record PDF: http://www.nyc.gov/html/dcas/downloads/pdf/cityrecord/cityrecord-08-07-14.pdf  -CMW


### publicHearings ###

  entityName: "City Planning Commission"
  
  subEntityName: 
  
  time: "2014-08-20T10:00:00-04:00"
  
  locationText: "Spector Hall, 22 Reade Street, New York, NY"
  
  locationLat:"40.714264"
  
  locationLon:"-74.004393"
  
  hearingID:"N 150021 PXM"
  
  hearingTitle:"420 LEXINGTON AVENUE OFFICE SPACE"
  
  recordText: "IN THE MATTER OF a Notice of Intent to acquire office space submitted by the Department of Citywide Administrative Services, pursuant to Section 195 of the New York City Charter for use of property located at 420 Lexington Avenue (Block 1280, Lot 60) (Office of Court Administration offices)."
  
  pointOfContact: "YVETTE V. GRUEL, Calendar Officer"

#### Schema.org version - JSON-LD ####
```json
 <script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "Event/Hearing",
    "name/hearingTitle": "420 LEXINGTON AVENUE OFFICE SPACE",
    "url/hearingID": "C 140411 HAK",
    "startDate": "2014-08-20T10:00:00",
    "duration": "PT6H",
    "location": {
        "@type": "Place",
        "address": {
            "@type": "PostalAddress",
            "addressCountry": "USA",
            "addressLocality": "New York",
            "addressRegion": "NY",
            "postalCode": "10007",
            "streetAddress": "Spector Hall, 22 Reade Street, Room 2E"
        },
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": "40.721290",
            "longitude": "-73.948890"
        }
    },
    "description/recordText": "IN THE MATTER OF an application submitted by the Department of Housing Preservation and Development (HPD); UDAAP designation, project approval and disposition of city-owned property to facilitate development of an 8-story mixed-use building with approximately 51 residential dwelling units, 41 units of affordable housing and ground floor commercial space.",
    "organizer": [
        {
            "@type": "GovernmentOrganization",
            "name": "City Planning Commission"
        },
        {
            "@type": "Person",
            "name": "YVETTE V. GRUEL",
            "jobTitle": "Calendar Officer",
            "contactPoint": {
                "@type": "contactPoint",
                "telephone": "(212) 720-3370",
                "contactType": "customer service"
            }
        }
    ]
}
</script> 
```  
  
  entityName: "Brooklyn Community Board 1"
  
  subEntityName: 
  
  time: "2014-08-12T18:00:00-04:00"
  
  locationText: "211 Ainslie Street c/o Manhattan Ave., Brooklyn, NY"
  locationLat:"40.721290"
  
  locationLon:"-73.948890"
  
  hearingID:"C 140411 HAK"
  
  hearingTitle:"695 Grand Avenue"
  
  recordText: "IN THE MATTER OF an application submitted by the Department of Housing Preservation and Development (HPD); UDAAP designation, project approval and disposition of city-owned property to facilitate development of an 8-story mixed-use building with approximately 51 residential dwelling units, 41 units of affordable housing and ground floor commercial space."
  
   pointOfContact:
  
  
  
  


### propertyDisposition ###

  entityName:"Citywide Administrative Services"
  
  subEntityName: "Office of Citywide Procurement"
  
  recordText: "The Department of Citywide Administrative Services, Office of Citywide Procurement is currently selling surplus assets on the internet. Visit http://www.publicsurplus.com/sms/nycdcas.ny/browse/home. To begin bidding, simply click on ‘Register’ on the home page. There are no fees to register. Offerings may include but are not limited to: office supplies/equipment, furniture, building supplies, machine tools, HVAC/plumbing/electrical equipment, lab equipment, marine equipment, and more. Public access to computer workstations and assistance with placing bids is available at the following locations:� DCAS Central Storehouse, 66-26 Metropolitan Avenue, Middle Village, NY 11379 � DCAS, Office of Citywide Procurement, 1 Centre Street, 18th Floor, New York, NY 10007"
  


### procurement ###



