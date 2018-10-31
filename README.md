# nsx-t-playground

## Upstream samples

https://github.com/vmwaresamples/nsx-t/tree/master/python

## Installation

https://my.vmware.com/group/vmware/details?downloadGroup=NSX-T-230-SDK-PYTHON&productId=673

```bash
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install lib/*.whl
```

## Run me

```bash
$ ssh -L 5001:100.104.252.4:3128 omg.charon-123.appcloud.swisscom.com
$ python sample.py
```

The test script should log into NSX-T using the local proxy over SSH and list all the existing logical switches.
