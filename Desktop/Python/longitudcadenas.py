listacadenas=["snake","ocelot","otacon","eva"]
def longitud_cadenas(listacadenas) :
    max=[0]
    for i in listacadenas :
        if len(i) > len(max) :
            max=i
    return max

print("La palabra mas larga es",longitud_cadenas(listacadenas))