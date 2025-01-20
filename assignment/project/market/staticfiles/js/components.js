function confirm_modal_open(target_element, text_pointer, context, btn, url) {
    target_element.style.transform = 'translateY(0px)';
    text_pointer.textContent = context;
    if (window.location.pathname == "/orders/"){
        btn.href = `/orders/change-status/${document.querySelector('#order_id').textContent.replace(/\s+/g, ' ').trim() }`
    }else{
        btn.href = url;
    }
}
function confirm_modal_close(target_element) {
    target_element.style.transform = 'translateY(-1500px)'
}

function close_message(message) {
    message.parentNode.style.transform = 'translateY(-1000px)'
}
