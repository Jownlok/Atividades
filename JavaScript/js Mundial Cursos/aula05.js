// Let não permite redeclaração de variável
// let nome = "João";
// let nome = "Vitor";

var x = 10;
{
    var x = 2;
}

alert(x);

const não muda o valor da variável
const nome = "João";
nome = "Vitor"; // Isso vai gerar um erro
