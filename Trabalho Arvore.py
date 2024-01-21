class Node: 
  def __init__(self, palavra):
      self.palavra = palavra
      self.esquerda = None
      self.direita = None
      self.proximo = None

class ArvoreEListas:
  def __init__(self):
      self.raiz = None
      self.lista_curta = None
      self.lista_longa = None

  def insere_palavra(self, palavra):

      if self.busca_palavra(palavra):
        # Verifica se a palavra já existe
        print(f'palavra ja existente: {palavra}')
      else:
        # Implementa a inserção na árvore
        self.raiz = self._insere(self.raiz, palavra)

        # Adiciona à lista correspondente se a palavra não existir ainda
        if len(palavra) <= 5:
            if not self.busca_na_lista(self.lista_curta, palavra):
                self.lista_curta = self.insere_na_lista(self.lista_curta, palavra)
        else:
            if not self.busca_na_lista(self.lista_longa, palavra):
                self.lista_longa = self.insere_na_lista(self.lista_longa, palavra)

        print(f'palavra inserida: {palavra}')

  def _insere(self, raiz, palavra):
      # Implementa a inserção na árvore (método recursivo)
      if raiz is None:
          return Node(palavra)
      if palavra < raiz.palavra:
          raiz.esquerda = self._insere(raiz.esquerda, palavra)
      elif palavra > raiz.palavra:
          raiz.direita = self._insere(raiz.direita, palavra)
      return raiz

  def insere_na_lista(self, cabeca, palavra):
      # Implementa a inserção na lista
      novo_no = Node(palavra)
      if cabeca is None or palavra < cabeca.palavra:
          novo_no.proximo = cabeca
          return novo_no
      atual = cabeca
      while atual.proximo is not None and palavra > atual.proximo.palavra:
          atual = atual.proximo
      novo_no.proximo = atual.proximo
      atual.proximo = novo_no
      return cabeca

  def busca_palavra(self, palavra):
      # Implementa a busca na árvore
      resultado = self._busca(self.raiz, palavra)
      if resultado:
          return True 
          
      else:
          return False
      

  def _busca(self, raiz, palavra):
      # Implementa a busca na árvore (método recursivo)
      if raiz is None or raiz.palavra == palavra:
          return raiz
      if palavra < raiz.palavra:
          return self._busca(raiz.esquerda, palavra)
      return self._busca(raiz.direita, palavra)

  def busca_na_lista(self, cabeca, palavra):
      # Verifica se a palavra já existe na lista
      atual = cabeca
      while atual:
          if atual.palavra == palavra:
              return True
          atual = atual.proximo
      return False


  def lista_palavras_na_lista(self, tamanho):
      # Implementa a listagem das palavras de uma das listas
      lista_atual = self.lista_curta if tamanho == 1 else self.lista_longa
      self._imprime_lista(lista_atual)

  def _imprime_lista(self, cabeca):
      # Implementa a impressão de uma lista
      atual = cabeca
      while atual:
          print(atual.palavra)
          atual = atual.proximo
      if not cabeca:
          print('lista vazia')


  def lista_palavras_por_tamanho(self, numero):
    # Implementa a listagem das palavras com o número de letras indicado
    lista_atual = self.lista_curta if numero <= 5 else self.lista_longa
    palavras = []

    atual = lista_atual
    while atual:
        if len(atual.palavra) == numero:
            palavras.append(atual.palavra)
        atual = atual.proximo

    palavras.sort()  # Ordena as palavras em ordem alfabética

    for palavra in palavras:
        print(palavra)

    if not palavras:
        print('lista vazia')


  def lista_palavras_em_ordem_alfabetica(self, inicio, fim):
      # Implementa a listagem das palavras em ordem alfabética entre duas letras
      self._imprime_intervalo(self.raiz, inicio, fim)

  def _imprime_intervalo(self, raiz, inicio, fim):
      # Implementa a impressão das palavras em ordem alfabética entre duas letras (método recursivo)
      words_in_range = []
      self._coletar_palavras_no_intervalo(raiz, inicio, fim, words_in_range)

      for word in words_in_range:
        print(word)

      if not words_in_range:
        print('lista vazia')

  def _coletar_palavras_no_intervalo(self, raiz, inicio, fim, resultado):
       # Coleta as palavras na árvore que estão no intervalo especificado.
      if raiz:
        if inicio <= raiz.palavra[0] <= fim:
          self._coletar_palavras_no_intervalo(raiz.esquerda, inicio, fim, resultado)
          resultado.append(raiz.palavra)
          self._coletar_palavras_no_intervalo(raiz.direita, inicio, fim, resultado)
        elif inicio < raiz.palavra[0]:
          self._coletar_palavras_no_intervalo(raiz.esquerda, inicio, fim, resultado)
        else:
          self._coletar_palavras_no_intervalo(raiz.direita, inicio, fim, resultado)

  def remove_palavra(self, palavra):
      # Implementa a remoção da palavra da árvore
      self.raiz, removida = self._remove(self.raiz, palavra)

      if removida:
          print(f'palavra removida: {palavra}')
          self.remover_da_lista(self.lista_curta, palavra)
          self.remover_da_lista(self.lista_longa, palavra)
      else:
          print(f'palavra inexistente: {palavra}')


  def remover_da_lista(self, cabeca, palavra):
    # Remove a palavra da lista
    if cabeca:
        if cabeca.palavra == palavra:
            if len(palavra) <= 5:
                self.lista_curta = self.lista_curta.proximo
            else:
                self.lista_longa = self.lista_longa.proximo
            cabeca = cabeca.proximo
        else:
            atual = cabeca
            while atual.proximo:
                if atual.proximo.palavra == palavra:
                    atual.proximo = atual.proximo.proximo
                    return
                atual = atual.proximo


  def _remove(self, raiz, palavra):
      # Implementa a remoção da palavra da árvore (método recursivo)
      if raiz is None:
          return raiz, False

      if palavra < raiz.palavra:
          raiz.esquerda, removida = self._remove(raiz.esquerda, palavra)
      elif palavra > raiz.palavra:
          raiz.direita, removida = self._remove(raiz.direita, palavra)
      else:
          # Caso 1: Nó sem filhos ou apenas um filho
          if raiz.esquerda is None:
              return raiz.direita, True
          elif raiz.direita is None:
              return raiz.esquerda, True

          # Caso 2: Nó com dois filhos - Encontrar o sucessor in-order (menor nó na subárvore direita)
          raiz.palavra = self._min_valor_no(raiz.direita).palavra
          raiz.direita, removida = self._remove(raiz.direita, raiz.palavra)

      return raiz, removida

  def _min_valor_no(self, no):
      # Encontra o nó com o menor valor na árvore (método auxiliar para a remoção)
      atual = no
      while atual.esquerda is not None:
          atual = atual.esquerda
      return atual

  def imprime_arvore(self):
      # Implementa a impressão da árvore
      self._imprime_arvore(self.raiz)

  def _imprime_arvore(self, raiz):
      # Implementa a impressão da árvore (percurso em pré-ordem)
      if raiz:
          print(f'palavra: {raiz.palavra}', end=' ')
          if raiz.esquerda:
              print(f'fesq: {raiz.esquerda.palavra}', end=' ')
          else:
              print('fesq: nil', end=' ')
          if raiz.direita:
              print(f'fdir: {raiz.direita.palavra}')
          else:
              print('fdir: nil')
          self._imprime_arvore(raiz.esquerda)
          self._imprime_arvore(raiz.direita)
      if self.raiz == None:
          print('arvore vazia')


# Função principal
def main():
  arvore_e_listas = ArvoreEListas()



  while True:
      comando = input().strip()

      if comando == 'e':
          break

      if comando == 'i':
          palavra = input().strip()
          arvore_e_listas.insere_palavra(palavra)
      elif comando == 'c':
          palavra = input().strip()
          arvore_e_listas.busca_palavra(palavra)
          consulta = arvore_e_listas.busca_palavra(palavra)
          if consulta:
            print(f'palavra já existente: {palavra}')
          else:
            print(f'palavra inexistente: {palavra}')
      elif comando == 'l':
          tamanho = int(input().strip())
          arvore_e_listas.lista_palavras_na_lista(tamanho)
      elif comando == 'x':
          numero = int(input())
          arvore_e_listas.lista_palavras_por_tamanho(numero)
      elif comando == 'o':
          inicio = input().strip()
          fim = input().strip()
          arvore_e_listas.lista_palavras_em_ordem_alfabetica(inicio, fim)
      elif comando == 'r':
          palavra = input().strip()
          arvore_e_listas.remove_palavra(palavra)
      elif comando == 'p':
          arvore_e_listas.imprime_arvore()

if __name__ == "__main__":
  main()


# Espero que pelos Deuses Astecas Antigos que funcione!!! 