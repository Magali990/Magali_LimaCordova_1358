#Array 2d (rows,cols)
#t_num_rows() regresa el numero de filas
#get_num_cols() " " " " COLUMNAS
#clearing (value)
#set_item(r,c,valor)
#get_item(r,c)

class Array2D:
         def __init__(self,rows,cols):
                  self.__data=[]
                  self.__row=rows
                  self.__col=cols
                  for row in range(rows):
                           tmp=[]
                           for col in range(cols):
                                    tmp.append(None)
                           self.__data.append(tmp)

         def to_string(self):
                  print(self.__data)

         def get_num_rows(self):
                  return self.__row

         def get_num_cols(self):
                  return self.__col

         def clearing(self, value):
                  for row in range(self.__row):
                           for col in range(self.__col):
                                    self.__data[row][col]=value

         def set_item(self,r,c,valor):
                  if (r>=0 and r<=self.__row) and (c>=0 and c<=self.__col):
                           self.__data[r][c]=valor

def main ():
         arreglo=Array2D(5,5)
         arreglo.to_string()
         print(f"numero de renglones {arreglo.get_num_rows()}")
         print(f"numero de columnas {arreglo.get_num_cols()}")
         arreglo.clearing(1)
         arreglo.to_string()
         

main()
