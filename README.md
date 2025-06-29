# Maior Número

Função \`maior_numero(a, b, c)\` em Python que retorna o maior entre três valores.

## Conteúdo

- \`maior_numero.py\`: implementação da função e script interativo.  
- \`test_maior_numero.py\`: testes unitários com \`pytest\`.  
- \`.github/workflows/python-app.yml\`: CI para rodar testes automaticamente.

## Como usar

1. Clone o repositório:
   \`\`\`bash
   git clone git@github.com:matheussiqueirahub/maior_numero.git
   cd maior_numero
   \`\`\`
2. (Opcional) Crie e ative um ambiente virtual:
   \`\`\`bash
   python3 -m venv .venv
   source .venv/bin/activate
   \`\`\`
3. Rode o script:
   \`\`\`bash
   python3 maior_numero.py
   \`\`\`

## Testes

1. Instale o pytest:
   \`\`\`bash
   pip install pytest
   \`\`\`
2. Execute:
   \`\`\`bash
   pytest -q
   \`\`\`

## CI/CD

A cada push na branch \`main\`, o GitHub Actions executa os testes via workflow.

