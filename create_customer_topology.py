from api_connector import create_api_connection
from vmware.vapi.bindings.struct import PrettyPrinter

from com.vmware.nsx_client import LogicalPorts
from com.vmware.nsx_client import LogicalRouterPorts
from com.vmware.nsx_client import LogicalRouters
from com.vmware.nsx_client import LogicalSwitches

from com.vmware.nsx.model_client import IPSubnet
from com.vmware.nsx.model_client import LogicalPort
from com.vmware.nsx.model_client import LogicalRouter
from com.vmware.nsx.model_client import LogicalRouterDownLinkPort
from com.vmware.nsx.model_client import LogicalRouterPort
from com.vmware.nsx.model_client import LogicalSwitch


NAME_PREFIX = 'czokoszok-'
TRANSPORT_ZONE_ID = '26430205-f40b-4754-ba02-6726f5641bc4'

CONNECTION = None
RESOURCES = []
SVC_LOGICAL_SWITCHES = None
SVC_LOGICAL_ROUTERS = None
SVC_LOGICAL_ROUTER_PORTS = None
SVC_LOGICAL_PORTS = None


def prepare_connectors():
    global CONNECTION
    CONNECTION = create_api_connection()

    global SVC_LOGICAL_SWITCHES
    SVC_LOGICAL_SWITCHES = LogicalSwitches(CONNECTION)
    global SVC_LOGICAL_ROUTERS
    SVC_LOGICAL_ROUTERS = LogicalRouters(CONNECTION)
    global SVC_LOGICAL_ROUTER_PORTS
    SVC_LOGICAL_ROUTER_PORTS = LogicalRouterPorts(CONNECTION)
    global SVC_LOGICAL_PORTS
    SVC_LOGICAL_PORTS = LogicalPorts(CONNECTION)


def delete_resource(resource_type, resource_id):
    if isinstance(resource_type, type(LogicalRouter)):
        SVC_LOGICAL_ROUTERS.delete(resource_id)
    elif isinstance(resource_type, type(LogicalSwitch)):
        SVC_LOGICAL_SWITCHES.delete(resource_id)
    elif isinstance(resource_type, type(LogicalRouterPort)):
        SVC_LOGICAL_ROUTER_PORTS.delete(resource_id)
    elif isinstance(resource_type, type(LogicalPort)):
        SVC_LOGICAL_PORTS.delete(resource_id)
    else:
        raise Exception("No idea what happens")


def main():
    prepare_connectors()

    resource = LogicalRouter(
        router_type=LogicalRouter.ROUTER_TYPE_TIER0,
        display_name=NAME_PREFIX + "t0",
        failover_mode=LogicalRouter.FAILOVER_MODE_PREEMPTIVE
    )
    new_t0 = SVC_LOGICAL_ROUTERS.create(resource)
    RESOURCES.append((type(new_t0), new_t0.id))

    resource = LogicalRouter(
        router_type=LogicalRouter.ROUTER_TYPE_TIER1,
        display_name=NAME_PREFIX + "t1-mars",
        failover_mode=LogicalRouter.FAILOVER_MODE_PREEMPTIVE
    )
    new_t1_1 = SVC_LOGICAL_ROUTERS.create(resource)
    RESOURCES.append((type(new_t1_1), new_t1_1.id))

    resource = LogicalRouter(
        router_type=LogicalRouter.ROUTER_TYPE_TIER1,
        display_name=NAME_PREFIX + "t1-snickers",
        failover_mode=LogicalRouter.FAILOVER_MODE_PREEMPTIVE
    )
    new_t1_2 = SVC_LOGICAL_ROUTERS.create(resource)
    RESOURCES.append((type(new_t1_2), new_t1_2.id))

    resource = LogicalSwitch(
        transport_zone_id=TRANSPORT_ZONE_ID,
        admin_state=LogicalSwitch.ADMIN_STATE_UP,
        replication_mode=LogicalSwitch.REPLICATION_MODE_MTEP,
        display_name=NAME_PREFIX + "ls-mars",
    )
    new_ls_1 = SVC_LOGICAL_SWITCHES.create(resource)
    RESOURCES.append((type(new_ls_1), new_ls_1.id))

    resource = LogicalSwitch(
        transport_zone_id=TRANSPORT_ZONE_ID,
        admin_state=LogicalSwitch.ADMIN_STATE_UP,
        replication_mode=LogicalSwitch.REPLICATION_MODE_MTEP,
        display_name=NAME_PREFIX + "ls-snickers",
    )
    new_ls_2 = SVC_LOGICAL_SWITCHES.create(resource)
    RESOURCES.append((type(new_ls_2), new_ls_2.id))

    print(RESOURCES)

    for elem in RESOURCES:
        delete_resource(elem[0], elem[1])

    # pp = PrettyPrinter()
    # pp.pprint(result)


if __name__ == "__main__":
    main()
