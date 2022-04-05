## Quickstart Guide

This guide aims to set up the utility scripts and troubleshoot common errors in the installation process.

## Common Errors on Startup
```
KeyError: 'GOOGLE_APPLICATION_CREDENTIALS'
[XXXXX] Failed to execute script 'main' due to unhandled exception!
```
or 
```
KeyError: 'GOOGLE_MAPS_API_KEY'
[XXXXX] Failed to execute script 'main' due to unhandled exception!
```

As the program relies on several Google Cloud methods to function,
these errors indicate that you have not modified your machine's PATH variable to point to the authentication file or key.

* If the error is `'GOOGLE_APPLICATION_CREDENTIALS'`:
  * Download the JSON key and set up PATH as described [here](https://cloud.google.com/docs/authentication/getting-started).
* If the error is `'GOOGLE_MAPS_API_KEY'`:
  * Follow the guide [here](https://developers.google.com/maps/documentation/javascript/get-api-key) under "Creating API Keys,"
  then create a PATH variable with name `GOOGLE_MAPS_API_KEY` and contents being the API key.

This will be remediated in the future with a helper script.