#Array() ----> constructor
#get_leght ()----> tamaño del arreglo
#get_item(index)---> Elem en pos index
#set_item (index, v)----> cambia valor en la posicion
#clearing(valor)
#Array2D
#Array2D (rows, cols)----> regresa eñ numero de
#clearing(value)
#set_item(rows, cols, value)
#get_item(r,c)
class Array:
         def __init__(self, n):#self = referencia a la propia clase
                  self.__data=[]
                  for i in range(n):
                           self.__data.append(None)
         def get_leght(self):
                  return len(self.__data)

         def set_item(self, index, value):
                  if index >= 0 and index < len(self.__data):
                           self.__data[index]= value 
                  else:
                           print("Fuera de rango")

         def get_item(self, index):
                  if index >= 0 and index < len(self.__data):
                           return self.__data[index] 
                  else:
                           print("Fuera de rango")
                                   
         def clearing(self, valor):
                  for index in range(len(self.__data)):
                           self.__data[index]=valor

         def to_string(self):
                  print(self.__data)

                       

#main
def main():
         arreglo = Array(10)
         arreglo.to_string()
         print(f"El tamaño es de{arreglo.get_leght()}")
         arreglo.set_item(1,10)
         arreglo.to_string()
         arreglo.set_item(12,10)
         print(f"El elemento 1 es {arreglo.get_item(1)}")
         arreglo.get_item(20)
         arreglo.clearing(5)
         arreglo.to_string()

main()
