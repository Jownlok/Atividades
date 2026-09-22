const inputTexto = document.querySelector("#Texto");
const botao = document.querySelector("#Botao");
const resultado = document.querySelector(".resultado");

botao.addEventListener('click', function desconto(){
    const valorFloat = parseFloat(inputTexto.value.replace(',', '.'));
    let valorDesconto = valorFloat * 0.15;
    let total = valorDesconto + valorFloat;
    resultado.innerHTML = total.toFixed(2);
});