import os
from project import app

docker_file = 'Dockerfile'
source_dir = os.path.abspath(os.curdir)
destination_dir = os.path.join(source_dir, '../mysql')

if not os.path.isdir(destination_dir):
    os.makedirs(destination_dir)

with open(os.path.join(destination_dir, docker_file), 'w') as mysql_dockerfile:
    mysql_dockerfile.write('FROM mysql:8.0')
    mysql_dockerfile.write('\n')
    mysql_dockerfile.write('\n# Set environment variables')
    mysql_dockerfile.write('\nENV MYSQL_USER {}'.format(app.config['MYSQL_USER']))
    mysql_dockerfile.write('\nENV MYSQL_PASSWORD {}'.format(app.config['MYSQL_PASSWORD']))
    mysql_dockerfile.write('\nENV MYSQL_DB {}'.format(app.config['MYSQL_DB']))
    mysql_dockerfile.write('\n')
