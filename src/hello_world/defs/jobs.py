import dagster as dg

print_hello = dg.AssetSelection.assets('hello')
print_hello_job = dg.define_asset_job(name ='print_hello_job', selection=print_hello)

print_world = dg.AssetSelection.assets('world')
print_world_job = dg.define_asset_job(name ='print_world_job', selection=print_world)

