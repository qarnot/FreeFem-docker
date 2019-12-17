#!/usr/bin/env python

import qarnot
conn = qarnot.connection.Connection(client_token="xxxx_mytoken_xxxx")
task = conn.create_task('helloworld', 'docker-batch', 1)
task.constants['DOCKER_CMD'] = 'echo hello world!'
task.run()
print(task.stdout())
