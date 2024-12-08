# Jupyter Embedded Kernel Provisioner

## Why?
Imagine you are working with a complex python program that has some gnarly initialization.  You want to start debugging in the middle with it.  You know of pdb.set_trace or IPython, but all you get is a weak terminal interface.

Jupyter ecosystem is rich but you are usually faced with the dichotomy of notebooks and programs.  WHat if you can install a kernel in the middle of a running program, and hook up Colab/VsCode (way better than Jupyter UI) right in the middle of it?  Yes it works

You just need to add these lines to wherever you want to spawn a kernel
```py
from IPython import embed_kernel; embed_kernel()
```


## Getting Started (Nix)
Assumes you are familiar and installed Nix.

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

## Non Nix Workflow
`pip install` this package with jupyter.

## Contributing
- Use `pip install .` to rebuild the provisioner
