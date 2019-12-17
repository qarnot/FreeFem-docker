#!/usr/bin/env python3

import qarnot
conn = qarnot.connection.Connection(client_token="<<<XXX put your token here XXX>>>")

input_bucket = conn.create_bucket('demo_text_input_bucket')
input_bucket.add_file('script')
input_bucket.add_file('texte.txt')

task = conn.create_task('text_analysis', 'docker-batch', 3)
task.resources.append(input_bucket)
task.constants['DOCKER_CMD'] = './script'
task.run()
