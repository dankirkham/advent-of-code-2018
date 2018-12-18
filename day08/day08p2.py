import re

def read_tokens():
    tokens = []

    f = open('input8.in', 'r')

    for line in f:
        m = re.search('(\d+)', line)

        while m:
            tokens.append(int(m.group(1)))

            line = line[m.span(1)[1]:]

            m = re.search('(\d+)', line)

    f.close()

    return tokens

def parse_node(tokens):
    node_value = 0

    children_count = next(tokens)
    metadata_count = next(tokens)

    children_values = []
    for _ in range(children_count):
        children_values.append(parse_node(tokens))

    if children_count == 0:
        for _ in range(metadata_count):
            node_value += next(tokens)
    else:
        for _ in range(metadata_count):
            metadata_entry = next(tokens) - 1
            if metadata_entry >= 0 and metadata_entry < len(children_values):
                node_value += children_values[metadata_entry]

    return node_value

tokens = read_tokens()

metadata_sum = parse_node(iter(tokens))

print(metadata_sum)
