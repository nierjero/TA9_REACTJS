def mult(a):
    def mult2(b):
        return a *b
    return mult2

print(

    mult(5)(3)
)