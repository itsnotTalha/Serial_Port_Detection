import os

def get_tty_from_port(port_id):

    base_path = f"/sys/bus/usb/devices/{port_id}"
    
    if not os.path.exists(base_path):
        return None

    for subdir in os.listdir(base_path):
        if ":" in subdir:
            interface_path = os.path.join(base_path, subdir)
            
            tty_class_path = os.path.join(interface_path, "tty")
            
            if os.path.exists(tty_class_path):
                tty_names = os.listdir(tty_class_path)
                if tty_names:
                    return tty_names[0] 

    return None

# Usage

port_map = {
    'USB3_PORT1': '3-1',
    'USB3_PORT1_1': '3-1.1',
    'USB3_PORT1_2': '3-1.2',
    'USB3_PORT1_3': '3-1.3',
    'USB3_PORT1_4': '3-1.4',
    'USB3_PORT2': '3-2',
    'USB3_PORT2_1': '3-2.1',
    'USB3_PORT2_2': '3-2.2',
    'USB3_PORT2_3': '3-2.3',
    'USB3_PORT2_4': '3-2.4',
}

device_name = get_tty_from_port(port_map['USB3_PORT2'])

if device_name:
    print(f"Port {port_map['USB3_PORT1']} is mapped to /dev/{device_name}")
else:
    print(f"No serial device found on port {port_map['USB3_PORT1']}")
