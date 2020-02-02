import sys
import ruamel.yaml

y = {}
with open(sys.argv[1],'r') as f:
    y = ruamel.yaml.YAML().load(f)

print(y[sys.argv[2]])