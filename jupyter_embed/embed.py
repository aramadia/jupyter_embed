from jupyter_client import KernelProvisionerBase
from jupyter_client import find_connection_file
import logging
import json
import os

_log = logging.getLogger(__name__)


class EmbedProvisioner(KernelProvisionerBase):
    """
    A Kernel Provisioner that re-uses an existing kernel.
    The kernel connection file is set in the environment variable
    'EXISTING_CONNECTION_FILE'.
    """

    async def launch_kernel(self, cmd, **kwargs):
        # Connect to existing kernel
        connection_file = ""
        if "EXISTING_CONNECTION_FILE" in os.environ:
            kernel_file = os.environ["EXISTING_CONNECTION_FILE"]
            connection_file = find_connection_file(kernel_file)
        else:
            # find last started kernel-*.json in the runtime dir
            connection_file = find_connection_file()

        if not os.path.exists(connection_file):
            _log.warning(f"Jupyter connection file '{connection_file}' does not exist.")

        _log.info(f'Existing IPython kernel = {connection_file}')
        info = {}
        with open(connection_file) as f:
            info = json.load(f)
        if "key" in info:
            key = info["key"]
            if isinstance(key, str):
                key = key.encode()
            info["key"] = key
        print("Exiting Provisioner", str(info))
        return info

    async def pre_launch(self, **kwargs):
        kwargs = await super().pre_launch(**kwargs)
        kwargs.setdefault('cmd', None)
        return kwargs

    def has_process(self) -> bool:
        return True

    async def poll(self):
        pass

    async def wait(self):
        pass

    async def send_signal(self, signum: int):
        _log.warning(f"Cannot send signal: {signum}.")

    async def kill(self, restart=False):
        if restart:
            _log.warning("Cannot restart existing kernel.")

    async def terminate(self, restart=False):
        if restart:
            _log.warning("Cannot terminate existing kernel.")

    async def cleanup(self, restart):
        pass