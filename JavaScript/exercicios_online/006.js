const descontos = [0.05, 0.10, 0.12];
const confirmar = document.querySelector('#Confirmar');
let tex1 = document.querySelector('#Text1');
let tex2 = document.querySelector('#Text2');
let tex3 = document.querySelector('#Text3');
let tex4 = document.querySelector('#Text4');
let show_desconto = document.querySelector('#Desconto');
let show_total = document.querySelector('#Total');

confirmar.addEventListener('click', function() {
    let desconto = 0;
    let total = 0;

    let valor1 = tex1.value;
    let valor2 = tex2.value;

    let v1 = parseFloat(tex3.value) || 0;
    let v2 = parseFloat(tex4.value) || 0;

    if (valor1 === 'Laranja' && valor2 === 'Frango' || valor1 === 'Frango' && valor2 === 'Laranja') {
        desconto = descontos[0];

        total = ((2.50 * v1) + (15.00 * v2)) * (1 - desconto);

        show_desconto.innerHTML = 'DESCONTO: ' + descontos[0];
        show_total.innerHTML = 'TOTAL: ' + total.toFixed(2);
    }
    else if (valor1 === 'Maçã' && valor2 === 'Linguiça' || valor1 === 'Linguiça' && valor2 === 'Maçã') {
        desconto = descontos[1];

        total = ((3.00 * v1) + (16.00 * v2)) * (1 - desconto);

        show_desconto.innerHTML = 'DESCONTO: ' + descontos[1];
        show_total.innerHTML = 'TOTAL: ' + total.toFixed(2);
    }
    else if (valor1 === 'Uva' && valor2 === 'Peixe' || valor1 === 'Peixe' && valor2 === 'Uva') {
        desconto = descontos[2];

        total = ((4.00 * v1) + (25.00 * v2)) * (1 - desconto);

        show_desconto.innerHTML = 'DESCONTO: ' + descontos[2];
        show_total.innerHTML = 'TOTAL: ' + total.toFixed(2);
    }
});