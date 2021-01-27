list=[    "sondeo", "geotecnia", "suelo", "ensayos", "laboratorio", "reportes", "nube", "ingenieria", "origen", "deposito", "roca", "agua", "muestreo", "exploracion",
    "online", "Geotechnical", "soil", "test", "water", "sampling", "report", "subsoil", "rock", "engineering","cloud", "probe", "hole", "ground"
]


list=[    "son", "geo","tecnia", "ensa", "lab", "nube", "ing", "ori", "dep", "roca",  "muestreo", "exp",
    "online", "technical", "soil", "test", "samp", "report", "sub",  "cloud", "probe", "hole", "ground", "in", "situ"
]



f = open ('datos.txt','w')


for a in list:
    for b in list:
        if a != b:
            texto='{}{}\n'.format(a,b)
            f.write(texto)


for a in list:
    for b in list:
        for c in list:
            if a == b or b == c or c ==a:
                pass
            else:
                texto='{}{}{}\n'.format(a,b,c)
                f.write(texto)
f.close()
