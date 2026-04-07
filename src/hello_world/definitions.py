from pathlib import Path
import dagster as dg

from hello_world.resources.send_ntfy import NftyResource
from hello_world.defs.assets.print import hello, world
from hello_world.defs.jobs import print_hello_job, print_world_job
from dagster import definitions, load_from_defs_folder


@definitions
def defs():
    return dg.Definitions(resources = {"nfty": NftyResource()}, assets = [hello, world], jobs = [print_hello_job, print_world_job])


