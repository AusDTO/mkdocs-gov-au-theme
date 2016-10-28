# Sending emails from your application

<br />
![Email Symbol](/usage/email_symbol.svg "Email Symbol")

## Introduction

cloud.gov.au have a resilient, highly available (outbound only) smtp service available.  
This service allows applications deployed to cloud.gov.au to send outbound emails.  
There is no capability to receive emails.

## Requesting Access

To use this smtp service then please lodge a request by emailing `support@cloud.gov.au`. Make sure you include the email address that all emails will be coming from.

We create you an account and add your domain (if not already done) to the [DKIM](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail) setup and send you the credentials along with some dns TXT records for [SPF](https://en.wikipedia.org/wiki/Sender_Policy_Framework) & DKIM.
You will need to make sure these dns records are adjusted to aid in your emails being delivered.

## Using the system

You should configure your application to use the following settings:

**Host**: smtp.hasmtp.cld.gov.au  
**Port**: 587  
**Encryption**: STARTTLS  
**AUTH Type**: LOGIN or PLAIN  
**AUTH Username**: *whole email address*  
**AUTH Pass**: Your password will be sent to you via sms .  

## Limitations

There is no access to smtp logging at this stage.  
This service is for unclassified use only. No DLM markers will be applied.


