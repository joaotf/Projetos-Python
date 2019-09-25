import os
import networkx as nx
from networkx import Graph
import matplotlib.pyplot as plt
import random
import numpy as np 
import pylab
from tkinter import filedialog as tkFileDialog
 
#DEPENDÊNCIAS PARA FUNCIONAR CORRETAMENTE
#pip install networkx==2.1
#python -mpip install -U pip
#python -mpip install -U matplotlib
cores = ['blue','red','yellow','green']
menu = 1;
lista_vertices = [];
lista_conexoes = [];
vertices = {};
vertices2 = {};
arestas = {}
vertice_conexao = {};
vertice_conexao2 = {};
weight = 0;


#CRIAÇÃO DO GRAFO
G = nx.Graph();
Y = nx.Graph();
pos = nx.spring_layout(G)
pos2 = nx.spring_layout(Y)

#red_edges = [('C','D'),('D','A')]
#edge_colors = ['black' if not edge in red_edges else 'red' for edge in G.edges()]

while(menu != 0):
    menu = int(input("Menu \n 1)Cadastrar vértice \n 2)Cadastrar ligação \n 3)Mostrar conexões \n 4)Mostrar vértices \n 5)Desenhar grafo \n 6)Verificar Grafo Euleriano \n 7)Mostrar percurso Euleriano \n 8)Remover Vértice \n 9)Grafo salva em Arquivo.txt\n 10)Arquivo.txt transforma em Grafo\n 11)Busca Cega - Algoritmo A*\n 12)Imagem\n 0)Sair \n Opção :"));
    if(menu == 1):
        os.system('cls');
        cadastrar_vertice = input("Digite o nome da vértice : ");
        vertices2 = {cadastrar_vertice:""};
        vertices.update(vertices2);
        lista_vertices.append(vertices);
        G.add_node(cadastrar_vertice);
    if(menu == 2):
        os.system("cls");
        if(len(vertices)>= 2):
            teste = vertices.keys();
            print("Vértices cadastradas : ",teste,"\n")
            conexao = input("Digite o nome da vértice de origem :\n");
            conexao2 = input("Digite o nome da vértice de destino :\n");
            valor = float(input("Digite o valor da conexão : \n"))
            if (conexao in teste) == True and (conexao2 in teste) == True:
                vertice_conexao2 = {conexao:conexao2};
                vertice_conexao.update(vertice_conexao2);
                lista_conexoes.append(vertice_conexao);
                G.add_edge(conexao,conexao2,weight=valor);
                arestas.update({conexao:conexao2}) 
                print("Conexão feita com sucesso!\n")
            elif((conexao in teste) == True) and ((conexao2 in teste) == False):
                os.system("cls");
                print("Você digitou incorretamente a Vértice de Destino ou ainda não a cadastrou.\n");
            elif((conexao in teste) == False) and ((conexao2 in teste) == True):
                os.system('cls');
                print("Você digitou incorretamente a Vértice de Origem ou ainda não a cadastrou.\n");
            elif((conexao in teste) == False) and ((conexao2 in teste) == False):
                os.system("cls");
                print("Você digitou incorretamente a Vértice de Destino e a Vértice de Origem ou ainda não as cadastrou.\n");
        elif(len(vertices) <= 0):    
            print("\n\nVocê ainda não cadastrou nenhuma vértice !")
        elif(len(vertices) == 1):
            print("\n\nVocê só cadastrou apenas uma(1) vértice !")
    if(menu == 3):
        os.system("cls")
        if(len(lista_conexoes) >= 1):
            for y in range(1):
                print("Conexões cadastradas :",lista_conexoes[y]);
        else:
            print("Nenhuma conexão foi cadastrada até o momento. \n")
    if(menu == 4):
        os.system("cls");
        for x in range(1):
            print("Vértices cadastradas :",vertices.keys());
    if(menu == 5):
        os.system("cls")
        plt.title("Inteligência Artificial - 1")
        plt.axis('off')
        pos = nx.circular_layout(G)
        edge_labels = {(u,v): d['weight'] for u,v,d in G.edges(data=True)}
        #nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
        #nx.draw(G,pos,node_size=1500,edge_color=edge_colors,edge_weight=True,with_labels=True)
        #nx.draw(G,with_labels = True,edge_weight = True)
        #plt.draw();
        #plt.show()
        #plt.figure()
        nx.draw_networkx_nodes(G,pos,node_size=700)
        nx.draw_networkx_edges(G,pos)
        nx.draw_networkx_labels(G,pos)
        nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
        plt.show();
        pylab.show();
    if(menu == 6):
        if(len(vertices) != 0):
            os.system("cls")
            print("Verificação : ",nx.is_eulerian(G))
        if(len(vertices) == 0):
            os.system("cls")
            print("O grafo ainda não foi preenchido \n")
    if(menu == 7):
        os.system("cls")
        if(len(vertices) == 0 or len(vertice_conexao) == 0):
            os.system("cls");
            print("O grafo não está preenchido ou não tem ligações suficientes! \n")
            continue;
        if((nx.is_eulerian(G) == True)):
            os.system("cls");
            print("Vértices cadastradas :",vertices.keys());
            perg = input("Digite a vértice inicial : ");
            caminho = list(nx.eulerian_circuit(G, source=perg));
            print("Caminho Euleriano : \n",caminho);
        elif(nx.is_eulerian(G) == False):
            os.system("cls");
            print("O grafo não é euleriano");
    if(menu == 8):
        if(len(vertices) != 0):
            print("Vértices Cadastradas : ",vertices.keys());
            perg = input("Digite a vértice para remover : ");
            G.remove_node(perg);
            print("Vértice "+perg+" removido com sucesso\n");
        elif(len(vertices) >= 0):
            os.system("cls");
            print("Você ainda não cadastrou nenhuma vértice \n")

    if(menu == 9):
        if(len(lista_conexoes) == 0):
            os.system("cls")
            print("Nenhuma conexão foi cadastrada até o momento. \n")
        elif(len(lista_conexoes) >= 1):
            f = tkFileDialog.askopenfile(mode="wb")
            nx.write_weighted_edgelist(G,f)
            os.system("cls")
            print("Arquivo gravado com sucesso")
            f.close();
            
 
    if(menu == 10):
        f = tkFileDialog.askopenfile(mode="rb");
        os.system("cls") 
        plt.title("Inteligência Artificial - 1")
        plt.axis('off')
 
        nx.read_weighted_edgelist(f,create_using=Y,nodetype=str,encoding="utf-8")
        pos = nx.spring_layout(Y)
        
        edge_labels = {(u,v): d['weight'] for u,v,d in Y.edges(data=True)}
        nx.draw_networkx_nodes(Y,pos,node_size=700)
        nx.draw_networkx_edges(Y,pos)
        nx.draw_networkx_labels(Y,pos)
        nx.draw_networkx_edge_labels(Y,pos,edge_labels=edge_labels)
        plt.show();
        pylab.show();
        
    if(menu == 11):
        os.system("cls")
        print("Algoritmo A*\n")
        inicial = input("Digite o começo :")
        target = input("Digite o final :")

        print("Resultado : ",list(nx.astar_path(Y,inicial,target,heuristic=None)),"\n")
    if(menu == 12):
        nx.draw_networkx_nodes(G,pos,node_size=700)
        nx.draw_networkx_edges(G,pos)
        nx.draw_networkx_labels(G,pos)
        nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)       
        perg = input("Imagem : ")
        plt.savefig(f"{perg}.png")
            
    if menu < 0 or menu >= 12 :
        os.system("cls")
        print("Valor inválido\n ")