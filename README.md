Uses devenv with flakes

Shamlessly stolen from https://github.com/sv99/jupyter_existing_provisioner, but fixed issues to make it work with the latest jupyter_client 8

```
direnv allow


# Check if jupyter and proivsioner installed
jupyter kernelspec provisioners

Available kernel provisioners:
  existing-provisioner    jupyter_existing_provisioner:ExistingProvisioner
  local-provisioner       jupyter_client.provisioning:LocalProvisioner
```

```
# Terminal one
python start_kernel.py


# Second terminal

jupyter lab --KernelProvisionerFactory.default_provisioner_name=embed

# Colab

jupyter lab --KernelProvisionerFactory.default_provisioner_name=embed --ServerApp.allow_origin='https://colab.research.google.com'

```

# Don't think its needed
pip install jupyter_contrib_nbextensions 
jupyter contrib nbextension install --user 
jupyter nbextensions_configurator enable --user

