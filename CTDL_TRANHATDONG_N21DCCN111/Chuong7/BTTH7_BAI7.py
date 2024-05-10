def SoCungRa(dt, v):
    if v not in dt:
        return None
    return len(dt[v])
dt = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': ['A'],
    'D': ['C']
}
v = 'A'
print(SoCungRa(dt, v))
