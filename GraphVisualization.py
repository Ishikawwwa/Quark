from pyvis.network import Network
#import networkx as nx

net = Network('1080px', '1920px', bgcolor="#222222", font_color="white", select_menu=True)

net.add_node(1, label="Skill 1", title="Link to Skill 1 guide")
net.add_node(2, label="Skill 2", title="Link to Skill 2 guide")
net.add_node(3, label="Skill 3", title="Link to Skill 3 guide")

net.add_edge(1, 3)

net.barnes_hut()

net.show("myquark.html", notebook=False)