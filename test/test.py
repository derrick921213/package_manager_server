import subprocess
import json
cmd = f"temp=/tmp;a=`ls $temp | grep '^dpm_test'`;cat `tar -tf $temp/$a | grep 'package.json'`"
output = subprocess.Popen(
    cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
data = output.stdout.read().decode('utf-8')
data_json = json.loads(data)
print(data_json['version'])
