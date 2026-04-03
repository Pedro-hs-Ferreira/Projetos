let titulo = document.querySelector('h1');
titulo.innerHTML = 'Hora do desafio!';

function verificarClique() {
    console.log('O botão foi clicado!');
}
function verificarClique2() {
    alert('Eu amo JS');
}
function verificarClique3() {
    let cidade = prompt('Digite o nome de uma cidade no Brasil!');
    alert(`estive em ${cidade} e lembrei de você!`);
}
function verificarClique4() {
    let primeiroNumero = parseInt(prompt('Digite o primeiro número!'));
    let segundoNumero = parseInt(prompt('Digite o segundo número!'));
    let resultado = primeiroNumero + segundoNumero;
    alert(`${primeiroNumero} + ${segundoNumero} = ${resultado}!`);
}
