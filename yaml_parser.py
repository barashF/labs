class YamlParser:
    class Node:
        def __init__(self, indent, parent=None):
            self.indent = indent
            self.parent = parent
            self.data = [] if parent and parent.is_list() else {}

        def is_list(self):
            return isinstance(self.data, list)

        def add_item(self, key, value):
            if self.is_list():
                self.data.append(value)
            else:
                self.data[key] = value

    def __init__(self):
        self.root = None
        self.current_node = None

    def load(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = [ln.rstrip() for ln in f if ln.strip()]

        for line in lines:
            indent = len(line) - len(line.lstrip())
            line = line.lstrip()

            if not self.current_node:
                self._init_root(line, indent)
                continue

            self._adjust_node_level(indent)

            if line.startswith('- '):
                self._process_list_item(line[2:], indent)
            else:
                self._process_dict_item(line, indent)

        return self.root.data if self.root else {}

    def _init_root(self, first_line, indent):
        if first_line.startswith('- '):
            self.root = self.Node(indent)
            self.root.data = []
            self.current_node = self.root
            self._process_list_item(first_line[2:], indent)
        else:
            self.root = self.Node(indent)
            self.current_node = self.root
            self._process_dict_item(first_line, indent)

    def _adjust_node_level(self, indent):
        while self.current_node.parent and indent <= self.current_node.parent.indent:
            self.current_node = self.current_node.parent

    def _process_list_item(self, content, indent):
        if ':' in content:
            key, value = content.split(':', 1)
            new_node = self.Node(indent, self.current_node)
            new_node.data = {key.strip(): self._parse_value(value.strip())}
            self.current_node.add_item(None, new_node.data)
            self.current_node = new_node
        else:
            value = self._parse_value(content)
            self.current_node.add_item(None, value)

    def _process_dict_item(self, line, indent):
        key, sep, value = line.partition(':')
        key = key.strip()
        value = value.strip()

        if not sep:
            return

        if not value:
            new_node = self.Node(indent, self.current_node)
            self.current_node.add_item(key, new_node.data)
            self.current_node = new_node
        else:
            self.current_node.add_item(key, self._parse_value(value))

    def _parse_value(self, value):
        if value.lower() in {'true', 'false'}:
            return value.lower() == 'true'
        if value in {'', '~'}:
            return None
        if value[0] in {'"', "'"}:
            return value[1:-1]
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value

    def save(self, data, file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(self._serialize(data))

    def _serialize(self, data, indent=0):
        output = []
        space = ' ' * indent

        if isinstance(data, dict):
            for key, value in data.items():
                output.append(f"{space}{key}:")
                output.append(self._serialize(value, indent + 2))
        elif isinstance(data, list):
            for item in data:
                prefix = f"{space}- "
                if isinstance(item, (dict, list)):
                    output.append(f"{prefix.rstrip()}")
                    output.append(self._serialize(item, indent + 2))
                else:
                    output.append(f"{prefix}{self._format_scalar(item)}")
        else:
            output.append(f"{space}{self._format_scalar(data)}")

        return '\n'.join(output)

    def _format_scalar(self, value):
        if value is None:
            return '~'
        if isinstance(value, bool):
            return 'true' if value else 'false'
        if isinstance(value, (int, float)):
            return str(value)
        return f'"{value}"' if ' ' in value else value

converter = YamlParser()
print(converter.load("C:/Users/artem/Desktop\PDF-Parser/2.yml"))
d = {'router': {'hostname': 'CiscoRouter1', 'interfaces': {'GigabitEthernet0/0': {'ip_address': '192.168.1.1', 'subnet_mask': '255.255.255.0', 'description': 'WAN Interface', 'status': 'up', 'mtu': 1500, 'GigabitEthernet0/1': {'ip_address': '192.168.2.1', 'subnet_mask': '255.255.255.0', 'description': 'LAN Interface', 'status': 'up', 'mtu': 1500}}, 'routing': {'static_routes': {'route1': {'destination_network': '0.0.0.0', 'subnet_mask': '0.0.0.0', 'next_hop': '192.168.1.254', 'route2': {'destination_network': '10.0.0.0', 'subnet_mask': '255.0.0.0', 'next_hop': '192.168.1.254'}}}}, 'dns': {'servers': {'primary': '8.8.8.8', 'secondary': '8.8.4.4'}}, 'access_lists': {'ACL_inbound': {'type': 'inbound', 'rules': {'rule1': {'action': 'permit', 'protocol': 'ip', 'source': 'any', 'destination': 'any', 'rule2': {'action': 'deny', 'protocol': 'ip', 'source': 'any', 
'destination': 'any'}}}}}}}}
converter.save(d, "C:/Users/artem/Desktop/PDF-Parser/test.yml")
