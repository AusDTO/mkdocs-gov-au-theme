## Deleting an Application

To get a list of existing apps deployed in the curent space run `cf apps`.

``` bash
[~/src/github.com/AusDTO/demo-app]
lunix@boran]  (master) -> cf apps
Getting apps in org dto / space dtoweb as example.person@digital.gov.au...
OK

name         requested state   instances   memory   disk   urls
dto-gov-au   started           1/1         64M      256M   dto-gov-au.apps.staging.digital.gov.au
mydemoapp    started           1/1         64M      256M   mydemoapp.apps.staging.digital.gov.au

[~/src/github.com/AusDTO/demo-app]
lunix@boran]  (master) ->
```

To delete an application from the platform is `cf delete <appname>`  
You should be very careful here - _measure twice - cut once !_

``` bash
[~/src/github.com/AusDTO/demo-app]
lunix@boran]  (master) -> cf delete mydemoapp

Really delete the app mydemoapp?> y
Deleting app mydemoapp in org dto / space dtoweb as example.person@digital.gov.au...
OK

[~/src/github.com/AusDTO/demo-app]
lunix@boran]  (master) ->

```
