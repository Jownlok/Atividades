var area, nome, button, saida;
button = document.querySelector("#Button");
area = document.querySelector("#Area");
saida = document.querySelector("#Saida");

button.addEventListener('click', function(){
    // PEGANDO O VALOR DO TEXTO
    nome = area.value;
    // COMPARANDO O VALOR, CASO POSITIVO É DIRECIONADO A OUTRA PÁGINA
    if(nome == 'João'){
        saida.innerHTML = 'Bem Vindo!'
        // ABRE UMA NOVA PÁGINA em outra guia
        window.open('../exercicios_online/ex_html/005.html', '_blank')
    }
    else{
        saida.innerHTML = 'Nome não reconhecido.'
    }
});