def ChuaDinh(dt, v):
    return v in dt
dt = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
v = 'A'
print(ChuaDinh(dt, v))

v = 'E'
print(ChuaDinh(dt, v))
