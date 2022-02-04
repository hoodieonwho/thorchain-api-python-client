import siaskynet as skynet
import os
import pytest
from pytest import ExitCode
import json
import fileinput


def update_client(client):
    os.system(f'bash fetch_swagger_json.sh {client}')
    sky_client = skynet.SkynetClient()
    link = f'https://siasky.net/{sky_client.upload_file(f"{client}.json")[6:]}'
    os.system(f'bash fetch_swagger_client.sh {client} {link} python')
    # assert pytest.main(["-x", f"{client}_client/test"]) == ExitCode.OK
    with fileinput.FileInput(f'{client}_client/setup.py', inplace=True) as file:
        for line in file:
            if "VERSION = " in line:
                print(f'VERSION = "{version[client]}"')
            else:
                print(line)


if __name__ == '__main__':
    with open('version.json', 'r') as json_file:
        version = json.load(json_file)
        # if we update both clients at the same time, there will be error due to the way
        # pytest.main works
        for client in version:
            try:
                file = open(f'{client}_client/setup.py', 'r+')
                for line in file:
                    if "VERSION = " in line:
                        if version[client] != line.split("VERSION = ")[1].split('"')[1]:
                            print(f"need to update {client}")
                            file.close()
                            update_client(client)
                            os.system(f'python {client}_client/setup.py sdist')
                        else:
                            print(f"no need to update {client}")
                            file.close()
                        break
            except FileNotFoundError:
                print(f"{client} not found, generating")
                update_client(client)
                os.system(f'python {client}_client/setup.py sdist')