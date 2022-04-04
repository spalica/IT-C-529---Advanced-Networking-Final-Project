


class Switch:
    def __init__(self):
        pass
    def __str__(self):
        pass

class Interface:
    def __init__(self, name, speeds: list, medium: str):
        self.name = name
        self.speeds = speeds
        self.medium = medium        
        self.tagged_vlans = []
        self.untagged_vlans = []

class Cisco3750G(Switch):
    def __init__(self, hostname, management_ip):
        self.hostname = hostname
        self.management_ip = management_ip
        self.make = 'Cisco'
        self.model = '3750G'
        self.rj45_port_count = 48
        self.sfp_port_count = 4
        self.int_speeds = [1000, 100, 10]
        self.sfp_int_speeds = 1000, 10000
        self.interfaces = []

        # Add copper intrfaces
        for i in range(1, self.rj45_port_count + 1):
            self.interfaces.append(Interface(f'GigabitEthernet 1/0/{i}', self.int_speeds, 'copper'))

        # Add SFP interfaces
        for j in range(0, self.sfp_port_count):
            self.interfaces.append(Interface(f'TenGigabitEthernet {j + 1}', self.sfp_int_speeds, 'fiber'))

    def __str__(self):
        to_return = self.hostname + '\n'
        for i in self.interfaces:
            to_return += '\t' + i.name + '\n'
        return to_return


if __name__ == '__main__':
    sw1 = Cisco3750G('Hostname', '192.168.1.20')
    print(str(sw1))