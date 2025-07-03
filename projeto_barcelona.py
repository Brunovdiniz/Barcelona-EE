import networkx as nx
import matplotlib.pyplot as plt
import math # Mantido para futuras extensões, se necessário.

# 1. Dados dos Jogadores:

jogadores_data = [
    {"nome": "Diego Kochen", "idade": 19, "altura": 1.88, "nacionalidade": "EUA", "posicao": "Goleiro", "nota_performance": 5.5, "e_capitao": False},
    {"nome": "Áron Yaakobishvili", "idade": 19, "altura": 1.85, "nacionalidade": "Hungria", "posicao": "Goleiro", "nota_performance": 5.5, "e_capitao": False},
    {"nome": "Joan García", "idade": 24, "altura": 1.91, "nacionalidade": "Espanha", "posicao": "Goleiro", "nota_performance": 6.0, "e_capitao": False},
    {"nome": "Iñaki Peña", "idade": 26, "altura": 1.83, "nacionalidade": "Espanha", "posicao": "Goleiro", "nota_performance": 6.5, "e_capitao": False},
    {"nome": "Marc-André ter Stegen", "idade": 33, "altura": 1.88, "nacionalidade": "Alemanha", "posicao": "Goleiro", "nota_performance": 9.0, "e_capitao": False},
    {"nome": "Wojciech Szczesny", "idade": 35, "altura": 1.96, "nacionalidade": "Polônia", "posicao": "Goleiro", "nota_performance": 8.0, "e_capitao": False},
    {"nome": "Toni Fernández", "idade": 16, "altura": 1.75, "nacionalidade": "Espanha", "posicao": "Atacante", "nota_performance": 5.0, "e_capitao": False},
    {"nome": "Guille Fernández", "idade": 17, "altura": 1.7, "nacionalidade": "Espanha", "posicao": "Meio-campista", "nota_performance": 5.5, "e_capitao": False},
    {"nome": "Lamine Yamal", "idade": 17, "altura": 1.8, "nacionalidade": "Espanha", "posicao": "Atacante", "nota_performance": 7.5, "e_capitao": False},
    {"nome": "Hector Fort", "idade": 18, "altura": 1.85, "nacionalidade": "Espanha", "posicao": "Defensor", "nota_performance": 5.5, "e_capitao": False},
    {"nome": "Pau Cubarsí", "idade": 18, "altura": 1.83, "nacionalidade": "Espanha", "posicao": "Defensor", "nota_performance": 6.5, "e_capitao": False},
    {"nome": "Andrés Cuenca", "idade": 18, "altura": 1.8, "nacionalidade": "Espanha", "posicao": "Defensor", "nota_performance": 5.0, "e_capitao": False},
    {"nome": "Landry Farré", "idade": 18, "altura": 1.78, "nacionalidade": "Espanha", "posicao": "Defensor", "nota_performance": 5.0, "e_capitao": False},
    {"nome": "Marc Bernal", "idade": 18, "altura": 1.91, "nacionalidade": "Espanha", "posicao": "Meio-campista", "nota_performance": 5.5, "e_capitao": False},
    {"nome": "Alexis Olmedo", "idade": 19, "altura": 1.87, "nacionalidade": "Espanha", "posicao": "Defensor", "nota_performance": 5.0, "e_capitao": False},
    {"nome": "Daniel Rodríguez", "idade": 19, "altura": 1.75, "nacionalidade": "Espanha", "posicao": "Atacante", "nota_performance": 5.0, "e_capitao": False},
    {"nome": "Álvaro Cortés", "idade": 20, "altura": 1.88, "nacionalidade": "Espanha", "posicao": "Defensor", "nota_performance": 5.0, "e_capitao": False},
    {"nome": "Sergi Domínguez", "idade": 20, "altura": 1.88, "nacionalidade": "Espanha", "posicao": "Defensor", "nota_performance": 5.0, "e_capitao": False},
    {"nome": "Gavi", "idade": 20, "altura": 1.73, "nacionalidade": "Espanha", "posicao": "Meio-campista", "nota_performance": 8.0, "e_capitao": False},
    {"nome": "Alejandro Balde", "idade": 21, "altura": 1.75, "nacionalidade": "Espanha", "posicao": "Defensor", "nota_performance": 7.5, "e_capitao": False},
    {"nome": "Marc Casadó", "idade": 21, "altura": 1.73, "nacionalidade": "Espanha", "posicao": "Meio-campista", "nota_performance": 6.0, "e_capitao": False},
    {"nome": "Pablo Torre", "idade": 22, "altura": 1.73, "nacionalidade": "Espanha", "posicao": "Meio-campista", "nota_performance": 6.0, "e_capitao": False},
    {"nome": "Pedri", "idade": 22, "altura": 1.75, "nacionalidade": "Espanha", "posicao": "Meio-campista", "nota_performance": 8.0, "e_capitao": False},
    {"nome": "Fermín López", "idade": 22, "altura": 1.75, "nacionalidade": "Espanha", "posicao": "Meio-campista", "nota_performance": 7.0, "e_capitao": False},
    {"nome": "Gerard Martin", "idade": 23, "altura": 1.85, "nacionalidade": "Espanha", "posicao": "Defensor", "nota_performance": 6.0, "e_capitao": False},
    {"nome": "Pau Víctor", "idade": 23, "altura": 1.83, "nacionalidade": "Espanha", "posicao": "Defensor", "nota_performance": 6.0, "e_capitao": False},
    {"nome": "Eric Garcia", "idade": 24, "altura": 1.83, "nacionalidade": "Espanha", "posicao": "Defensor", "nota_performance": 6.5, "e_capitao": False},
    {"nome": "Ferran Torres", "idade": 25, "altura": 1.83, "nacionalidade": "Espanha", "posicao": "Atacante", "nota_performance": 7.0, "e_capitao": False},
    {"nome": "Jules Koundé", "idade": 26, "altura": 1.8, "nacionalidade": "França", "posicao": "Defensor", "nota_performance": 8.0, "e_capitao": False},
    {"nome": "Ronald Araújo", "idade": 26, "altura": 1.88, "nacionalidade": "Uruguai", "posicao": "Defensor", "nota_performance": 8.5, "e_capitao": False},
    {"nome": "Dani Olmo", "idade": 27, "altura": 1.78, "nacionalidade": "Espanha", "posicao": "Meio-campista", "nota_performance": 7.5, "e_capitao": False},
    {"nome": "Frenkie de Jong", "idade": 28, "altura": 1.8, "nacionalidade": "Holanda", "posicao": "Meio-campista", "nota_performance": 8.5, "e_capitao": False},
    {"nome": "Raphinha", "idade": 28, "altura": 1.75, "nacionalidade": "Brasil", "posicao": "Atacante", "nota_performance": 7.5, "e_capitao": False},
    {"nome": "Andreas Christensen", "idade": 29, "altura": 1.88, "nacionalidade": "Dinamarca", "posicao": "Defensor", "nota_performance": 7.5, "e_capitao": False},
    {"nome": "Oriol Romeu", "idade": 33, "altura": 1.83, "nacionalidade": "Espanha", "posicao": "Meio-campista", "nota_performance": 6.0, "e_capitao": False},
    {"nome": "Iñigo Martínez", "idade": 34, "altura": 1.83, "nacionalidade": "Espanha", "posicao": "Defensor", "nota_performance": 6.5, "e_capitao": False},
    {"nome": "Robert Lewandowski", "idade": 36, "altura": 1.85, "nacionalidade": "Polônia", "posicao": "Atacante", "nota_performance": 8.5, "e_capitao": True}
]

