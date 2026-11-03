from github import Github, GithubException
from github import Auth

# ===================================================================
# 1. AUTENTICAÇÃO SEGURA
# ===================================================================
# COLE O SEU TOKEN ENTRE AS ASPAS:
TOKEN = ""

auth = Auth.Token(TOKEN)
g = Github(auth=auth)

try:
    user = g.get_user()
    print(f"✅ Conectado com sucesso como: {user.login}")
except Exception as e:
    print(f"❌ Erro ao conectar ao GitHub: {e}")
    exit()

# ===================================================================
# FUNÇÕES DO AGENTE
# ===================================================================

def atualizar_readme_perfil():
    """Atualiza o README do perfil principal."""
    repo_name = user.login
    
    conteudo_readme = f"""# Olá! Eu sou o Mariel 👋

🎓 Estudante de **Análise e Desenvolvimento de Sistemas** na UNINASSAU (Recife/PE)
💻 Foco em **Desenvolvimento Front-end & Engenharia de Software**

---

### 🛠️ Stacks & Tecnologias
- **Linguagens:** JavaScript, Python, C#, Java, HTML5, CSS3
- **Frameworks & Libs:** React
- **Ferramentas:** VS Code, PyCharm, Git, GitHub, Figma

---

📫 Conecte-se comigo no [LinkedIn](https://linkedin.com)!
"""

    try:
        repo = user.get_repo(repo_name)
    except GithubException:
        print(f"⚡ Criando o repositório de perfil '{repo_name}'...")
        repo = user.create_repo(repo_name, auto_init=True)

    try:
        contents = repo.get_contents("README.md")
        repo.update_file(
            path="README.md",
            message="docs: atualização automática do README do perfil",
            content=conteudo_readme,
            sha=contents.sha
        )
        print("🚀 README do perfil atualizado com sucesso no GitHub!")
    except GithubException:
        repo.create_file(
            path="README.md",
            message="docs: criação automática do README do perfil",
            content=conteudo_readme
        )
        print("🚀 README do perfil criado com sucesso no GitHub!")


def criar_ficheiro_licenca(nome_repo):
    """Cria um ficheiro LICENSE (MIT) na raiz do repositório especificado."""
    try:
        repo = user.get_repo(nome_repo)
    except GithubException:
        print(f"❌ Repositório '{nome_repo}' não foi encontrado na sua conta.")
        return

    texto_licenca = f"""MIT License

Copyright (c) 2026 {user.name or user.login}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

    try:
        contents = repo.get_contents("LICENSE")
        print(f"ℹ️ O repositório '{nome_repo}' já possui um ficheiro LICENSE.")
    except GithubException:
        repo.create_file(
            path="LICENSE",
            message="docs: adição da licença MIT pelo agente",
            content=texto_licenca
        )
        print(f"📄 Ficheiro LICENSE (MIT) criado com sucesso em '{nome_repo}'!")


def gerar_readme_projeto(nome_repo, titulo_projeto, descricao, tecnologias, instrucoes_execucao=""):
    """Gera um README.md profissional para um repositório de projeto."""
    try:
        repo = user.get_repo(nome_repo)
    except GithubException:
        print(f"❌ Repositório '{nome_repo}' não foi encontrado na sua conta.")
        return

    tech_list = "\n".join([f"- {tech}" for tech in tecnologias])

    conteudo_readme = f"""# {titulo_projeto}

{descricao}

---

## 🛠️ Tecnologias Utilizadas
{tech_list}

---

## 🚀 Como Executar o Projeto

```bash
# Clone o repositório
git clone [https://github.com/](https://github.com/){user.login}/{nome_repo}.git

# Acesse a pasta do projeto
cd {nome_repo}

{instrucoes_execucao or '# Siga as instruções específicas de execução aqui'} """

    # ===================================================================
# EXECUÇÃO
# ===================================================================
print("\n=== Iniciando as ações do agente GitHub ===")

# 1. Atualiza o README do seu perfil principal
atualizar_readme_perfil()

# 2. Cria o arquivo LICENSE (MIT) no repositório escolhido
# (Troque 'SEU_REPOSITORIO' pelo nome exato de um repositório seu)
criar_ficheiro_licenca("Agente-GITHUB")

# 3. Gera um README profissional para o seu repositório
gerar_readme_projeto(
    nome_repo="Agente-GITHUB",
    titulo_projeto="Agente GitHub",
    descricao="Agente para personalizar o seu repositório ou perfil no GitHub.",
    tecnologias=["Python"],
    instrucoes_execucao="npm install\nnpm start"
)