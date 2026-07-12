import subprocess
import sys

cmd = ['ls -lah /']
encoding = 'utf_8'
system = sys.platform

print(system)

if system == "win32":
    cmd = ['ping', '127.0.0.1']
    encoding = 'cp850'


proc = subprocess.run(
    cmd, capture_output=False,
    text=True, encoding=encoding,
    shell=True,
)

print()

print('args:', proc.args)
print('stderr:', proc.stderr)
print('stdout:', proc.stdout)
print('returncode:', proc.returncode)