# Definir o capitão:
capitao_nome = "Robert Lewandowski"

# 2. Função de Cálculo de Peso da Aresta (Refinada)

def calcular_peso_aresta(jogador1, jogador2):
    # Peso base inicial: quanto maior, mais 'distante' os jogadores estão por padrão.
    peso = 10.0

    # 1. Mesma Posição: Conexão muito forte
    if jogador1["posicao"] == jogador2["posicao"]:
        peso -= 4.0 # Reduz significativamente o peso (menor peso = conexão mais forte)

    # 2. Mesma Nacionalidade: Conexão forte
    if jogador1["nacionalidade"] == jogador2["nacionalidade"]:
        peso -= 3.0 # Reduz o peso

    # 3. Proximidade de Altura (quanto menor a diferença, menor o impacto no peso)
    if jogador1["altura"] is not None and jogador2["altura"] is not None:
        # Altura máxima: 1.96m (Wojciech Szczesny), mínima: 1.70m (Guille Fernández). Diferença máxima: 0.26m
        diferenca_altura = abs(jogador1["altura"] - jogador2["altura"])
        # Normaliza a diferença para um fator entre 0 e 1 e escala
        peso += (diferenca_altura / 0.26) * 1.5 # Adiciona um custo proporcional à diferença, com impacto médio
    else:
        # Penalidade maior se a altura for desconhecida para qualquer um dos jogadores
        peso += 2.0

    # 4. Proximidade de Idade (quanto menor a diferença, menor o impacto no peso)
    # Idade máxima: 36 (Lewandowski), mínima: 16 (Toni Fernández). Diferença máxima: 20
    diferenca_idade = abs(jogador1["idade"] - jogador2["idade"])
    peso += (diferenca_idade / 20.0) * 1.0 # Impacto um pouco menor que a altura, mas ainda relevante

    # 5. Proximidade de Nota de Performance (quanto menor a diferença, menor o impacto no peso)
    # Nota máxima: 9.0 (Ter Stegen), mínima: 5.0 (Vários). Diferença máxima: 4.0
    diferenca_nota = abs(jogador1["nota_performance"] - jogador2["nota_performance"])
    peso += (diferenca_nota / 4.0) * 2.5 # Impacto mais significativo, pois é uma métrica chave de performance

    # Garantir um peso mínimo positivo para evitar problemas com alguns algoritmos (como Dijkstra)
    return max(0.1, peso) # Peso mínimo para garantir que não haja caminhos "gratuitos" ou negativos.

