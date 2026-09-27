var blocoum = document.querySelector('#blocoum');
var blocodois = document.querySelector('#blocodois');
var valor = document.querySelector('#escolha');
var resultado = document.querySelector('#resultado');
var confirmar = document.querySelector('#confirmar');

confirmar.addEventListener('click', function calcular() {
    var n1 = parseFloat(blocoum.value);
    var n2 = parseFloat(blocodois.value);
    var escolha = valor.value
    
    if (escolha === 'somar'){
        let total = n1 + n2;
        resultado.innerHTML = total;
    }
    else if (escolha === 'subtrair'){
        let total = n1 - n2;
        resultado.innerHTML = total;
    }
    else if (escolha === 'multiplicar'){
        let total = n1 * n2;
        resultado.innerHTML = total;
    }
    else if (escolha === 'dividir'){
        let total = n1 / n2;
        resultado.innerHTML = total;
    }
} );
