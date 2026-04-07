import dagster as dg
import requests
from .config import SUCCESS, FAILURE, CHANNEL
from dagster import ConfigurableResource

class NftyResource(ConfigurableResource):
    channel: str = CHANNEL
    success: str = SUCCESS
    failure: str = FAILURE

    def success_message(self) -> None:
        requests.post(self.channel, data=self.success.encode(encoding='utf-8'))

    def failure_message(self) -> None:
        requests.post(self.channel, data=self.failure.encode(encoding='utf-8'))


