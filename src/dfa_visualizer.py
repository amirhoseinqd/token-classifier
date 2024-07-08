import graphviz

def create_dfa_image():
    # Define The DFA Using Graphviz
    dfa = graphviz.Digraph('DFA', filename='./output/dfa', format='png')

    # Adding States
    dfa.attr('node', shape='circle')
    dfa.node('S0')  # Start state
    dfa.node('S1')  # Identifier state
    dfa.node('S2')  # Number state
    dfa.node('S3')  # Symbol state
    dfa.node('S4')  # Keyword state

    # Adding Transitions
    # For Identifiers
    dfa.edge('S0', 'S1', label='a-z')
    dfa.edge('S1', 'S1', label='a-z0-9')

    # For Numbers
    dfa.edge('S0', 'S2', label='0-9')
    dfa.edge('S2', 'S2', label='0-9')
    dfa.edge('S2', 'S3', label='.')

    # For Symbols
    symbols = ['(', ')', ';', '+', '*', '=', '>', '>=', '<', '<=', '!=', '==']
    for symbol in symbols:
        dfa.edge('S0', 'S3', label=symbol)

    # For Keywords
    keywords = ['int', 'char', 'if', 'then', 'else']
    for keyword in keywords:
        dfa.edge('S0', 'S4', label=keyword)

    # Mark Start State
    dfa.attr('node', shape='doublecircle')
    dfa.node('S0')

    # Save The DFA As An Image
    dfa.render()

if __name__ == "__main__":
    create_dfa_image()
