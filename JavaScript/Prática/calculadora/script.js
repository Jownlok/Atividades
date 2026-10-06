const display = document.getElementById('display');

for (let i = 0; i <= 9; i++) {
    document.getElementById(`b${i}`).addEventListener('click', () => {
        display.value += i;
    });
}

document.getElementById('soma').addEventListener('click', () => display.value += '+');
document.getElementById('subtracao').addEventListener('click', () => display.value += '-');
document.getElementById('divisao').addEventListener('click', () => display.value += '/');
document.getElementById('multiplicacao').addEventListener('click', () => display.value += '*');

document.getElementById('del').addEventListener('click', () => {
    display.value = '';
});

document.getElementById('igual').addEventListener('click', () => {
    try {
        display.value = eval(display.value);
    } catch {
        display.value = 'Erro';
    }
});