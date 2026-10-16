var text = document.querySelector("#text");
var result = document.querySelector("#result");

text.addEventListener("input", function(){
    var value = text.value;
    if (value == "1"){
        result.innerHTML = "Janeiro = 30 dias";
    }
    else if (value == "2"){
        result.innerHTML = "Fevereiro = 28 dias";
    }
    else if (value == "3"){
        result.innerHTML = "Março = 31 dias";
    }
    else if (value == "4"){
        result.innerHTML = "Abril = 30 dias";
    }
    else if (value == "5"){
        result.innerHTML = "Maio = 31 dias";
    }
    else if (value == "6"){
        result.innerHTML = "Junho = 30 dias";
    }
    else if (value == "7"){
        result.innerHTML = "Julho = 31 dias";
    }
    else if (value == "8"){
        result.innerHTML = "Agosto = 31 dias";
    }
    else if (value == "9"){
        result.innerHTML = "Setembro = 30 dias";
    }
    else if (value == "10"){
        result.innerHTML = "Outubro = 31 dias";
    }
    else if (value == "11"){
        result.innerHTML = "Novembro = 30 dias";
    }   
    else if (value == "12"){   
        result.innerHTML = "Dezembro = 31 dias";
    }
    else if (value < 1 || value > 12){
        result.innerHTML = "Mês inválido";
    }
});