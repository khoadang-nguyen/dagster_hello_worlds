from typing import Union

import dagster as dg
from hello_world.defs.jobs import print_hello_job, print_world_job

hello_schedule = dg.ScheduleDefinition(job=print_hello_job, cron_schedule='0 6 * * *')
world_schedule = dg.ScheduleDefinition(job=print_world_job, cron_schedule='0 7 * * *')
