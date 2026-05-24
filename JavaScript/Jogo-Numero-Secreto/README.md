````md
# 🎯 Jogo Do Número Secreto

Um jogo simples e divertido desenvolvido em JavaScript onde o jogador precisa adivinhar um número secreto gerado aleatoriamente pelo sistema.

---

## 📌 Sobre o Projeto

O **Jogo Do Número Secreto** sorteia números entre **1 e 10** e dá dicas ao jogador informando se o número secreto é maior ou menor que o chute informado.

O projeto também utiliza síntese de voz para narrar as mensagens exibidas na tela utilizando a biblioteca **ResponsiveVoice**.

---

## 🚀 Tecnologias Utilizadas

- HTML5
- CSS3
- JavaScript
- ResponsiveVoice

---

## 🎮 Como Funciona

1. O sistema gera um número aleatório entre 1 e 10.
2. O jogador digita um número no campo de entrada.
3. O jogo informa se o número secreto é:
   - Maior 📈
   - Menor 📉
4. Quando o jogador acerta:
   - Uma mensagem de vitória é exibida 🎉
   - O número de tentativas aparece na tela
5. O jogador pode reiniciar a partida e jogar novamente.

---

## 📂 Estrutura Principal do Código

### Funções principais:

| Função | Descrição |
|---|---|
| `exibirTextoNaTela()` | Exibe textos na tela e ativa a voz |
| `exibirMensagemInicial()` | Mostra a mensagem inicial do jogo |
| `verificarChute()` | Verifica se o jogador acertou |
| `gerarNumeroAleatorio()` | Gera números aleatórios sem repetição |
| `limparCampo()` | Limpa o campo de input |
| `reiniciarJogo()` | Reinicia o jogo |

---

## 🧠 Lógica do Projeto

O jogo possui:
- Controle de tentativas
- Sorteio sem repetição dos números
- Reinicialização automática da lista quando todos os números forem usados
- Feedback visual e por voz

---

## ▶️ Como Executar

1. Clone este repositório:

```bash
git clone https://github.com/Pedro-hs-Ferreira/jogo-numero-secreto.git
````

2. Abra o arquivo `index.html` no navegador.

---

## 📸 Demonstração

```txt
🎯 Jogo do número secreto!
Escolha um número entre 1 e 10
```

---

## 📚 Aprendizados

Este projeto ajuda a praticar:

* Variáveis
* Funções
* Condições
* Arrays
* Manipulação do DOM
* Eventos
* Recursividade
* Integração com bibliotecas externas

---

## 👨‍💻 Autor

Projeto desenvolvido por Pedro Ferreira 🚀

```
```
