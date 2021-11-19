class Produto():

    def __init__(self):
        self.titulo = None
        self.valor = None
        self.desconto = None
       

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_valor(self):
        return self.valor

    def set_valor(self, valor):
        self.valor = valor

    def get_desconto(self):
        return self.desconto

    def set_desconto(self, desconto):
        self.desconto = desconto

    def descreveProduto(self):
        print('LIVROS ROMANTICOS COM DESCONTOS')
        print('CDs DE ROCKS COM DESCONTOS')
        print('DVDs DE FILMES COM DESCONTOS')
        print ('\n')
      

    def descricao_produto(self):

      lista = []
   
      lista.append(self.get_titulo())
      lista.append(self.get_valor())
      return lista



class Livro(Produto):
    def __init__(self):
        super().__init__()
        self.autor = None

    def get_autor(self):
        return self.autor

    def set_autor(self, autor):
        self.autor = autor

    def descreve_livro(self):
        print('Autor: ', self.get_autor())  

    def preco_com_desconto(self, desconto):
        desconto = 0
        desconto = self.get_desconto()*10/100
        return self.get_desconto()- desconto



class CD(Produto):

    def __init__(self):
        super().__init__()
        self.artista = None

    def get_artista(self):
        return self.artista

    def set_artista(self, artista):
        self.artista = artista
   
    def descreve_cd(self):
       print('Artista: ', self.get_artista())

    def preco_com_desconto(self, desconto):
        desconto = 0
        desconto = self.get_desconto()*15/100
        return self.get_desconto()- desconto


class DVD(Produto):

    def __init__(self):
        super().__init__()
        self.duracao = None

    def get_duracao(self):
        return self.duracao

    def set_duracao(self, duracao):
        self.duracao = duracao
   
    def descreve_dvd(self):
       print('Duração: ', self.get_duracao())

    def preco_com_desconto(self, desconto):
        desconto = 0
        desconto = self.get_desconto()*20/100
        return self.get_desconto()- desconto


#EXECUCAO DE DISCRIÇÃO

descricao = Produto ()
descricao.descreveProduto()


#EXECUCAO 1
produto1 = Produto()
produto1.set_titulo('o melhor de mim')
produto1.set_valor(45)


produto2 = Produto()
produto2.set_titulo('Cidade de Papel')
produto2.set_valor(35)


produto3 = Produto()
produto3.set_titulo('A culpa é das estrelas')
produto3.set_valor(37)


livro1 = []
livro2 = []
livro3 = []
livro1.append(produto1.descricao_produto())
livro2.append(produto2.descricao_produto())
livro3.append(produto3.descricao_produto())


for livro1 in livro1:
  livro = livro1
  #print(livro1)
  #// pensei em printar as listas com os produtos também, mas achei melhor apenas guardar elas em uma varial e mostrar os produtos individualmente // por isso os prints estão comentados.
 

for livro2 in livro2:
  livro = livro2
 

for livro3 in livro3:
  livro = livro3
  #print(livro3)
 
#print('\n')



produto_cd1 = Produto()
produto_cd1.set_titulo('Wonderwall')
produto_cd1.set_valor(15)

produto_cd2 = Produto()
produto_cd2.set_titulo('Rock in Roll')
produto_cd2.set_valor(25)

produto_cd3 = Produto()
produto_cd3.set_titulo('Anos 80 a 90')
produto_cd3.set_valor(100)

cd1 = []
cd2 = []
cd3 = []
cd1.append(produto_cd1.descricao_produto())
cd2.append(produto_cd2.descricao_produto())
cd3.append(produto_cd3.descricao_produto())
for cd1 in cd1:
  cd = cd1
  #print(cd1)


for cd2 in cd2:
  cd = cd2
  #print(cd2)


for cd3 in cd3:
  cd = cd3
  #print(cd3)
  #print('\n')


produto_dvd1 = Produto()
produto_dvd1.set_titulo('Liga da Justica de Zack Snyder')
produto_dvd1.set_valor(55)

