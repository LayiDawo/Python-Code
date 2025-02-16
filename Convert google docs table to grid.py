import pandas as pd
def get_values(doc_link):
    table = pd.read_html(doc_link)[0]
    rows = table.values.tolist()[1:]
    for data in rows:
        data[1] = data[1].encode('latin1').decode('utf-8')
    return rows

def print_values(rows):
    max_x = max_y = 0
    for data in rows:
        max_x = max(int(data[0]), max_x)
        max_y = max(int(data[2]), max_y)

    grid = [[" " for i in range(max_x+1)] for i in range(max_y+1)]

    for x, char, y in rows:
        grid[int(y)][int(x)] = char

    for line in grid:
        if 1 == len(set(line)):
            continue
        else:
         print("".join(line),"\n")

print_values(get_values("https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"))
