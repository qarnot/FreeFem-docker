#!/usr/bin/env python3

import qarnot
conn = qarnot.connection.Connection(client_token="<<<XXX put your token here XXX>>>")
task = conn.create_task('helloworld pro', 'docker-batch', 4)
task.constants['DOCKER_CMD'] = 'echo hello world from Instance number ${INSTANCE_ID}!'
task.run()
