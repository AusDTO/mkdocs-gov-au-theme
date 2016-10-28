# Application Deployment

To get a list of existing apps depoloyed in the curent space run `cf apps`.

The command used for deploying a new app, or for updating an existing app, is `cf push ...`

There is a fair amount of options available to the `cf push` command. To see them all run `cf push --help`

Let's push our demo application now to the platform.

``` bash
[~/src/github.com/AusDTO/pcf_demo_app]
lunix@boran]  (master) -> cf push mydemoapp -b staticfile_buildpack -n mydemoapp -i 1 -m 64M -k 256M
...
...
```
There is a bit going on here. Lets run throught what the options are:

**-b** :specifiy what buildpack to use to configure the Application Instance  
**-n** :sets the subdomain under which our application will be available  
**-i** :sets how many instances are required to serve our application  
**-m** :sets the maximum RAM usage for our application (e.g. 256M, 1024M, 1G)  
**-k** :sets the maximum DISK usage for our application (e.g. 256M, 1024M, 1G)  

Lets see this in action.
``` bash
[~/src/github.com/AusDTO/pcf_demo_app]
lunix@boran]  (master) -> cf push mydemoapp -b staticfile_buildpack -n mydemoapp -i 1 -m 64M -k 256M
Creating app mydemoapp in org dto / space dtoweb as example.person@digital.gov.au...
OK

Creating route mydemoapp.apps.staging.digital.gov.au...
OK

Binding mydemoapp.apps.staging.digital.gov.au to mydemoapp...
OK

Uploading mydemoapp...
Uploading app files from: /home/lunix/src/github.com/AusDTO/pcf_demo_app
Uploading 550B, 2 files
Done uploading
OK

Starting app mydemoapp in org dto / space dtoweb as example.person@digital.gov.au...
Creating container
Successfully created container
Downloading app package...
Downloaded app package (518B)
Downloading buildpacks (staticfile_buildpack)...
Downloading staticfile_buildpack...
Downloaded staticfile_buildpack
Downloaded buildpacks
Staging...
-------> Buildpack version 1.2.2
Downloaded [file:///tmp/buildpacks/59f767b9bf9c7cde279cb3b56367792c/dependencies/https___s3.amazonaws.com_pivotal-buildpacks_nginx_cflinuxfs2_nginx-1.8.0-linux-x64.tgz]
grep: Staticfile: No such file or directory
-----> Using root folder
-----> Copying project files into public/
-----> Setting up nginx
grep: Staticfile: No such file or directory
Exit status 0
Staging complete
Uploading droplet, build artifacts cache...
Uploading droplet...
Uploading build artifacts cache...
Uploaded build artifacts cache (131B)
Uploaded droplet (2.4M)
Uploading complete

1 of 1 instances running

App started


OK

App mydemoapp was started using this command `sh boot.sh`

Showing health and status for app mydemoapp in org dto / space dtoweb as example.person@digital.gov.au...
OK

requested state: started
instances: 1/1
usage: 64M x 1 instances
urls: mydemoapp.apps.staging.digital.gov.au
last uploaded: Mon Feb 15 01:46:56 UTC 2016
stack: cflinuxfs2
buildpack: staticfile_buildpack

     state     since                    cpu    memory        disk            details
#0   running   2016-02-15 12:47:36 PM   0.0%   3.3M of 64M   33.7M of 256M

[~/src/github.com/AusDTO/pcf_demo_app]
lunix@boran]  (master) ->
```

With just a single command you should now have your application running on the DTO Platform at [http://mydemoapp.apps.staging.digital.gov.au](http://mydemoapp.apps.staging.digital.gov.au)
