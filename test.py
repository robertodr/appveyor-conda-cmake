import sys
import subprocess
import shlex

command = 'ls -l'

cmd = shlex.split(command)

result = subprocess.run(cmd,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        universal_newlines=True)

print('stdout', result.stdout)
print('stderr', result.stderr)

sys.exit(0)
