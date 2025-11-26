# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0      #cantidad de elemetnos en la lista
i = 0      # elemento que queremos insertar
j = None   # cursor de desplazamiento hacia la izquierda (None = empezar)
temp = None

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 0      
    j = None

def step():
    global items, n, i, j 
    if i >= n:
        return {"done": True}

    if j is None:
        j = i 
        return {"highlight": True}

    a = j
    b = j-1
    swap = False

    if j > 0 and items[b] > items[a]:
        items[b], items[a] = items[a], items[b]
        swap = True
        j -= 1
        return {"a": a, "b": b, "swap": swap,  "done": False}
    else:
        i += 1
        j = None
        return {"a": a, "b": b, "swap": swap,  "done": False}

    
    #if j > 0:
     #   j = j-1
    #    return {"a": a, "b": b, "swap": swap,  "done": False}
    #i += 1
    #j = None
    #return {"a": a, "b": b, "swap": swap,  "done": False}
    
    #NO FUNCIONA

    # - Si i >= n: devolver {"done": True}.
    # - Si j es None: empezar desplazamiento para el items[i] (p.ej., j = i) y devolver un highlight sin swap.
    # - Mientras j > 0 y items[j-1] > items[j]: hacer UN swap adyacente (j-1, j) y devolverlo con swap=True.
    # - Si ya no hay que desplazar: avanzar i y setear j=None.
    
