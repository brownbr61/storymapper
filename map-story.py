import json
import yaml
import pydot
 
from yaml.loader import SafeLoader

with open('story-map.yaml','r') as f:
  storymap_dict = yaml.load(f, Loader=SafeLoader)

json_formatted = json.dumps(storymap_dict, indent=2)
print(json_formatted)
print()

graph_intro = '''graph G {
newrank=true;
rankdir="TD";
compound=true;
node [shape=box];
edge [dir=none];

'''
plotlines = []
with open('output.gv', 'w') as f:
  f.write(graph_intro)
  plotline_ct = 0
  # for index in range(0,len(storymap_dict)):
  for plotline in storymap_dict:
    plotlines.append(plotline)
  write_line = ""
  for plotline in plotlines:
    write_line = write_line + "\"{}\" -- ".format(plotline)
  write_line = write_line[:-4]
  f.write ("{} [style=invis];\n\n".format(write_line))
  f.write("subgraph cluster_plotlines {\n")
  for plotline in storymap_dict:
    plotpoints = storymap_dict[plotline]
    f.write("subgraph cluster_plotline{0} {{\nrank = same; \"{1}\";\n".format(plotline_ct, plotline))

    plotpoint_ct = 0
    for plotpoint in plotpoints:
      if type(plotpoint) == type(dict()):
        f.write("plotline{0}point{1} [label=\"{2}\"];\n".format(plotline_ct, plotpoint_ct, plotpoint["name"]))
        plotpoint_ct += 1
    write_line = "{{ rank = same; \"{}\" -- ".format(plotline)
    for i in range(0,len(plotpoints)):
      if type(plotpoints[i]) == type(dict()):
        write_line = write_line + "\"plotline{0}point{1}\" -- ".format(plotline_ct, i)
    write_line = write_line[:-4]
    f.write ("{0}; }}\n".format(write_line))
    plotline_ct += 1
    f.write("}\n")
  f.write("}\n")
  f.write("}\n")
      
      

graph = pydot.graph_from_dot_file("output.gv")[0]

graph.write_pdf("output.pdf")