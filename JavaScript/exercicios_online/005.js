var text=document.querySelector("#text");
var pull=document.querySelector("#pull");
var result=document.querySelector("#result");

pull.addEventListener("click", function(){
    valor = parseFloat(text.value);

    if (valor > 0){
        if (valor % 2 === 0){
            result.innerHTML = 'O número é par e positivo'
        }else{
            result.innerHTML = 'O número é ímpar e positivo'

        }
    }

    else if (valor < 0){
        if (Math.abs(valor) % 2 === 0){
            result.innerHTML = 'O número é par e negativo'
        }else{
            result.innerHTML = 'O número é ímpar e negativo'

        }
    }

});