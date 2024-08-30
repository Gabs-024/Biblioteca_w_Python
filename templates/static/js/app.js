let items = document.querySelectorAll('.slider .item');
let next = document.getElementById('next');
let prev = document.getElementById('prev');

let active = 3;
function loadShow(){
    let stt = 0;
    items[active].style.transform = `none`;
    items[active].style.zIndex = 1;
    items[active].style.filter = 'none';
    items[active].style.opacity = 1;
    for(var i = active + 1; i < items.length; i++){
        stt++;
        items[i].style.transform = `translateX(${120*stt}px) scale(${1 - 0.2*stt}) perspective(16px) rotateY(-1deg)`;
        items[i].style.zIndex = -stt;
        items[i].style.filter = 'blur(5px)';
        items[i].style.opacity = stt > 2 ? 0 : 0.6;
    }
    stt = 0;
    for(var i = active - 1; i >= 0; i--){
        stt++;
        items[i].style.transform = `translateX(${-120*stt}px) scale(${1 - 0.2*stt}) perspective(16px) rotateY(1deg)`;
        items[i].style.zIndex = -stt;
        items[i].style.filter = 'blur(5px)';
        items[i].style.opacity = stt > 2 ? 0 : 0.6;
    }
}
loadShow();
next.onclick = function(){
    active = active + 1 < items.length ? active + 1 : active;
    loadShow();
}
prev.onclick = function(){
    active = active - 1 >= 0 ? active - 1 : active;
    loadShow();
}

// Aguarda 100 ms para garantir que a mensagem esteja renderizada
setTimeout(function() {
    // Seleciona todas as mensagens de alerta
    const allMessages = document.querySelectorAll('.messages-container .alert');

    // Itera sobre todas as mensagens encontradas
    allMessages.forEach(function(message) {
        // Se a mensagem for de sucesso, aguarda 10 segundos antes de redirecionar
        if (message.classList.contains('alert-success')) {
            setTimeout(function() {
                // Aqui você pode redirecionar, se necessário
                // window.location.href = "{% url 'alguma:pagina' %}";
            }, 3000);  // Tempo para exibir a mensagem antes de redirecionar (10 segundos)
        } else {
            // Aplica o efeito de ocultar mensagem para outras classes de alerta
            setTimeout(function() {
                message.style.transition = "opacity 0.5s ease";
                message.style.opacity = "0";
                setTimeout(() => message.style.display = "none", 500);
            }, 3000);  // Tempo para ocultar mensagens de erro ou aviso (5 segundos)
        }
    });
}, 100);  // Um pequeno atraso para garantir que o DOM esteja completamente carregado


 