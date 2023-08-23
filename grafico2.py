import cheapest_insertion as ci
import matplotlib.pyplot as plt

def grafico2(lista_nodi, lista_fermate, lista_route, nomefile):

    plt.figure(figsize=(30, 30))
    plt.grid()
    plt.xticks(range(0, 1001, 50))
    plt.yticks(range(0, 1001, 50))



    for el in lista_nodi:
        plt.plot(el.get_x(), el.get_y(), color='pink', marker='o')
        plt.annotate(el.get_id(), (el.get_x(), el.get_y()), textcoords="offset points", xytext=(0,10), ha='center')



    for el in lista_route:
        
        lista=el.get_nodi()
        lista_x=[]
        lista_y=[]
        lista_i=[]
        for el2 in lista:
            lista_x.append(el2.get_x())
            lista_y.append(el2.get_y())
            lista_i.append(el2.get_id())
        plt.plot(lista_x, lista_y, color='blue', marker='o', linewidth=0.5)
        for i, label in enumerate(lista_i):
            plt.annotate(label, (lista_x[i], lista_y[i]), textcoords="offset points", xytext=(0,10), ha='center')

    for el in lista_fermate:
        plt.plot(el.get_x(), el.get_y(), color='orange', marker='o')
        plt.annotate(el.get_l(), (el.get_x(), el.get_y()), textcoords="offset points", xytext=(10,0), ha='center')

    plt.plot(321, 765, color='red', marker='o')

    plt.savefig(nomefile)