# 3. Criando o Grafo com NetworkX

G = nx.Graph()

# Adicionar nós (jogadores) com seus atributos
for jogador in jogadores_data:
    G.add_node(jogador["nome"], **jogador) # Adiciona todos os atributos do dicionário como atributos do nó

# Adicionar arestas ponderadas
for i in range(len(jogadores_data)):
    for j in range(i + 1, len(jogadores_data)): # Evita duplicatas e conexões de um nó consigo mesmo
        jogador1 = jogadores_data[i]
        jogador2 = jogadores_data[j]

        # Garantir que não estamos conectando o mesmo jogador
        if jogador1["nome"] != jogador2["nome"]:
            peso = calcular_peso_aresta(jogador1, jogador2)
            G.add_edge(jogador1["nome"], jogador2["nome"], weight=peso)

# Exemplo de Verificação: Confirmação da criação do grafo
print(f"Grafo criado com {G.number_of_nodes()} nós e {G.number_of_edges()} arestas.")
print(f"Atributos de Lewandowski: {G.nodes[capitao_nome]}")
if G.has_edge("Robert Lewandowski", "Marc-André ter Stegen"):
    print(f"Peso da aresta Lewandowski-Ter Stegen: {G.edges['Robert Lewandowski', 'Marc-André ter Stegen']['weight']:.2f}")

# 4. Aplicação de Algoritmos e Cálculo de Métricas

print("\n--- Análise de Grafo ---")

# Encontrar o nó do capitão para usar nos algoritmos
capitao = None
for jogador in jogadores_data:
    if jogador["e_capitao"]:
        capitao = jogador["nome"]
        break

if capitao is None:
    print("Capitão não encontrado no conjunto de dados. Verifique o atributo 'e_capitao'.")
