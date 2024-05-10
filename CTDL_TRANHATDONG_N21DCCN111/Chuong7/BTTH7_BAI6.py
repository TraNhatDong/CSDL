def SoCungVao(dt, v):
    if v not in dt:
        return None
    so_cung_vao = sum(v in edges for edges in dt.values())
    return so_cung_vao
dt = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': ['A'],
    'D': ['C']
}
v = 'C'
print(SoCungVao(dt, v))
