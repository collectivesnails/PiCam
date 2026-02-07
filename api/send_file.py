# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "os",
# ]
# ///
import vault_dir as vault
import os

class Immich:

    def __init__(self):
        self = self

    def send_file(self, file):
        host = vault.immich_host
        api_key = vault.api_key
        os.system(f'immich login-key {host} {api_key}')
        os.system(f'immich upload {file} --album-name "Pi Cam"')
        return file
