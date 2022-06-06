# http://lwh.free.fr/pages/algo/tri/tri_insertion_es.html
# https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheInsertionSort.html
# https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-6.php

def Insertion(Vector):

    for i in range(1,len(Vector)):

        actual = Vector[i]
        posicion = i

        #Desplazamiento de los elementos del vector
        while posicion > 0 and Vector[posicion-1] > actual:#mientras los datos del vector sean mayores al actual 

            #movimiento de los datos        
            Vector[posicion] = Vector[posicion-1]

            #cambio de posicion
            posicion = posicion - 1

        #insertar el elemento en su lugar
        Vector[posicion] = actual


########################################

vector = [54,26,93,17,77,31,44,55,20]

Insertion(vector)

#mostrar el vector
print ("VECTOR ORDENADO:") 
print(vector)