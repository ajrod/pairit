import subprocess
import json
import sys

p = subprocess.Popen(["pyflakes", sys.argv[1]], stdout=subprocess.PIPE)

out, err = p.communicate()

data = {}


out = out.split("\n")[:-1]

for error in out:
	
	error = error.split(":")
	line = error[1]
	errormsg = error[2]
	data[line] = errormsg.strip()

print json.dumps(data)
