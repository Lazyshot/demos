#!/usr/bin/env python

import config

from comodit_client.api import Client
from comodit_client.api.importer import Import

def clean_up():
    # Connect to the ComodIT API
    client = Client(config.endpoint, config.username, config.password)
    org = client.get_organization(config.organization)

    print "Cleaning up ComodIT..."

    # Delete environment (if empty)
    env = org.environments().delete('Render Farm')

    # Delete applications
    org.applications().delete('NFS Server')
    org.applications().delete('NFS Client')
    org.applications().delete('Blender')

    print "Done."


if __name__ == '__main__':
    try:
        clean_up()
    except Exception as e:
        print e
