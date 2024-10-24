from ncclient import manager
import xmltodict

m = manager.connect(
    host="10.0.15.189",
    port=830,
    username="admin",
    password="cisco",
    hostkey_verify=False
    )


def getinterface():
    netconf_filter = """
    <filter>
        <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>Loopback65070165</name>
            </interface>
        </interfaces-state>
    </filter>
    """
    netconf_reply = m.get(filter=netconf_filter)
    response_dict = xmltodict.parse(netconf_reply.xml)
    interface_data = response_dict.get("rpc-reply", {}).get("data", {})
    if interface_data:
        return True
    else:
        return False

def create():
    netconf_config = """ 
    <config>def netconf_edit_config(netconf_config):
    return  m.<!!!REPLACEME with the proper Netconf operation!!!>(target="<!!!REPLACEME with NETCONF Datastore!!!>", config=<!!!REPLACEME with netconf_config!!!>)
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <interface>
                <Loopback>
                    <name>Loopback65070165</name>
                    <description>created loopback by NETCONF</description>
                    <ip>
                        <address>
                            <primary>
                                <address>172.30.165.1</address>
                                <mask>255.255.255.0</mask>
                            </primary>
                        </address>
                    </ip>
                </Loopback>
            </interface>
        </native>
    </config>
    """
    have = getinterface()
    
    if have == False:
        netconf_reply = netconf_edit_config(netconf_config)
        xml_data = netconf_reply.xml
        if '<ok/>' in xml_data:
            return "Interface loopback 65070165 is created successfully"
    else:
        return "Cannot create: Interface loopback 65070165"


def delete():
    netconf_config = """
    <config>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <interface>
                <Loopback operation="delete">
                    <name>Loopback65070165</name>
                </Loopback>
            </interface>
        </native>
    </config>
    """

    try:
        netconf_reply = netconf_edit_config(netconf_config)
        xml_data = netconf_reply.xml
        if '<ok/>' in xml_data:
            return "Interface loopback 65070165 is deleted successfully"
    except:
        return "Cannot delete: Interface loopback 65070165"

def enable():
    netconf_config = """
    <config>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <interface>
                <Loopback>
                    <name>Loopback65070165</name>
                    <description>Enabled via NETCONF</description>
                    <shutdown operation="delete"/> 
                </Loopback>
            </interface>
        </native>
    </config>
    """

    have = getinterface()
    if have == False:
        return "Cannot enable: Interface loopback 65070165"
    else:
        netconf_reply = netconf_edit_config(netconf_config)
        xml_data = netconf_reply.xml
        print("Response from the device:")
        print(xml_data)
        if '<ok/>' in xml_data:
            return "Interface loopback 65070165 is enabled successfully"


def disable():
     netconf_config = """
    <config>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <interface>
                <Loopback>
                    <name>Loopback65070165</name>
                    <description>Disabled via NETCONF</description>
                    <shutdown/>
                </Loopback>
            </interface>
        </native>
    </config>
    """

    have = getinterface()
    if have == False:
        return "Cannot disable: Interface loopback 65070165"
    else:
        netconf_reply = netconf_edit_config(netconf_config)
        xml_data = netconf_reply.xml
        if '<ok/>' in xml_data:
            return "Interface loopback 65070165 is shutdowned successfully"

def netconf_edit_config(netconf_config):
    return  m.edit_config(target="running", config=netconf_config)


def status():
    netconf_filter = 
    """
    <filter>
        <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>Loopback65070165</name>
            </interface>
        </interfaces-state>
    </filter>
    """
    netconf_reply = m.get(filter=netconf_filter)
    netconf_reply_dict = xmltodict.parse(netconf_reply.xml)
    interface_data = netconf_reply_dict.get("rpc-reply", {}).get("data", {})
    if(interface_data):
        interface_data = interface_data.get("interfaces-state", {}).get("interface", {})
        admin_status = interface_data.get("admin-status")
        oper_status = interface_data.get("oper-status")
        name_interface = interface_data.get("name").get("#text")
        print(admin_status)
        print(oper_status)
        if (admin_status == 'up' and oper_status == 'up' and name_interface == 'Loopback65070165'):
            return "Interface loopback 65070165 is enabled"
        elif (admin_status == 'down' and oper_status == 'down' and name_interface == 'Loopback65070165'):
            return "Interface loopback 65070165 is disabled"
        elif (name_interface != 'Loopback65070165'):
            return "No Interface loopback 65070165"
    else:
        return "No Interface loopback 65070165"
