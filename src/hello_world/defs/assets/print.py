import dagster as dg
import requests

@dg.asset
def hello() -> None: 
    try: 
        print('hello')
        requests.post("https://ntfy.sh/dagster_hello_worlds",
            data="hello success".encode(encoding='utf-8'))
    except Exception as e:
        requests.post("https://ntfy.sh/dagster_hello_worlds",
            data="hello fail".encode(encoding='utf-8'))
        raise
    


@dg.asset(deps=['hello'])
def world() -> None:
    try:      
        print('world')
        requests.post("https://ntfy.sh/dagster_hello_worlds",
            data="world success".encode(encoding='utf-8'))
    except Exception as e:
        requests.post("https://ntfy.sh/dagster_hello_worlds",
            data="world fail".encode(encoding='utf-8'))
        raise




