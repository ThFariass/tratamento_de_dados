# tratamento_de_dados

Durante esta etapa de tratamento de dados, aplicamos um fluxo claro e direto em Python para deixar nossa base pronta para análises avançadas. Primeiro, extraímos o arquivo CSV e mapeamos cada campo às suas regras de padronização. Por exemplo, ajustamos nomes de endereços garantindo que entradas com apenas uma palavra fossem classificadas como “Endereço Incompleto” e formatamos corretamente as demais. Para o campo de estados, convertemos todas as siglas para letras maiúsculas e validamos contra a lista oficial de UFs, rotulando automaticamente como “UF Desconhecida” quando necessário. As categorias de produtos ganharam uniformidade: transformamos variações como “alimentos” e “alimento” em “Alimento”, “roupas” em “Roupas” e agrupamos qualquer entrada em branco sob o rótulo “Outros”.

No tratamento de e‑mails, criei uma expressão regular que valida domínios e sufixos, convertendo tudo para letras minúsculas e sinalizando, com o texto “Email Inválido”, casos fora do padrão. Ao final, cada coluna passou por sua respectiva função de transformação, resultando em valores consistentes e de fácil interpretação.

O processo seguiu o conceito de ETL (Extract, Transform, Load): extraímos os dados originais, aplicamos transformações específicas para cada atributo e, por fim, geramos um arquivo CSV limpo e padronizado. Esse pipeline Python assegura que a base esteja organizada, pronta para alimentar relatórios, dashboards ou qualquer análise que vier a ser realizada, garantindo confiabilidade e agilidade em projetos futuros.

Arquivo src contem os scripts.
Arquivo data contem o csv atualizado
