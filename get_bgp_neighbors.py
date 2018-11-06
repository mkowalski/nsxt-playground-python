from api_connector import create_api_connection
from vmware.vapi.bindings.struct import PrettyPrinter

from com.vmware.nsx.logical_routers.routing.bgp.neighbors_client import Status as BGPStatus


def main():
    connection = create_api_connection()

    bgp_svc = BGPStatus(connection)
    result = bgp_svc.list(
        logical_router_id='eb18c105-521a-4ca1-a7d7-ed51d93ed718',
        source='realtime'
    )

    pp = PrettyPrinter()
    pp.pprint(result)


if __name__ == "__main__":
    main()
