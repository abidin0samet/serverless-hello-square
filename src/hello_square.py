import json
from urllib.parse import parse_qs

def _resp(status, body, headers=None):
    base = {
        "statusCode": status,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body, ensure_ascii=False),
    }
    if headers:
        base["headers"].update(headers)
    return base

def handler(event, context):
    query = {}
    if isinstance(event, dict):
        if "rawQueryString" in event:
            query = parse_qs(event.get("rawQueryString") or "")
        elif "queryStringParameters" in event and event["queryStringParameters"]:
            query = {k:[v] for k,v in event["queryStringParameters"].items()}
    path = (event.get("rawPath") if isinstance(event, dict) else None) or "/"
    route = path.lstrip("/").split("?")[0]

    if route == "hello":
        name = None
        if "name" in query and query["name"]:
            name = query["name"][0]
        greeting = f"Merhaba {name}, bu fonksiyon bulutta çalışıyor!" if name else "Merhaba! Bu fonksiyon bulutta çalışıyor!"
        return _resp(200, {"message": greeting})

    if route == "square":
        number = None
        if "number" in query and query["number"]:
            try:
                number = int(query["number"][0])
            except ValueError:
                return _resp(400, {"error": "number parametresi tamsayı olmalıdır."})
        else:
            return _resp(400, {"error": "number parametresi zorunludur."})
        return _resp(200, {"input": number, "square": number * number})

    return _resp(404, {"error": "Route bulunamadı. /hello veya /square kullanın."})
