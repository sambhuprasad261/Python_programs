from graphviz import Digraph

def add_state(g, name, out, final=False):
    if final:
        g.node(name, f"{name}/{out}", shape="doublecircle")
    else:
        g.node(name, f"{name}/{out}", shape="circle")

def add_edge(g, s, t, inp):
    g.edge(s, t, label=str(inp))

g = Digraph("FSM", filename="fsm.gv", format="png")
g.attr(rankdir="LR")

# Reset arrow (Reset --> S0/0)
g.node("reset", "", shape="point")
g.edge("reset", "S0", label="reset")

# States + outputs (Moore)
for i in range(25):
    add_state(g, f"S{i}", 0)
add_state(g, "S25", 1, final=True)

# Transitions
transitions = {
    "S0":  {0:"S0",  1:"S1"},
    "S1":  {0:"S2",  1:"S1"},
    "S2":  {0:"S3",  1:"S1"},
    "S3":  {0:"S0",  1:"S4"},
    "S4":  {0:"S5",  1:"S1"},
    "S5":  {0:"S6",  1:"S1"},
    "S6":  {0:"S0",  1:"S7"},
    "S7":  {0:"S8",  1:"S1"},
    "S8":  {0:"S9",  1:"S1"},
    "S9":  {0:"S0",  1:"S10"},
    "S10": {0:"S11", 1:"S1"},
    "S11": {0:"S12", 1:"S1"},
    "S12": {0:"S0",  1:"S13"},
    "S13": {0:"S14", 1:"S1"},
    "S14": {0:"S15", 1:"S1"},
    "S15": {0:"S0",  1:"S16"},
    "S16": {0:"S17", 1:"S1"},
    "S17": {0:"S18", 1:"S1"},
    "S18": {0:"S0",  1:"S19"},
    "S19": {0:"S20", 1:"S1"},
    "S20": {0:"S21", 1:"S1"},
    "S21": {0:"S0",  1:"S22"},
    "S22": {0:"S23", 1:"S1"},
    "S23": {0:"S24", 1:"S1"},
    "S24": {0:"S0",  1:"S25"},
    "S25": {0:"S0",  1:"S1"},
}

for s, mp in transitions.items():
    for inp, t in mp.items():
        add_edge(g, s, t, inp)

# Render output: fsm.png
g.render(cleanup=True)
print("Generated: fsm.png")
