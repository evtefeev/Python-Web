from urllib.parse import urlparse

from config import URL

result = urlparse(URL)

PGUSER = result.username
PGPASSWORD = result.password
PGDB = result.path[1:]
PGHOST = result.hostname
PGPORT = result.port

print(f"""
user: {PGUSER}
pass: {PGPASSWORD}
host: {PGHOST}
port: {PGPORT}
""")