produto_dvd2 = Produto()
produto_dvd2.set_titulo('Jogador N01')
produto_dvd2.set_valor(150)

produto_dvd3 = Produto()
produto_dvd3.set_titulo('Interstalar')
produto_dvd3.set_valor(100)

dvd1 = []
dvd2 = []
dvd3 = []
dvd1.append(produto_dvd1.descricao_produto())
dvd2.append(produto_dvd2.descricao_produto())
dvd3.append(produto_dvd3.descricao_produto())
for dvd1 in dvd1:
  dvd = dvd1
  #print(dvd1)

for dvd2 in dvd2:
  dvd = dvd2
  #print(dvd2)


for dvd3 in dvd3:
  dvd = dvd3
  #print(dvd3)
#print('\n')

#EXECUÇAO2

livro0 = Livro()
livro0.set_autor('Nichollas Sparkes')
livro0.set_desconto(livro1[1])
print('Livro')
livro0.descreve_livro()
print(livro1[0])
print('Valor: R$',livro0.preco_com_desconto(0))
print('\n')

livro00 = Livro()
livro00.set_autor('John Green')
livro00.set_desconto(livro2[1])
print('Livro')
livro00.descreve_livro()
print(livro2[0])
print('Valor: R$',livro00.preco_com_desconto(0))
print('\n')

livro000 = Livro()
livro000.set_autor('John Green')
livro000.set_desconto(livro3[1])
print('Livro')
livro000.descreve_livro()
print(livro3[0])
print('Valor: R$',livro000.preco_com_desconto(0))
print('\n')

#execução3
cd0 = CD()
cd0.set_artista('Oasis')
cd0.set_desconto(cd1[1])
print('CD')
cd0.descreve_cd()
print(cd1[0])
print('Valor: R$',cd0.preco_com_desconto(0))
print('\n')

cd00 = CD()
cd00.set_artista('KISS')
cd00.set_desconto(cd2[1])
print('CD')
cd00.descreve_cd()
print(cd2[0])
print('Valor: R$',cd00.preco_com_desconto(0))
print('\n')

cd000 = CD()
cd000.set_artista('Helton John')
cd000.set_desconto(cd3[1])
print('CD')
cd000.descreve_cd()
print(cd3[0])
print('Valor: R$',cd000.preco_com_desconto(0))
print('\n')

#EXECUÇÂO4
dvd0 = DVD()
dvd0.set_duracao(' 3:45:23')
dvd0.set_desconto(dvd1[1])
print('DVD')
dvd0.descreve_dvd()
print(dvd1[0])
print('Valor: R$',dvd0.preco_com_desconto(0))
print('\n')

dvd00 = DVD()
dvd00.set_duracao(' 1:56:12')
dvd00.set_desconto(dvd2[1])
print('DVD')
dvd00.descreve_dvd()
print(dvd2[0])
print('Valor: R$',dvd00.preco_com_desconto(0))
print('\n')

dvd000 = DVD()
dvd000.set_duracao(' 2:45:00')
dvd000.set_desconto(dvd3[1])
print('DVD')
dvd000.descreve_dvd()
print(dvd3[0])
print('Valor: R$',dvd000.preco_com_desconto(0))
print('\n')

#EXECUÇÃO DAS SOMAS DOS PRODUTOS
#1 SOMA DOS LIVROS
soma1 = livro0.preco_com_desconto(0) + livro00.preco_com_desconto(0) + livro000.preco_com_desconto(0)
print('Valor total do Box Livros R$',soma1)

#2 SOMA DOS CD'S
soma2 = cd0.preco_com_desconto(0) + cd00.preco_com_desconto(0) + cd000.preco_com_desconto(0)
print('Valor total do Box CD R$',soma2)

#3 SOMA DOS DVD'S
soma3 = dvd0.preco_com_desconto(0) + dvd00.preco_com_desconto(0) + dvd000.preco_com_desconto(0)
print('Valor total do Box DVD R$',soma3)

#4 Soma total dos produtos
total = soma1 + soma2 + soma3
print('Valor total dos produtos R$',total)

import sys
sys.exit()