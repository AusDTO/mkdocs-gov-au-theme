# Log Access

We are able to access our application’s log output by using the cf logs command like this:
`cf logs mydemoapp`

This will tail the application logs, from all Application Instances, straight to your development workstation's console.

You can test it by opening up your browser and accessing [http://mydemoapp.apps.staging.digital.gov.au](http://mydemoapp.apps.staging.digital.gov.au).
This will produce the following output:

``` bash
[~/src/github.com/AusDTO/demo-app]
lunix@boran]  (master) -> cf logs mydemoapp
Connected, tailing logs for app mydemoapp in org dto / space dtoweb as example.person@digital.gov.au...

2016-02-15T14:40:11.61+1100 [RTR/0]      OUT mydemoapp.apps.staging.digital.gov.au - [15/02/2016:03:40:11 +0000] "GET / HTTP/1.1" 200 0 126 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36" 10.0.0.141:14391 x_forwarded_for:"1.129.96.124" x_forwarded_proto:"http" vcap_request_id:27c111af-4ea8-4c26-696c-0e90bd3908eb response_time:0.002084462 app_id:8d1ad4e9-9607-4927-abd3-522c621953b3
2016-02-15T14:40:11.66+1100 [APP/0]      OUT ==> /home/vcap/app/nginx/logs/access.log <==
2016-02-15T14:40:11.66+1100 [APP/0]      OUT 1.129.96.124, 10.0.0.141 - - - [15/Feb/2016:03:40:11 +0000] "GET / HTTP/1.1" 200 126
2016-02-15T14:40:16.76+1100 [RTR/0]      OUT mydemoapp.apps.staging.digital.gov.au - [15/02/2016:03:40:16 +0000] "GET / HTTP/1.1" 304 0 0 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36" 10.0.0.141:14391 x_forwarded_for:"1.129.96.124" x_forwarded_proto:"http" vcap_request_id:9bd055fc-9717-431b-7f4d-f244c3d7c581 response_time:0.001701489 app_id:8d1ad4e9-9607-4927-abd3-522c621953b3
2016-02-15T14:40:17.20+1100 [RTR/0]      OUT mydemoapp.apps.staging.digital.gov.au - [15/02/2016:03:40:17 +0000] "GET / HTTP/1.1" 304 0 0 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36" 10.0.0.141:14391 x_forwarded_for:"1.129.96.124" x_forwarded_proto:"http" vcap_request_id:40ee6886-f0d9-46d0-7feb-628ce10a5bff response_time:0.001669128 app_id:8d1ad4e9-9607-4927-abd3-522c621953b3
2016-02-15T14:40:17.44+1100 [RTR/0]      OUT mydemoapp.apps.staging.digital.gov.au - [15/02/2016:03:40:17 +0000] "GET / HTTP/1.1" 304 0 0 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36" 10.0.0.141:14391 x_forwarded_for:"1.129.96.124" x_forwarded_proto:"http" vcap_request_id:aa887531-4bdb-474e-6768-1bbc45e09fa1 response_time:0.0016547 app_id:8d1ad4e9-9607-4927-abd3-522c621953b3
2016-02-15T14:40:17.66+1100 [APP/0]      OUT 1.129.96.124, 10.0.0.141 - - - [15/Feb/2016:03:40:16 +0000] "GET / HTTP/1.1" 304 0
2016-02-15T14:40:17.66+1100 [APP/0]      OUT 1.129.96.124, 10.0.0.141 - - - [15/Feb/2016:03:40:17 +0000] "GET / HTTP/1.1" 304 0
2016-02-15T14:40:17.66+1100 [APP/0]      OUT 1.129.96.124, 10.0.0.141 - - - [15/Feb/2016:03:40:17 +0000] "GET / HTTP/1.1" 304 0
2016-02-15T14:40:22.17+1100 [HEALTH/0]   OUT healthcheck passed
2016-02-15T14:40:22.17+1100 [HEALTH/0]   OUT Exit status 0
^C[~/src/github.com/AusDTO/demo-app]
lunix@boran]  (master) ->
```


To see logs from the past:

``` bash
[~/src/github.com/AusDTO/demo-app]
lunix@boran]  (master) -> cf logs --recent mydemoapp
Connected, dumping recent logs for app mydemoapp in org dto / space dtoweb as example.person@digital.gov.au...

2016-02-15T14:38:23.91+1100 [STG/0]      OUT Downloading staticfile_buildpack...
2016-02-15T14:38:23.96+1100 [STG/0]      OUT Downloaded staticfile_buildpack
2016-02-15T14:38:23.98+1100 [STG/0]      OUT Downloaded buildpacks
2016-02-15T14:38:23.98+1100 [STG/0]      OUT Staging...
...
...
```
