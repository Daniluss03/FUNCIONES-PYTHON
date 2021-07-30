def monitorizar_args( funcion):

    def decorar(*args,**kwargs):
        print("\t esta apunto de ejecutar la funcion",funcion.__name__)
      
        funcion(*args,**kwargs)
       
        print("\t Se ha finalizado la  ejecucion de  la funcion",funcion.__name__)

    return decorar 


@monitorizar_args
def hola(nombre):
    print ("Hola {}!".format(nombre))
@monitorizar_args
def adios(nombre):
    print("adios {}!".format(nombre))
@monitorizar_args
def saludar(nombre):
     print("buenos dias {}!".format(nombre))   

print(hola("hector"))
