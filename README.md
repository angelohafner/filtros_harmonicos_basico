
# Cálculos Básicos de Filtros Harmônicos

Este repositório contém dois scripts em Python para realizar cálculos básicos de filtros harmônicos, voltados para aplicações em filtros sintonizados e filtros amortecidos. Cada script calcula parâmetros importantes, como impedância, corrente, tensão, potência e frequências de sintonia, além de fornecer suporte para configurações de células capacitivas.

## Arquivos

1. **filtro_sitonizado.py**  
   Este script calcula os parâmetros de um filtro LC sintonizado. Ele é útil para aplicações em que se deseja sintonizar o filtro a uma frequência específica.

2. **filtro_amortecido.py**  
   Este script calcula os parâmetros de um filtro LC amortecido, incluindo a resistência adicional no indutor, usada para obter um comportamento de amortecimento.

## Funções Principais

Ambos os arquivos contêm as seguintes funções principais:

- **frequencia_sintonia(L, C)**: Calcula a frequência de sintonia do filtro LC.
- **calcular_impedancia(...)**: Calcula a impedância dos elementos R, L e C.
- **calcular_corrente_tensao(...)**: Calcula a corrente e tensão em cada elemento a partir da tensão de linha.
- **calcular_potencia(...)**: Calcula a potência em cada elemento com base na tensão e corrente.
- **calcular_filtro_estrela(...)**: Função principal para calcular todas as propriedades do filtro em estrela (impedância, corrente, tensão e potência).

Cada script fornece uma função adicional para configuração de células capacitivas:

- **celulas(...)**: Configura o número de células capacitivas em série e paralelo, calcula a capacitância nominal, a potência e a tensão para a configuração desejada.

## Exemplo de Uso

### 1. **Filtro Sintonizado**

Para rodar o script `filtro_sitonizado.py`, defina os valores de entrada e execute o script. Ele imprimirá os resultados de cálculo e exibe um dicionário `resultado_formatado` com os dados formatados para cada elemento do filtro.

### 2. **Filtro Amortecido**

No script `filtro_amortecido.py`, os cálculos incluem uma resistência no indutor, que afeta a impedância e a potência do filtro. Ao definir os valores e executar o script, os resultados são exibidos de forma semelhante ao script do filtro sintonizado.

## Requisitos

Estes scripts dependem das bibliotecas Python `numpy` para cálculos numéricos. Instale-as com o comando:

```bash
pip install numpy
```

## Executando os Scripts

Execute cada script em Python diretamente para visualizar os cálculos no console:

```bash
python filtro_sitonizado.py
python filtro_amortecido.py
```

## Contato

Para dúvidas ou sugestões, entre em contato.
