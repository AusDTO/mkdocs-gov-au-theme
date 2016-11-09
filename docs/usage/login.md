Before you can login you will need to:

- [install CloudFoundry command line tools](/usage/setup/)
- be a member of an existing project on cloud.gov.au

If you are starting a new project then you will need to [Request a new project](/usage/start_new_project/)

If you need access to an existing project then ask the projects CloudFoundry maintainer. This is usually the Delivery Manager or Tech Lead. If you get stuck you can [send us a support ticket](mailto:support@cloud.gov.au).

Login with:

```
cf login -a https://api.system.staging.digital.gov.au
```

You will then need to enter your email address, password and select from a list of available Orgs and Spaces.

You can also define your login options all at once with:

```
cf login -a https://api.system.staging.digital.gov.au -u <email> -o <org> -s <space>
```

Once logged in, to target a different project use:

```
cf target -o <org> -s <space>
```

The `<org>` is the CloudFoundry organisation. This is usually the name of the project.

The `<space>` is the CloudFoundry space. This is usually the name of the application.

For example:

```
cf target -o digital-marketplace -s marketplace-frontend
```

Now you can deploy and manage your application from the Command Line.
