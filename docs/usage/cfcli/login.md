# Platform Login

Before working with The Platform you need to instruct the cf cli what platform API endpoint, organisation & space to work with and what your credentials are. If you only belong to one ORG and/or space then these will be auto-selected for you.

``` bash
[~/src/github.com/AusDTO/ops/sekrets]
lunix@boran]  (master) -> cf login -a https://api.system.staging.digital.gov.au --skip-ssl-validation
API endpoint: https://api.system.staging.digital.gov.au

Email> example.person@digital.gov.au

Password>
Authenticating...
OK

Targeted org dto

Targeted space dtoweb


API endpoint:   https://api.system.staging.digital.gov.au (API version: 2.43.0)
User:           example.person@digital.gov.au
Org:            dto
Space:          dtoweb
```

You should now be logged in and ready.
