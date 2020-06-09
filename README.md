## Run
```bash
python -m fluffy_parakeet
```

## Config
```json
// config.json
{
    "timeout": 3 // req timeout
}
```

```json
//route.json
[
    {
        "path":"/flaskapp",
        "methods":["GET", "POST"],
        "d_address":"http://127.0.0.1:5000/",
        "d_method":"GET"
    }
]
```