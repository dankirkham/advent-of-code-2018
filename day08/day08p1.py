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
    metadata_sum = 0

    children_count = next(tokens)
    metadata_count = next(tokens)

    for _ in range(children_count):
        metadata_sum += parse_node(tokens)


    for _ in range(metadata_count):
        metadata_sum += next(tokens)

    return metadata_sum

tokens = read_tokens()

metadata_sum = parse_node(iter(tokens))

print(metadata_sum)
