import dagster as dg
from pathlib import Path
from hello_world.resources.send_ntfy import NftyResource
import requests
from datetime import datetime

TODAY = datetime.today().date().strftime(format='%Y-%M-%d')

@dg.asset
def hello(
          context : dg.AssetExecutionContext) -> None: 
    
    try: 
        context.log.info(f"Đang run asset Hello cho ngày {TODAY}")
        prrint("Hello")
        # nfty.success_message()
    except Exception as e:
         
         ERROR = f"asset hello run cho ngày {TODAY} lỗi: {str(e)}"
         context.log.info(ERROR)
         context.log.info("Đang gửi lỗi")
         requests.post("https://ntfy.sh/dagster_hello_worlds", data = ERROR.encode(encoding='utf-8'), verify=False)
         context.log.info("Gửi lỗi thành công")



@dg.asset(deps=['hello'])
def world(nfty: NftyResource) -> None:
    try: 
        print('world')
        SUCCESS = "data run thành công"
        nfty.success_message(SUCCESS)
    except Exception as e:
        ERROR = str(e)
        nfty.failure_message(ERROR)





