d = {"mandya":20,"bangalore":30,"Mysore":40}

dc={c:v*2 for c,v in d.items()}
print(dc)

dc={c:v for c,v in d.items() if v<30 or v>30}
print(dc)