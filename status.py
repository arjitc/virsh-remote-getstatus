import subprocess
from flask import Flask
app = Flask(__name__)

@app.route('/status/<vmid>/<key>')
def status(vmid, key):
    if key == "test":
     cmd = "/usr/bin/virsh list --all | grep kvm%s | awk {'print $3'}" % vmid
     p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
     (output, err) = p.communicate()
     if output == "":
      output = "missing"
     return output


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