else:
    print(f"\nCapitão do time: {capitao}")

    ### 4.1. Busca em Largura (BFS)

    print("\n--- Busca em Largura (BFS) a partir do Capitão ---")
    # Para visualizar os "níveis" de conexão:
    
    # Nível 0: O próprio capitão
    print(f"Nível 0 (Capitão): {capitao}")

    # Nível 1: Jogadores diretamente conectados ao capitão
    vizinhos_capitao = list(G.neighbors(capitao))
    print(f"Nível 1 (Jogadores diretamente conectados ao capitão): {vizinhos_capitao}")

    # Nível 2: Jogadores a dois passos do capitão
    jogadores_2_passos = set()
    for vizinho in vizinhos_capitao:
        for vizinho_do_vizinho in G.neighbors(vizinho):
            # Garante que não é o capitão ou um vizinho direto já listado
            if vizinho_do_vizinho != capitao and vizinho_do_vizinho not in vizinhos_capitao:
                jogadores_2_passos.add(vizinho_do_vizinho)
    print(f"Nível 2 (Jogadores a dois passos do capitão): {list(jogadores_2_passos)}")

    ### 4.2. Algoritmo de Dijkstra

    print("\n--- Caminhos Mínimos com Dijkstra ---")
    # Dijkstra encontra o caminho mais curto ponderado (menor peso total).
    # Vamos encontrar o caminho mais 'forte' (menor peso total) do capitão para alguns jogadores chave.

    # Escolha de alguns alvos para Dijkstra
    alvos_dijkstra = []
    if "Marc-André ter Stegen" in G.nodes(): alvos_dijkstra.append("Marc-André ter Stegen") # Goleiro
    if "Pedri" in G.nodes(): alvos_dijkstra.append("Pedri") # Meio-campista
    if "Ronald Araújo" in G.nodes(): alvos_dijkstra.append("Ronald Araújo") # Defensor
    if "Lamine Yamal" in G.nodes(): alvos_dijkstra.append("Lamine Yamal") # Atacante promissor

    for alvo in alvos_dijkstra:
        if alvo == capitao:
            continue
        try:
            length, path = nx.single_source_dijkstra(G, source=capitao, target=alvo, weight='weight')
            print(f"\nCaminho mais 'forte' do {capitao} para {alvo}:")
            print(f"  Custo total (peso acumulado): {length:.2f}")
            print(f"  Caminho: {' -> '.join(path)}")
        except nx.NetworkXNoPath:
            print(f"\nNão há caminho entre {capitao} e {alvo}.")
        except Exception as e:
            print(f"\nErro ao calcular caminho entre {capitao} e {alvo}: {e}")

    ### 4.3. Métricas da Ciência das Redes

    print("\n--- Métricas da Ciência das Redes ---")

    # Grau dos Nós
    print("\nGrau dos Nós (Número de Conexões):")
    grau_nos = dict(G.degree())
    sorted_grau = sorted(grau_nos.items(), key=lambda item: item[1], reverse=True)
    for jogador, grau in sorted_grau[:10]: # Top 10
        print(f"  {jogador}: {grau}")
    print(f"  ...e mais {len(sorted_grau) - 10} jogadores.")


    # Centralidade de Grau (Normalizada)
    print("\nCentralidade de Grau:")
    centralidade_grau = nx.degree_centrality(G)
    sorted_centralidade_grau = sorted(centralidade_grau.items(), key=lambda item: item[1], reverse=True)
    for jogador, centralidade in sorted_centralidade_grau[:5]: # Top 5
        print(f"  {jogador}: {centralidade:.4f}")

    # Centralidade de Intermediação (Betweenness Centrality)
    print("\nCentralidade de Intermediação:")
    centralidade_inter = nx.betweenness_centrality(G, weight='weight') # Ponderada pelo peso
    sorted_centralidade_inter = sorted(centralidade_inter.items(), key=lambda item: item[1], reverse=True)
    for jogador, centralidade in sorted_centralidade_inter[:5]: # Top 5
        print(f"  {jogador}: {centralidade:.4f}")

    # Centralidade de Proximidade (Closeness Centrality)
    print("\nCentralidade de Proximidade:")
    centralidade_prox = nx.closeness_centrality(G, distance='weight') # Ponderada pelo peso
    sorted_centralidade_prox = sorted(centralidade_prox.items(), key=lambda item: item[1], reverse=True)
    for jogador, centralidade in sorted_centralidade_prox[:5]: # Top 5
        print(f"  {jogador}: {centralidade:.4f}")

    # Componentes Conectados
    print("\nComponentes Conectados:")
    num_componentes = nx.number_connected_components(G)
    print(f"  Número de componentes conectados: {num_componentes}")
    if num_componentes > 1:
        for i, componente in enumerate(nx.connected_components(G)):
            print(f"  Componente {i+1}: {list(componente)}")
    else:
        print("  A rede é totalmente conectada (todos os jogadores estão interligados).")

    # Diâmetro da Rede
    print("\nDiâmetro da Rede:")
    try:
        # O diâmetro do NetworkX calcula o caminho mais longo em termos de número de arestas (não ponderado).
        diametro = nx.diameter(G)
        print(f"  Diâmetro (não ponderado): {diametro}")
    except nx.NetworkXError as e:
        print(f"  Não foi possível calcular o diâmetro: {e}")
        print("  Isso geralmente acontece se o grafo não for conectado (tem mais de um componente).")

