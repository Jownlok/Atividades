const button = document.querySelector('#confirm');
let result = document.querySelector('#result');

button.addEventListener('click', function(){
    let box = document.querySelector('#box').value.toLowerCase();
    
    if(box === 'a' || box === 'e' || box === 'i' || box === 'o' || box === 'u') {
        result.innerHTML = "A letra é uma vogal.";
    }
    else{
        result.innerHTML = "A letra é uma consoante.";
    }
});