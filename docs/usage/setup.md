# Setting your project up

Congratulations, you should now have your cloud.gov.au accounts all setup.  
All you need now is to scaffold out a codebase, activate circleci and push the code to github.

## Requirements

* A workstation (preferred Linux or OSX)
* git
* browser
* cf-cli
* ruby
* jalpha rubygem

The DTO has produced a rubygem, `jalpha`, for scaffolding out an opinionated Jekyll stack for your Alpha.

## Actions

* `gem install jalpha`
* `jalpha new <projectname>`
* `cd <projectname>`
* `bin/setup`
* `git init`
* `git remote add ....`
* `git add -a`
* `git commit -am 'initial commit'`
* `git push -u origin master`
* go to circleci in the browser and authorize with Github.
* follow your new github repo
* add some environment variables via the circleci UI
```
CF_API
CF_ORG
CF_PASSWORD
CF_SPACE
CF_USER
CF_BASIC_AUTH_USERNAME  [optional]
CF_BASIC_AUTH_PASSWORD  [optional]
```


