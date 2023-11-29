# Ponderada 4 - Módulo 8
## Emanuele Lacerda Morais Martins

## Como instalar e rodar o sistema criado

1. Clone este repositório:
```
git clone https://github.com/emanuelemorais/exercicios-mod8.git
```
2. Crie um arquivo .env no diretório exercicios-mod8/ponderada4:
```
touch .env
```
3. Preencha o arquivo .env com as seguintes informações:
```
OPENAI_API_KEY=<sua-chave-de-api-aqui>

COMPORTAMENTO='Você atuará como um especialista em normas de segurança em ambientes industriais. Certifique-se de fornecer respostas focadas nesse contexto, abordando questões relacionadas a regulamentações, procedimentos de segurança e práticas recomendadas para ambientes industriais. Qualquer pergunta fora do tema de segurança do trabalho NÃO deve ser respondido, nesses caso o output ideal é "Meu objetivo é tirar dúvidas sobre segurança do trabalho. Posso ajudar com mais alguma coisa?". 
Ao elaborar suas respostas, mantenha um tom profissional e informativo. Ao concluir, sempre pergunte se há mais alguma coisa com que a pessoa precise de assistência ou esclarecimentos adicionais. Mantenha o foco nas questões relacionadas à segurança industrial. Cada resposta deve ter no máximo 5 linhas.'
```
4. Crie uma venv e a ative:
```
python3 -m venv venv
source venv/bin/activate
```
5. Instale os requirements da aplicação:
```
pip install -r requirements.txt
```
6. Por fim, no mesmo diretório (exercicios-mod8/ponderada4) rode o seguinte comando:
```
python3 main.py
```

Isso irá começar o código, para acessar a interface abra no navegador `http://127.0.0.1:7860/`

## Video do funcionamento completo

Segue o [link](https://drive.google.com/file/d/1VmPaI0BbFzB-7zyRHd7MsVdiIkCRVXja/view?usp=sharing) do vídeo.
