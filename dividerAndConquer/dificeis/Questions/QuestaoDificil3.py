import collections

class Solution(object):
    def recoverArray(self, n, sums):
        """
        :type n: int
        :type sums: List[int]
        :rtype: List[int]
        """
      
        sums.sort()
        
        ans = []
        
       
        for _ in range(n):
          
            d = sums[1] - sums[0]
            
           
            s_next = []
            
     
            counts = collections.Counter(sums)
            
        
            for s in sums:
                if counts[s] > 0:
                
                    if counts[s + d] > 0:
                        s_next.append(s)
                        counts[s] -= 1
                        counts[s + d] -= 1
            
           
            s_next_set = set(s_next)
            
           
            if 0 in s_next_set:
                ans.append(d)
                sums = s_next
            else:
               
                ans.append(-d)
               
                sums = [s + d for s in s_next]
                
        return ans
    

    import collections

import collections

class Solution(object):
    def recoverArray(self, n, sums):
        """
        :type n: int
        :type sums: List[int]
        :rtype: List[int]
        """
        # Ordena a lista inicial de somas.
        sums.sort()
        
        ans = []
        
        # Encontramos um elemento do array desconhecido a cada iteração.
        for _ in range(n):
            # A diferença entre as duas menores somas é um candidato para um elemento
            # ou seu negativo. Vamos chamá-lo de 'd'.
            d = sums[1] - sums[0]
            
            # Vamos particionar o `sums` atual em dois conjuntos potenciais.
            # `s_next` irá guardar uma das metades da partição.
            s_next = []
            
            # Usa um mapa de frequência (Counter) para buscas e decrementos eficientes.
            counts = collections.Counter(sums)
            
            # Constrói uma metade da partição de forma gulosa.
            for s in sums:
                if counts[s] > 0:
                    # Assume que 's' está na primeira metade da partição.
                    # Seu elemento correspondente na outra metade deve ser 's + d'.
                    if counts[s + d] > 0:
                        s_next.append(s)
                        counts[s] -= 1
                        counts[s + d] -= 1
            
            # Agora, decide se o elemento é 'd' ou '-d'.
            # O novo conjunto de somas de subconjuntos PRECISA conter 0 (para o conjunto vazio).
            
            # Cria um set (conjunto) para uma verificação rápida com 'in'.
            s_next_set = set(s_next)
            
            # Se 0 está na metade que acabamos de construir, nossa hipótese estava correta.
            # O elemento é 'd', e `s_next` é o novo array `sums`.
            if 0 in s_next_set:
                ans.append(d)
                sums = s_next
            else:
                # Se 0 não está em `s_next`, ele deve estar na *outra* metade da partição.
                # Isso implica que o elemento era `-d`.
                ans.append(-d)
                # O novo array `sums` correto é a outra metade da partição, que é {s + d para todo s em s_next}.
                sums = [s + d for s in s_next]
                
        return ans