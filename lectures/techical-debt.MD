## Quadrante do Débito Técnico

Que tipo de falhas de decisões podem ser consideradas como débito técnico? Para Uncle Bob, decisões erradas produzidas por pessoas que desconhecem (ou não dominam) as boas práticas não são necessariamente débitos técnicos.

> O termo "débito técnico" deve ser reservado para casos em que as pessoas tomaram uma decisão **ponderada** de adotar uma estratégia de design que não é sustentável a longo prazo, mas produz um benefício de curto prazo, como fazer um lançamento. A questão é que a dívida rende valor mais cedo, mas precisa ser quitada o quanto antes.

Para Fowler, a decisão de chamar uma escolha equivocada de débito técnico não é o cerne da questão. Segundo o autor, débito técnico é uma **metáfora** que tem por objetivo auxiliar sobre como os problemas de decisão são comunicados e resolvidos. O débito técnico como metáfora torna mais amigável o processo de comunicá-lo para pessoas não-técnicas.

Há diferenças entre o débito técnico prudente e aquele que é irresponsável. Além disso, há também diferença entre o débito técnico deliberado e aquele que foi inadvertidamente percebido. Dessa maneira, é possível dividir débitos técnicos nos quadrantes: irresponsável/prudente e deliberado/inadvertido.

```
+-----------------------------------------------------+
|       Irresponsável     |         Prudente          |
|-------------------------|---------------------------|
|  "Nós não temos tempo   |   "Nós devemos entregar   |
|    para design"         |     agora e lidar com     |
|                         |     as consequencias"     |
|                         |                           |
| Deliberado              |                           |
+-------------------------+---------------------------+
| Inadvertido             |                           |
|                         |                           |
|  "O que é divisão em    |   "Agora nós sabemos como |
|       camadas?"         |     nós deveríamos ter    |
|                         |            feito"         |
|                         |                           |
+-----------------------------------------------------+
```

### References
https://martinfowler.com/bliki/TechnicalDebtQuadrant.html
