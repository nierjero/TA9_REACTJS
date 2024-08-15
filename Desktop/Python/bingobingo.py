númerosbingo=[[1,2,3,4],[7,8,5,5,13],[9,7,6],[1,2,3,4]] 
números_sorteados=[1,2,3,4,8,6,43,7,13,87,13,9,6,5] 
def tiene_bingo(númerosbingo,números_sorteados) : 
    bingo=True 
    for fila in númerosbingo:  
         for número in fila : 
              if número not in números_sorteados : 
                  bingo= False 
    return bingo 
    

print(tiene_bingo(númerosbingo, números_sorteados)) 