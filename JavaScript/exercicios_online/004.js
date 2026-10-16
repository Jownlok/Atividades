var num1 = document.querySelector("#num1");
var num2 = document.querySelector("#num2");
var button = document.querySelector("#button");
var result = document.querySelector(".resultado");

button.addEventListener("click", function(){
    valor1=parseFloat(num1.value);
    valor2=parseFloat(num2.value);

    if (valor1 > valor2){
        result.innerHTML = `${valor1} é maior que ${valor2}`;
    }
    else if(valor2 > valor1){
        result.innerHTML = `${valor2} é maior que ${valor1}`;
    }
    else if(valor1 == valor2){
        result.innerHTML = "Os valores são iguais"
    }
});

