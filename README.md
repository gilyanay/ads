# ads

this app was build as a microservice with 3 different resource. \
the main file receives the REST request and allocates here to the corrct resource. 

I build this app like this, so if in the future the app will receive different kind of request, for instance a kafka event that will be registered in a specific callback.

in this app I build 3 different resource: ads, impression and stats.

although currently their only one request per resource, the division is more logic. 

## get ad:
 - endpoint: /ads
 - method: GET
    ## query params:
     - sdk_version
     - user_name
     - country_code
     - platform
     - session_id
     ## response:
     - vast xml ad - as string


## impression:
- endpoint: /impressions
- method: POST 
    ## object:
    - sdk_version
    - user_name
    - country_code
    - platform
    - session_id
    ## response:
     - Http 200


## get stats:
- endpoint: /stats
- method: Get
    ## query params:
     - filter_type
     ## response:
     - object type with:
       - impressions per user/sdk version
       - ads request per user/sdk_version
       - fill rate - impressions/ads request

