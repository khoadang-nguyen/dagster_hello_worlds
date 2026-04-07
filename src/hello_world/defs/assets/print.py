import dagster as dg
from pathlib import Path
from hello_world.resources.send_ntfy import NftyResource


@dg.asset
def hello(nfty: NftyResource) -> None: 
    
    try: 
        print('hello')
        nfty.success_message()
    except Exception as e:
        nfty.failure_message()
        raise e



@dg.asset(deps=['hello'])
def world(nfty: NftyResource) -> None:
    try: 
        print('world')
        nfty.success_message()
    except Exception as e:
        nfty.failure_message()
        raise e





