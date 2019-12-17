#!/usr/bin/env python3

import qarnot

# Enter client token here
conn = qarnot.connection.Connection(client_token='<<<XXX put your token here XXX>>>')

input_bucket = conn.create_bucket("freefem-input")
# Adds the resources found in a local file called freefem_resources to the bucket
input_bucket.sync_directory("freefem-resources")
output_bucket = conn.create_bucket("freefem-output")

task = conn.create_task("freefem", "docker-batch", 1)

# Appends the resources of the bucket to the task
task.resources.append(input_bucket)

task.results = output_bucket

task.constants["DOCKER_HOST"] = "localhost"
task.constants["DOCKER_REPO"] = "qarnotlab/freefem"
task.constants["DOCKER_TAG"] = "latest"

# Configure parameter to change the step depth (adding "-step PARAMETER_BETWEEN_0.1_AND_0.9_HERE")
task.constants["DOCKER_CMD"] = "/usr/freefem/bin/ff-mpirun -n 4 ./navierstokes.edp -v 0 -step 0.8"

task.submit()
