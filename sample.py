from com.vmware.nsx_client import LogicalRouters
from com.vmware.nsx_client import LogicalSwitches
from vmware.vapi.bindings.struct import PrettyPrinter

from api_connector import create_api_connection


def main():
    connection = create_api_connection()

    # logicalswitches_svc = LogicalSwitches(connection)
    # result = logicalswitches_svc.list()

    logicalrouters_svc = LogicalRouters(connection)
    result = logicalrouters_svc.list()

    pp = PrettyPrinter()
    pp.pprint(result)


if __name__ == "__main__":
    main()
