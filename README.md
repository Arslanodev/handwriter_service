# Description
Service for generating handwritten text out of digital text

## Endpoints

`POST` - `/`
data: 
```json
{
    "text": ["hello world"]
}
```
return:
```json
{
    "result_id": "/result/<id>"
}
```
Get results:
`GET` - `/result/<result_id>`

Return:
```json
{
    "ready": true,
    "successful": true,
    "value": {
        "download_link": "/download/d6ec16dd-ca1a-41a1-9170-65c437f83b96"
    }
}
```