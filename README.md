Implementation of a clamd client with a REST interface to take base64 encoded files

# Build and Run

To build the Docker image:
`docker build --tag <docker hub repo>/clamav:<version> .`

To push to Docker Hub:
`docker push <docker hub repo>/clamav:<version>`

To create a CloudFoundry app:
`cf push notify-clamav -f manifest.yml --docker-image <docker hub repo>/clamav:<version>`

To run the docker instance locally:
`docker run --name <docker hub repo>clamav:<version> -p 127.0.0.1:5000:5000 clamav`

# Usage

POST http://staging-notify-clamav.cloudapps.digital/v1/scan

The below example is the base64 encoded string of a test file which will give a virus FOUND response.

```javascript
{
    "file" : "WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy1URVNULUZJTEUhJEgrSCoK"
}
```

file: a base64 encoded string of a file

## Response from the server

### Good Response

```javascript
{
    "status": {
        "stream": [
            "OK",
            null
        ]
    }
}
```

### Bad Response

```javascript
{
    "status": {
        "stream": [
            "FOUND",
            "Eicar-Test-Signature"
        ]
    }
}
```