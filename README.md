# embyserverapi
Emby Server API - Python. Generated via Swagger Codegen.
  
## Installation & Usage
### pip install

Python package hosted on PyPi - https://pypi.org/project/EmbyServerAPI/
```sh
pip install EmbyServerAPI
```

## Generate from source
If you build from source, be aware that your rest.py file will not contain the changes located in this [commit](0543e40).  
This change was necessary for uploading base64strings via image_service_api.

### Instructions
Modify the following attributes in config.json.
 * *projectName*
 * *packageVersion*  

Run codegen.sh.

