import json
import yaml
import pydot
 
from yaml.loader import SafeLoader

with open('story-map.yaml','r') as f:
  storymap_dict = yaml.load(f, Loader=SafeLoader)

json_formatted = json.dumps(storymap_dict, indent=2)
print(json_formatted)
print()

plotlines = {}
with open('output.gv', 'w') as f:
  f.write("graph storymap {\n  rankdir=\"LR\"\n")
  for plotline in storymap_dict:
    plotpoints = storymap_dict[plotline]
    # f.write("  \"{0}\" [label=\"{0}\",URL=\"www.google.com\"]\n".format(nodekey))
    f.write("  \"{0}\" [label=\"{0}\"]\n".format(plotline))
    for point in plotpoints:
      print(point)
      
      

# graph = pydot.graph_from_dot_file("output.gv")[0]

# graph.write_pdf("output.pdf")