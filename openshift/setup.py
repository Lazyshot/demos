#!/usr/bin/env python

import config 

from comodit_client.api import Client
from comodit_client.api.collection import EntityNotFoundException
from comodit_client.api.importer import Import

def setup():
    # Connect to the ComodIT API
    client = Client(config.endpoint, config.username, config.password)
    org = client.get_organization(config.organization)

    print "Setting up ComodIT..."

    # Create environment (if not already present)
    try:
        org.environments().create("Openshift", "Environment containing the openshift cluster.")
    except:
        pass

    # Import applications
    importer = Import()
    importer.import_application(org, 'openshift-bind-server')
    importer.import_application(org, 'openshift-broker')
    importer.import_application(org, 'openshift-client')
    importer.import_application(org, 'openshift-dhcp-dns-config')
    importer.import_application(org, 'openshift-mcollective-client')
    importer.import_application(org, 'openshift-mcollective-node')
    importer.import_application(org, 'openshift-mongodb')
    importer.import_application(org, 'openshift-node')
    importer.import_application(org, 'openshift-rabbitmq-server')

    print "Done."


if __name__ == '__main__':
    try:
        setup()
    except Exception as e:
        print e