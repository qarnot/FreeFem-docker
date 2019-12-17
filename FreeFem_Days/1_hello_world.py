#!/usr/bin/env python3

import qarnot
conn = qarnot.connection.Connection(client_token="<<<XXX put your token here XXX>>>")
task = conn.create_task('helloworld', 'docker-batch', 1)
task.constants['DOCKER_CMD'] = 'echo hello world!'
task.run()
print(task.stdout())