# 5. Visualização da Rede

print("\n--- Visualização da Rede ---")

plt.figure(figsize=(15, 12)) # Define o tamanho da figura para melhor visualização

# Definir o layout do grafo
# spring_layout é bom para mostrar clusters e nós centrais
pos = nx.spring_layout(G, k=0.7, iterations=50, seed=42) # Adicionei seed para reprodutibilidade do layout

# Listas para customização da visualização
node_colors = []
node_sizes = []
edge_widths = []
edge_alpha_values = [] # Renomeado para evitar confusão, serão os valores alpha para cada aresta
node_labels = {} 

# Iterar sobre os nós para definir cores, tamanhos e rótulos
for node in G.nodes():
    jogador_data = G.nodes[node]
    node_labels[node] = node # O rótulo será o próprio nome do jogador

    # Cor do nó: Capitão em destaque, outros por posição
    if jogador_data["e_capitao"]:
        node_colors.append("red") # Capitão em vermelho
        node_sizes.append(1200) # Capitão maior
    else:
        # Cores diferentes para cada posição
        if jogador_data["posicao"] == "Goleiro":
            node_colors.append("skyblue")
        elif jogador_data["posicao"] == "Defensor":
            node_colors.append("lightgreen")
        elif jogador_data["posicao"] == "Meio-campista":
            node_colors.append("orange")
        elif jogador_data["posicao"] == "Atacante":
            node_colors.append("gold")
        else:
            node_colors.append("lightgray") # Cor padrão
        node_sizes.append(600) # Tamanho padrão para outros jogadores

# Iterar sobre as arestas para definir largura e opacidade baseadas no peso
# Lembre-se: menor peso = conexão mais forte = linha mais grossa/escura
# Obter todos os pesos para encontrar min e max de forma segura
edge_weights = [data['weight'] for u, v, data in G.edges(data=True)]

if edge_weights: # Verifica se há arestas para evitar erro em grafo vazio
    max_weight = max(edge_weights)
    min_weight = min(edge_weights)
else: 
    max_weight = 1.0 # Valores padrão se não houver arestas ou se todos os pesos forem iguais
    min_weight = 0.0

for u, v, data in G.edges(data=True):
    weight = data['weight']
    
    # Normaliza o peso para uma escala de 0 a 1 (0 para o peso máximo, 1 para o mínimo)
    # Assim, pesos menores (conexões mais fortes) terão valores maiores para largura/opacidade
    if (max_weight - min_weight) > 0:
        normalized_strength = 1 - ((weight - min_weight) / (max_weight - min_weight)) 
    else:
        normalized_strength = 0.5 # Se todos os pesos forem iguais, força uma força média

    edge_widths.append(1 + (normalized_strength * 3)) # Largura da linha (de 1 a 4)
    edge_alpha_values.append(0.3 + (normalized_strength * 0.7)) # Opacidade (de 0.3 a 1.0)
    
# Desenhar os nós
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes, alpha=0.9)

# Desenhar as arestas com opacidade individual
# Note que passamos edge_alpha_values diretamente para alpha, junto com a cor base
nx.draw_networkx_edges(G, pos, width=edge_widths, edge_color="gray", alpha=edge_alpha_values)

# Desenhar os rótulos dos nós (nomes dos jogadores)
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=8, font_weight="bold")

# Adicionar título
plt.title("Rede de Conexões dos Jogadores do Barcelona", size=18)

# Adicionar legenda para as cores dos nós
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', label='Capitão',
               markerfacecolor='red', markersize=10),
    plt.Line2D([0], [0], marker='o', color='w', label='Goleiro',
               markerfacecolor='skyblue', markersize=10),
    plt.Line2D([0], [0], marker='o', color='w', label='Defensor',
               markerfacecolor='lightgreen', markersize=10),
    plt.Line2D([0], [0], marker='o', color='w', label='Meio-campista',
               markerfacecolor='orange', markersize=10),
    plt.Line2D([0], [0], marker='o', color='w', label='Atacante',
               markerfacecolor='gold', markersize=10)
]
plt.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout(rect=[0, 0, 0.85, 1]) # Ajusta o layout para acomodar a legenda
plt.show() # Exibe a visualização