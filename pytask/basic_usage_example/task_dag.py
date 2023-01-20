import networkx as nx
import pytask


@pytask.mark.produces("dag.svg")
def task_draw_dag(produces):
    dag = pytask.build_dag({})

    nx.set_node_attributes(dag, "rectangle", "shape")
    nx.set_node_attributes(dag, "white", "color")
    nx.set_node_attributes(dag, "white", "fontcolor")
    nx.set_edge_attributes(dag, "white", "color")

    labels = {n: {"label": ""} for n in dag}
    nx.set_node_attributes(dag, labels)

    shapes_of_tasks = {n: {"shape": "hexagon"} for n in dag if "::" in n}
    nx.set_node_attributes(dag, shapes_of_tasks)

    graph = nx.nx_agraph.to_agraph(dag)
    graph.draw(produces, prog="dot", args='-Gbgcolor="transparent" -Gratio=9/16')


def get_label(node):
    if "::" in node:
        label = node.split("::")[-1]
    elif "/scipy" in node:
        label = "/".join(node.split("/")[-3:])
    else:
        label = "/".join(node.split("/")[-2:])
    label = label.replace('"', "")
    return label
