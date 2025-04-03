from lib.state.state import State
import graphviz

def draw_dag_image(dag_base, segmentName="dag"):
    dag = dag_base.getRoot()
    filename = f"segment/{segmentName}/diagram/{dag_base.name if dag_base.name != None else 'dag'}"

    dot = graphviz.Digraph(comment='DAG', format='png')
    visited_states = set()  # Set to track visited states

    def add_nodes_edges(state, dot):
        if state in visited_states:  # Skip if already visited
            return
        visited_states.add(state)  # Mark state as visited

        node_name = f"{id(state)}"
        dot.node(node_name, f"{state.name or 'State'}\\n{state.des or ''}", shape='box', style='filled', fillcolor='green')

        # Add edges for bind operations
        for i, listener in enumerate(state.listeners):
            op_node_name = f"{id(state)}-op-{i}"
            op_name = getattr(listener, '__name__', 'Operator')
            node_color = 'lightcoral' if "filter" in op_name.lower() else 'white'
            dot.node(op_node_name, f"{op_name}", style='filled', fillcolor=node_color, fontcolor='black')
            dot.edge(node_name, op_node_name)
            node_name = op_node_name

        for listener in state.join_point:
            for s in dag.list_state:
                if s.emit == listener:
                    child_node_name = f"{id(s)}"
                    dot.edge(node_name, child_node_name)
                    add_nodes_edges(s, dot)

    add_nodes_edges(dag.getRoot(), dot)
    dot.render(filename, view=False)


def JoinPoint(name, des,*states) -> State:
    roots = {x.getRoot() for x in states}
    combined_state = State(states[0], name, des)
    for root in roots:
        root.list_state.append(combined_state)
    for state in states:
        state.join_point.append(combined_state.emit)
    return combined_state