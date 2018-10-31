import os
import requests

from vmware.vapi.lib import connect
from vmware.vapi.security.user_password import \
    create_user_password_security_context
from vmware.vapi.stdlib.client.factories import StubConfigurationFactory

NSX_HOST = 'psrvwl02nsx0701.sccloudinfra.net'
TCP_PORT = '443'
USER = 'admin'
GOPASS_CREDENTIAL = 'PKS/NSX-T/admin'
PROXY = {'https': 'http://localhost:5001'}


def create_api_connection():
    session = requests.session()
    session.proxies.update(PROXY)
    session.verify = False

    nsx_url = 'https://%s:%s' % (NSX_HOST, TCP_PORT)
    connector = connect.get_requests_connector(
        session=session, msg_protocol='rest', url=nsx_url)
    stub_config = StubConfigurationFactory.new_std_configuration(connector)
    security_context = create_user_password_security_context(
        USER, os.popen("gopass " + GOPASS_CREDENTIAL).read())
    connector.set_security_context(security_context)

    return stub_config
