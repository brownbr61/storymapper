import json
import yaml
import pydot
import pygraphviz
 
from yaml.loader import SafeLoader

with open('test.yaml','r') as f:
  storymap_dict = yaml.load(f, Loader=SafeLoader)

json_formatted = json.dumps(storymap_dict, indent=2)
print(json_formatted)
print()

plotlines = {}
with open('output.gv', 'w') as f:
  f.write("graph storymap {\n  rankdir=\"LR\"\n")
  for nodekey in storymap_dict:
    node = storymap_dict[nodekey]
    plotline = node["plotline"]
    f.write("  \"{0}\" [label=\"{0}\",URL=\"www.google.com\"]\n".format(nodekey))
    if plotline not in plotlines.keys():
      plotlines[plotline] = dict()
    chapter = int(node["chapter"])
    if chapter not in plotlines[plotline]:
      plotlines[plotline][chapter] = list()
    plotlines[plotline][chapter].append(nodekey)
  for line in plotlines:
    write_line = "  "
    plotline = plotlines[line]
    keys = list(plotline.keys())
    keys.sort()
    pl = {i: plotline[i] for i in keys}
    plotline = pl
    for chapter in plotline:
      for scene in plotline[chapter]:
        write_line = write_line + "\"{}\" -- ".format(scene)
    write_line = write_line[:-4]
    f.write("{}\n".format(write_line))
  f.write("}")

graph = pydot.graph_from_dot_file("output.gv")[0]

graph.write_pdf("output.pdf")