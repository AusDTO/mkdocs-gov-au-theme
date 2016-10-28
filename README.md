# MkDocs UI Kit theme

[![PyPI version](https://badge.fury.io/py/mkdocs-gov-au-theme.svg)](https://badge.fury.io/py/mkdocs-gov-au-theme)

A Digital Transformation Office UI Kit theme for [MkDocs](http://www.mkdocs.org/). View a [demo of this theme](http://docs.cloud.gov.au/)

## Quick start

Install with `pip`:

```
pip install mkdocs-gov-au-theme
```

Add the following line to `mkdocs.yml`:

```
theme: 'gov-au-theme'
```

## Customise page template

This theme allows you to add certain components to the page by specifying configuration options in the `mkdocs.yml` file. All the custom components must be listed as key value pairs within the `extra` YAML array.

For example:

```
extra:
  badge: beta
  feedback_link:
    - 'title': 'Support request'
      'url': 'https://www.support-url.gov.au'
```

### Add project badge to your docs

You can add a badge to the site title in the header by adding the following
line to `mkdocs.yml`:

```
extra:
  badge: beta
```

You can add whatever text you want within the badge. This can be helpful to let the user know if your docs are in [Alpha, Beta or Live](https://www.dto.gov.au/standard/service-design-and-delivery-process/).

### Add feedback or contact button to your header

You may want users to be able to lodge tickets or email you for help with your documentation or service.

You can do this by adding the following lines to `mkdocs.yml`:

```
extra:
  feedback_link:
    - 'title': 'Support request'
      'url': 'https://www.support-request-url.gov.au'
```

### Add basic text search to you docs

Add the following line to `mkdocs.yml`:

```
extra:
  search: true
```

### Add links in the footer

Add the following lines to `mkdocs.yml`:

```
extra:
  footer_links:
    - 'title': 'Status'
      'url': 'http://status.gov.au'
      'external': 'true'
    - 'title': 'Privacy policy'
      'url': '/privacy-policy'
```

You can add as many links as needed. You can also specify whether a link is an external link with `'external': 'true'`

### Add links to edit current page on github

If you specify a `repo_url` for your docs the template will automatically add a
'Edit this page on GitHub' link to each page generated for a .md file. This link will take the
user to the md file on `master` branch in the GitHub repo.

You can specify your GitHub repo by adding the following line to `mkdocs.yml`:

```
repo_url: https://github.com/AusDTO/mkdocs-gov-au-theme
```

**You *do not* specify the repo_url within the `extra:` YML array**

## Even more configuration options

This theme also allows you to add and modify tags in your sites `<head>`.

### Add Google Analytics

Add the following lines to `mkdocs.yml`:

```
google_analytics: ['UA-12345678-9', 'name']
```

## Projects currently using MkDocs UI Kit theme

- [docs.cloud.gov.au](https://github.com/AusDTO/cga_docs)
