import os
import subprocess
import datetime

# MySQL connection config
db_user = "root"
db_password = "Secret5555"
db_name = "testdb"
host = "127.0.0.1"  # MUST be 127.0.0.1, not localhost, to force TCP
backup_dir = "backups"

# Create backup folder if it doesn't exist
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)

# Unique filename
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
backup_file = f"{backup_dir}/{db_name}_backup_{timestamp}.sql"

# Build mysqldump command
dump_command = [
    "mysqldump",
    "--protocol=TCP",
    f"-h{host}",
    f"-u{db_user}",
    f"-p{db_password}",
    db_name
]

# Run backup
with open(backup_file, "w") as f:
    result = subprocess.run(dump_command, stdout=f)

if result.returncode == 0:
    print(f" Backup complete: {backup_file}")
else:
    print(" Backup failed.")
