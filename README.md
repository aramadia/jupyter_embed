Uses devenv with flakes

```
direnv allow


# Check if jupyter and proivsioner installed
$ jupyter kernelspec provisioners
Available kernel provisioners:
  existing-provisioner    jupyter_existing_provisioner:ExistingProvisioner
  local-provisioner       jupyter_client.provisioning:LocalProvisioner
```

```
# Terminal one
python start_kernel.py


# Second terminal

jupyter lab --KernelProvisionerFactory.default_provisioner_name=existing-provisioner

```


