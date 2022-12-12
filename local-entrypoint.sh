#!/bin/bash
# if any of the commands in your code fails for any reason, the entire script fails
set -o errexit
# fail exit if one of your pipe command fails
set -o pipefail
# exits if any of your variables is not set
set -o nounset

mysql_ready() {
python << END

import sys

import pymysql.cursors

try:
    connection = pymysql.connect(host="${SQL_HOST}",
                                user="${SQL_USER}",
                                password="${SQL_PASSWORD}",
                                database="${SQL_DATABASE}",
                                cursorclass=pymysql.cursors.DictCursor)
except:
    sys.exit(-1)
sys.exit(0)

END
}

until mysql_ready; do
  >&2 echo '[LESSERY] - Waiting for Mysql to become available...'
  sleep 1
done
>&2 echo '[LESSERY] - Mysql is available'

uvicorn src.main:app --reload --workers 1 --host 0.0.0.0 --port 8000