from api_connector import create_api_connection
from vmware.vapi.bindings.struct import PrettyPrinter

from com.vmware.nsx_client import LogicalRouters as LogicalRouters
from com.vmware.nsx.logical_routers.nat_client import Rules as NatRules
from com.vmware.nsx.logical_routers.routing.bgp.neighbors_client import Status as BgpNeighborsStatus
from com.vmware.nsx.logical_routers.routing.advertisement_client import Rules as BgpAdvertisementRules
from com.vmware.nsx.logical_routers.routing.redistribution_client import Rules as BgpRedistributionRules
from com.vmware.nsx.logical_routers.routing.static_routes_client import BfdPeers as BfdPeers


LOGICAL_ROUTER_ID = 'eb18c105-521a-4ca1-a7d7-ed51d93ed718'


def main():
    connection = create_api_connection()
    pp = PrettyPrinter()

    pp.pprint(LogicalRouters(connection).get(logical_router_id=LOGICAL_ROUTER_ID))
    pp.pprint(NatRules(connection).list(logical_router_id=LOGICAL_ROUTER_ID))
    # pp.pprint(BgpAdvertisementRules(connection).get(logical_router_id=LOGICAL_ROUTER_ID))
    pp.pprint(BgpRedistributionRules(connection).get(logical_router_id=LOGICAL_ROUTER_ID))
    pp.pprint(BfdPeers(connection).list(logical_router_id=LOGICAL_ROUTER_ID))
    pp.pprint(BgpNeighborsStatus(connection).list(logical_router_id=LOGICAL_ROUTER_ID, source='realtime'))


if __name__ == "__main__":
    main()
