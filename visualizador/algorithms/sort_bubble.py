# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0
j = 0

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 0
    j = 0

def step():
    global items, n, i, j

    if j >= n-1:
        return {"done": True} 

    a = i
    b = i + 1
    swap = False
    
    if items[a] > items[b]:
        items[a], items[b] = items[b], items[a]
        swap = True

    i += 1

    if i>=n-1-j:
        i = 0
        j += 1
    
    return {"a": a, "b": b, "swap": swap, "done": False} 
