# Guia de Desenvolvimento – Chat RAG para Petshop

Este documento é meu ponto de partida antes de escrever qualquer linha de código.  
A ideia aqui é organizar o que será feito, o porquê de cada decisão e a sequência de implementação.  
Quero manter tudo simples, direto e com foco em qualidade.

---

## 1. Contexto

O objetivo do projeto é construir um chat capaz de responder perguntas sobre um petshop usando RAG (Retrieval Augmented Generation).  
As informações sobre o petshop virão de um banco SQL, e a resposta final será gerada por um modelo de linguagem.

A intenção é entregar uma solução leve, bem estruturada e fácil de entender. Nada de complexidade desnecessária — só o essencial feito com cuidado.

---

## 2. Objetivo do Sistema

- Permitir que o usuário pergunte algo no frontend (React).
- O backend (FastAPI) recebe a pergunta, procura informações relevantes no banco SQL e monta o contexto.
- A resposta final é gerada por um LLM (DeepSeek R1 via OpenRouter).
- O frontend exibe a resposta no formato de um chat simples.

O sistema deve ser:
- minimalista,
- performático,
- organizado,
- claro de ler e manter.

---

## 3. Escopo Funcional

**O que o sistema vai fazer:**
- Carregar documentos sobre o petshop (horários, serviços, políticas, produtos etc).
- Gerar embeddings locais desses documentos.
- Receber perguntas do usuário.
- Criar embedding da pergunta.
- Recuperar os documentos mais semelhantes usando similaridade de cosseno.
- Montar o contexto final.
- Chamar o LLM para gerar a resposta.
- Retornar a resposta para o frontend.
- Exibir o histórico do chat no navegador.

---

## 4. Arquitetura Geral

A solução terá três partes principais:

### 4.1 Backend (FastAPI)
- Organização em módulos:
  - `main.py` – inicialização da API
  - `routes/chat.py` – rota de chat
  - `database.py` – conexão SQLite + SQLAlchemy
  - `models.py` – tabela `Document`
  - `schemas.py` – Pydantic de entrada/saída
  - `embeddings.py` – modelo BGE small
  - `rag.py` – pipeline de retrieval e montagem de prompt
  - `llm.py` – integração com OpenRouter

### 4.2 Banco de Dados
- SQLite para facilitar o setup local.
- Tabela `documents` contendo:
  - id
  - title
  - content
  - embedding (lista de floats armazenada como texto/json)
- Um script `seed.py` será responsável por popular o banco com informações do petshop e gerar embeddings iniciais.

### 4.3 Frontend (React + Vite)
- Interface de chat simples.
- Input para pergunta.
- Exibição do histórico.
- Chamada POST para `/chat`.

---

## 5. Tecnologias e Motivações

- **FastAPI**: rápido, limpo e bom para APIs.
- **SQLite + SQLAlchemy**: leve e suficiente para RAG de teste.
- **Sentence Transformers (BGE Small)**: embeddings locais rápidos.
- **NumPy**: cálculo da similaridade de cosseno.
- **DeepSeek R1 via OpenRouter**: LLM real, gratuito, com boa capacidade.
- **React + Vite**: frontend rápido de montar e fácil de entender.
- **Pytest**: criar ao menos 1 ou 2 testes básicos.
- **dotenv**: gerenciar a chave de API do OpenRouter.

---

## 6. Fluxo RAG (resumo)

1. Pergunta chega no endpoint `/chat`.
2. Backend gera embedding da pergunta com BGE Small.
3. Carrega do banco os embeddings dos documentos.
4. Calcula a similaridade (cosine).
5. Seleciona os top K documentos.
6. Monta um prompt contendo:
   - instruções
   - contexto (textos dos documentos)
   - pergunta do usuário
7. Passa o prompt para o modelo DeepSeek R1 via OpenRouter.
8. Retorna a resposta estruturada para o frontend.
9. Frontend exibe a resposta no chat.

---

## 7. Etapas de Implementação (minhas tarefas na ordem)

1. Criar estrutura básica do repositório (backend + frontend).
2. Implementar o esqueleto do backend (FastAPI, SQLAlchemy, modelos).
3. Configurar embeddings locais (BGE small).
4. Criar `seed.py` com documentos do petshop e salvar embeddings.
5. Criar pipeline RAG:
   - geração de embedding da pergunta
   - recuperação dos documentos
   - montagem do prompt
6. Implementar a chamada para o DeepSeek R1 usando OpenRouter.
7. Conectar tudo na rota `/chat`.
8. Criar testes básicos:
   - endpoint `/chat`
   - função de retrieval
9. Implementar frontend React (UI simples de chat).
10. Criar README com instruções de uso.
11. Revisar tudo, testar ponta a ponta e limpar código.

---

## 8. Considerações de Qualidade

- Evitar código desnecessário.
- Priorizar legibilidade, organização e responsabilidade clara por módulo.
- Nunca expor a API key no repositório.
- Nomes de funções e variáveis claros.
- Testar cada parte isoladamente antes de integrar.

---

## 9. Próximos Passos Após o MVP

Essas não são prioridades para o desafio, mas documentar ajuda a mostrar visão:

- Trocar SQLite por Postgres (com pgvector).
- Trocar DeepSeek e BGE SMALL por OPEN ai
- Adicionar atualização dinâmica dos documentos.
- Implementar streaming das respostas.
- Criar Dockerfile para facilitar deploy.
- Criar testes adicionais.

---

## 10. Conclusão

Este documento resume o meu planejamento antes de começar a codar.  
Agora que as decisões principais estão estruturadas, posso iniciar o desenvolvimento com mais clareza e foco.

A meta é entregar uma solução enxuta, bem construída e que demonstre domínio dos conceitos envolvidos, sem exageros ou complexidade desnecessária.

