import subprocess
import glob

password_db = {}
with open("password_db.txt") as cmudict:
    for cur_ln in cmudict:
        if not cur_ln:
            continue
        cur_ln_split = cur_ln.split()
        # print(cur_ln_split)
        host = cur_ln_split[0].strip()
        password = cur_ln_split[1].strip()

        password_db[host] = password
print(password_db)

hostsfile=open("telnet_target.txt", "r")
ini_file = glob.glob("*.ini")
kwds = {
    "stdout": subprocess.PIPE,
    "bufsize": 1,
    "close_fds": True,
    "universal_newlines": True,
}

#build commands
log_dir = '/Users/ezhou/Downloads/logger_test2'
commands = []
log_files = {}
hosts=hostsfile.readlines()
for host in hosts:
    # print(f'read target = {host}')
    cur_target = host.strip()
    if not cur_target or cur_target.startswith('#') or cur_target.startswith("/"):
        continue
    if cur_target not in password_db:
        continue
    for conf_fn in ini_file:
        # print(f'cur_conf = {conf_fn}')
        cur_cmd = ["python3", "telnet_logger.py"]
        cur_cmd.append("--host")
        cur_cmd.append(cur_target)
        cur_cmd.append("--password")
        cur_cmd.append(password_db[cur_target])
        cur_cmd.append("--cfg")
        cur_cmd.append(conf_fn)
        cur_cmd.append("--file-dir")
        cur_cmd.append(log_dir)
        print(cur_cmd)

        commands += [cur_cmd]

procs = [subprocess.Popen(cmd, **kwds) for cmd in commands]

# Join on proesses, reading stdout as we can
while procs:
    for p in procs:
        if p.poll() is not None:           # process ended
            procs.remove(p)                # remove the process
            print(f"Done: {p.args}")

print("all done!!!!")

