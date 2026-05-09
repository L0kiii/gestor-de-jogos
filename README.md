# 🎮 Gestor de Jogos

Projeto feito em Python para gerenciar jogos que quero zerar. Permite adicionar jogos, registrar o tempo de conclusão, acompanhar o histórico de atualizações e persistir os dados em um arquivo JSON.
---

## ✨ Funcionalidades

- ➕ Adicionar um ou mais jogos de uma vez
- 🔍 Verificação automática de jogos duplicados
- ✅ Marcar jogos como concluídos com o tempo levado para zerar
- ⏱️ Atualizar o tempo de jogo sem precisar marcar como concluído
- 📋 Listar todos os jogos com status e histórico formatado
- 🗑️ Excluir jogos da lista
- 📝 Histórico detalhado de atualizações por jogo
- 💾 Persistência automática dos dados em arquivo JSON

---

## 🚀 Como usar

### Pré-requisitos

- Python 3.x instalado

### Executando o projeto

```bash
python gestor_jogos.py
```

### Comandos disponíveis

| Comando  | Descrição                                        |
|----------|--------------------------------------------------|
| `ADD`    | Adiciona um ou mais jogos                        |
| `SHOW`   | Lista todos os jogos com status e histórico      |
| `UPDATE` | Atualiza status ou tempo de jogo                 |
| `DELETE` | Remove um jogo da lista                          |
| `ABOUT`  | Exibe informações sobre o projeto                |
| `QUIT`   | Salva os dados e encerra o programa              |

---

## 📁 Estrutura do projeto

```
gestor-jogos/
│
├── gestor_jogos.py   # Código principal
├── jogos.json        # Banco de dados local (gerado automaticamente)
├── .gitignore
└── README.md
```

---

## 🗄️ Exemplo de dados salvos (jogos.json)

```json
[
    {
        "nome": "Elden Ring",
        "tempo": 72.5,
        "concluido": true,
        "historico": [
            {
                "data": "2026-03-10 18:00:00",
                "tempo": 50.0
            },
            {
                "data": "2026-03-15 21:30:00",
                "concluido": true,
                "tempo": 72.5
            }
        ]
    },
    {
        "nome": "Hollow Knight",
        "tempo": 12.0,
        "concluido": false,
        "historico": [
            {
                "data": "2026-04-01 20:00:00",
                "tempo": 12.0
            }
        ]
    }
]
```

---

## 🖥️ Exemplo de saída (comando SHOW)

```
JOGO: ELDEN RING
TEMPO DE JOGO: 72.5 horas
CONCLUÍDO: Sim
HISTÓRICO:
  DATA: 10/03/2026
  HORA: 18:00
  CONCLUÍDO: Não
  TEMPO DE JOGO: 50.0h

  DATA: 15/03/2026
  HORA: 21:30
  CONCLUÍDO: Sim
  TEMPO DE JOGO: 72.5h
```

---

## 🛠️ Tecnologias utilizadas

- **Python 3**
- Módulo `json` — persistência de dados
- Módulo `datetime` — registro de datas no histórico

---

## 👤 Autor

**L0ki**
