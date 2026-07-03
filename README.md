# Mobility Data Treatment

Este projeto tem como objetivo consumir dados brutos de mobilidade, inicialmente a partir de um CSV mockado de rastreador, normalizar, classificar, validar e transformar esses dados em um modelo tratado canônico chamado `MobilityEvent`.

O projeto não implementa um Lakehouse completo neste momento. A proposta atual é construir apenas o núcleo de tratamento de dados, mantendo uma estrutura simples e escalável para futura evolução para camadas como Bronze, Silver e Gold.

## Objetivo atual

Transformar dados brutos em dados tratados confiáveis.

Fluxo esperado:

```text
Dado bruto
    ↓
Extração
    ↓
Normalização
    ↓
Classificação
    ↓
Validação
    ↓
Transformação
    ↓
MobilityEvent