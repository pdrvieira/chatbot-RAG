# 🐾 Chat Petshop - Frontend

Interface web moderna para o sistema de chat RAG do Petshop.

## 🛠️ Stack Tecnológica

- **React 18** - Biblioteca UI
- **Vite** - Build tool e dev server
- **TypeScript** - Type safety
- **Tailwind CSS** - Estilização utilitária

## 🚀 Como Rodar

### Instalação

```bash
npm install
```

### Desenvolvimento

```bash
npm run dev
```

O app estará disponível em `http://localhost:5173`

### Build para Produção

```bash
npm run build
```

## 📁 Estrutura do Projeto

```
frontend/
├── src/
│   ├── components/       # Componentes reutilizáveis
│   ├── lib/             # Utilitários e API client
│   ├── styles/          # Estilos globais e Tailwind
│   ├── App.tsx          # Componente principal
│   └── main.tsx         # Entry point
├── index.html
├── package.json
├── vite.config.ts
├── tsconfig.json
└── tailwind.config.js
```

## 🔗 Backend

O frontend se comunica com a API FastAPI rodando em `http://localhost:8000`

Endpoint principal: `POST /chat`
- Request: `{ "question": string }`
- Response: `{ "answer": string, "sources": string[] }`

## 📝 Próximos Passos

- [ ] Implementar componentes de chat
- [ ] Integrar com API do backend
- [ ] Adicionar tratamento de erros
- [ ] Melhorar acessibilidade

