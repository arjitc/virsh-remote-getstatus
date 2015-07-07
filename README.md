# virsh-remote-getstatus
Grab status of a virsh machine via URL

## Requirements
* Flask
* Python

## Configuration
Edit status.py (Line 7), change the key to something else apart from "test" and replace "YOUR_IP_HERE" with your IP address

## Running
> python status.py

> root@nc2-kvm:~# python status.py
> * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 
 Goto http://your.ip.address:5000/status/KVMID/KEY
 
 * KVMID = kvm(id), so if your KVM's name is kvm180, the KVMID becomes just "180"
 * KEY = the key you set at the configuration step above
 
## Sample output

* If the maching is running, the output will be just: running
* If the machine is offline, the output will be just: shut
* If the machine is missing, the output will be just: missing
