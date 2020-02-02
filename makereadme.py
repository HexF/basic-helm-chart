import sys
import pystache
import ruamel.yaml
import collections


tableHeader = "\n".join([
    "**Parameter** | **Description** | **Default**",
    "--- | --- | ---",
    ""
])

yaml = ruamel.yaml.YAML()

if len(sys.argv) != 5:
    raise ValueError("Invalid parameter length")

template = ""
chart = {}
values = {}

with open(sys.argv[1], 'r') as f:
    template = f.read()
with open(sys.argv[3], 'r') as f:
    chart = yaml.load(f.read())
with open(sys.argv[4], 'r') as f:
    values = yaml.load(f.read())

tableRows = []

def followPath(a, path):
    if len(path) == 0:
        return a
    return followPath(a[path[0]], path[1:])

def itr(a, path = []):
    for key, val in a.items():
        pth = path[:]
        pth.append(key)
        if isinstance(val, collections.OrderedDict) and len(val) > 0:
            itr(val, pth)
        else:
            v = val
            if isinstance(v, collections.OrderedDict) and len(v) == 0:
                v = "{}"
            if isinstance(v, list) and len(v) == 0:
                v = "[]"
            if not v:
                v = "nil"
            description = ""
            di = followPath(values, path).ca.items
            c = 0
            if key in di:
                while not di[key][c]:
                    c = c + 1
                    if c == len(di[key]):
                        c = 0
                        break
                if di[key][c]:
                    description = di[key][c]
                    if isinstance(description, list):
                        description = description[0]
                    description = description.value.strip().replace("\n", "").replace("#","",1)
            
            e = " | ".join(["`" + '.'.join(pth) + "`", description, "`" + str(v) + "`"])
            tableRows.append(e)

itr(values)

table = '\n'.join(tableRows)

chart["valuesTable"] = tableHeader + table

output = pystache.render(template, {'Chart': chart})


with open(sys.argv[2], 'w') as f:
    f.write(output)