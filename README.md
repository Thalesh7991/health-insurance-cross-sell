# Health Insurance Cross Sell

![Image Inicial](/money.png)

## Problema de Negócio

<p>A Insurance All é uma empresa que fornece seguro de saúde para seus clientes e o time de produtos está
analisando a possibilidade de oferecer aos assegurados, um novo produto: Um seguro de automóveis.</p>

<p> A Insurance All fez uma pesquisa com cerca de 380 mil clientes sobre o interesse em aderir a um novo produto
de seguro de automóveis, no ano passado. Todos os clientes demonstraram interesse ou não em adquirir o
seguro de automóvel e essas respostas ficaram salvas em um banco de dados junto com outros atributos dos
clientes. </p>

<p>O time de produtos selecionou 127 mil novos clientes que não responderam a pesquisa para participar de uma
campanha, no qual receberão a oferta do novo produto de seguro de automóveis. A oferta será feita pelo time
de vendas através de ligações telefônicas.
  
Contudo, o time de vendas tem uma capacidade de realizar 20 mil ligações dentro do período da campanha. </p>

## O Desafio

<p> Nesse contexto, fui contratado como um consultor de Ciência de Dados para construir um modelo que
prediz se o cliente estaria ou não interessado no seguro de automóvel.
  
Com a minha solução, o time de vendas espera conseguir priorizar as pessoas com maior interesse no novo
produto e assim, otimizar a campanha realizando apenas contatos aos clientes mais propensos a realizar a
compra.
 </p>
 
 <p> Além disso ao final da consultoria devo entregar um relatório contendo algumas análises e respostas
às seguintes perguntas:
 </p>
 
 **Primeira Análise:** Qual a porcentagem de clientes interessados em adquirir um seguro de automóvel, o time de vendas conseguirá contatar fazendo 20.000 ligações?
 
 **Segunda Análise:** E se a capacidade do time de vendas aumentar para 40.000 ligações, qual a porcentagem de clientes interessados em adquirir um seguro de automóvel o time de vendas conseguirá contatar?
 
 **Terceira Análise:** Quantas ligações o time de vendas precisa fazer para contatar 80% dos clientes interessados em adquirir um seguro de automóvel?
 
 ## Dados Disponíveis para Análise
 
|      Atributos      |       Descrição      |
| ------------------- |  ------------------- | 
|  Id |  ID único do cliente |
|  Gender |  Sexo do Cliente |
|  Age |  Idade do Cliente |
|  Driving License |  0: se não possui carteira de motorista, 1: se possui|
|  Region Code |  Código único da região do cliente |
|  Previously Insured |  1: Cliente já teve seguro de carro, 0: nunca teve  |
|  Vehicle Age |  Tempo do carro do cliente |
|  Vehicle Damage |  1: Cliente já teve carro danificado no passado, 0: nunca teve |
|  Annual Premium |  Valor total pago no seguro em um ano |
|  Policy Sales Channel |  Código anonimizado para o canal de divulgação ao cliente ou seja. Agentes diferentes, por correio, por telefone, pessoalmente, etc |
|  Vintage |  Número de dias que o cliente foi associado à empresa |
|  Response |  1 : O cliente está interessado, 0 : O cliente não está interessado |

## Estratégia de Solução

***Minha estratégia para resolver esse desafio foi:***

**Step 01. Data Description:**  O objetivo é utilizar métricas estatísticas para identificar outliers no escopo do negócio.

**Step 02. Feature Engineering:** Derivar novos atributos com base nas variáveis originais para descrever melhor o fenômeno a ser modelado.

**Step 03. Exploratory Data Analysis:** Explorar os dados para encontrar insights e entender melhor o impacto das variáveis no aprendizado do modelo.

**Step 04. Data Preparation:** Preparar os dados para que os modelos de aprendizado de máquina possam aprender um comportamento específico.

**Step 05. Feature Selection:** Seleção dos atributos mais significativos para treinar o modelo.

**Step 06. Machine Learning Modelling:** Treinamento do modelo de aprendizado de máquina.

**Step 07. Hyperparameter Fine Tunning:** Escolher os melhores valores para cada um dos parâmetros do modelo selecionado na etapa anterior.

**Step 08. Convert Model Performance to Business Values:** Converter o desempenho do modelo em um resultado de negócios.

**Step 09. Deploy Modelo to Production:** Publicar o modelo em um ambiente web para que outras pessoas ou serviços possam usar os resultados para melhorar a decisão de negócios.

## Performance do Modelo de Machine Learning

| Modelo  |  precision_at_20000  | precision_at_40000  |  recall_at_20000  | recall_at_20000 |
| ------------------- | ------------------- | ------------------- | ------------------- | ------------------- |
|  Random Forest |  0,302	 |  0.226 |  	0,661 | 0.988 |
|  Extra Trees |  0.295 |  0.224 |  0.646 | 0.981 |
|  KNN |  0.294	 |  0.214	 |  0.644 | 0.938 |
|  Linear Regression |  0.263 |  0.227 |  0.576 | 0.994 |


O modelo escolhido foi a **Random Forest**, pois apresentou melhores resultados de rankeamento.
