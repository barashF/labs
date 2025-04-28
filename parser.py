class YamlConverter:
    def __init__(self):
        self._indent_step = 2

    def read(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            return self._build_structure([ln.rstrip() for ln in f if ln.strip()])
    
    def _build_structure(self, lines):
        root = []
        stack = [{'level': -1, 'node': root, 'type': list}]
        
        for line in lines:
            indent = len(line) - len(line.lstrip())
            content = line.lstrip()
            
            while indent <= stack[-1]['level']:
                stack.pop()
            
            current = stack[-1]
            
            if content.startswith('- '):
                item = self._create_item(content[2:], indent + self._indent_step)
                current['node'].append(item)
                if isinstance(item, dict):
                    stack.append({'level': indent, 'node': item, 'type': dict})
            else:
                key, _, value = content.partition(':')
                key = key.strip()
                
                if not key:
                    continue
                
                if not value:
                    value = {}
                    stack.append({'level': indent, 'node': value, 'type': dict})
                else:
                    value = self._parse_value(value.strip())
                
                if isinstance(current['node'], list):
                    current['node'][-1][key] = value
                else:
                    current['node'][key] = value
        
        return root[0] if len(root) == 1 else root

    def _create_item(self, content, next_indent):
        if ':' in content:
            node = {}
            key, _, value = content.partition(':')
            node[key.strip()] = self._parse_value(value.strip())
            return node
        return self._parse_value(content)
    
    def _parse_value(self, value):
        if not value:
            return None
        for converter in [int, float]:
            try:
                return converter(value)
            except:
                continue
        return value.strip("'\"")
    
    def write(self, data):
        return '\n'.join(self._format_section(data))

    def _format_section(self, data, indent=0):
        lines = []
        space = ' ' * indent
        
        if isinstance(data, dict):
            for k, v in data.items():
                if isinstance(v, (dict, list)):
                    lines.append(f"{space}{k}:")
                    lines.extend(self._format_section(v, indent + self._indent_step))
                else:
                    lines.append(f"{space}{k}: {v}")
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, (dict, list)):
                    lines.append(f"{space}-")
                    lines.extend(self._format_section(item, indent + self._indent_step))
                else:
                    lines.append(f"{space}- {item}")
        else:
            lines.append(f"{space}{data}")
        
        return lines

converter = YamlConverter()
d = converter.read("C:/Users/artem/Desktop/PDF-Parser/0.yml")
print(d)