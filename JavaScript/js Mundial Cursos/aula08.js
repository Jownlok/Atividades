/*
    OBJETOS = Variáveis com muitos valores/propriedades dentro;
    Ex.: const carro = {marca:'ford', modelo:'Ra', ano:'2026'}
    Objetos podem ser métodos = funções colocadas dentro de uma propriedade
*/
const carro = {marca:'ford', modelo:'ka', ano:'2015', placa:'ABC-1234', completo: function(){return "A marca é" + this.marca}};
// This.xyz é para imprimir valores das propriedas dentro do próprio objeto

console.log(carro.completo()) /*Chamo a função que imprime = A marca é ford */



