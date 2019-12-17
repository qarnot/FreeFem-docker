#!/usr/bin/env python

import qarnot

conn = qarnot.connection.Connection(client_token="<<<XXX put your token here XXX>>>")

bucket = conn.create_bucket("Fibonacci_code")
bucket.sync_directory("resources")

task = conn.create_task('run_Fibo', 'python', 3)

task.resources = [ bucket ]

task.constants['PYTHON_SCRIPT'] = 'Fibonacci.py 1,21,32 ${INSTANCE_ID}'

task.run()

print(task.stdout())
print(task.stderr())

