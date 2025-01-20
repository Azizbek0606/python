function incrementQuantity(maxValue, update_btn , elem) {
    if (parseInt(elem.value) == maxValue) {
        createMessage("You have reached the maximum quantity", "error");
    } else {
        elem.value = parseInt(elem.value) + 1;
        update_btn.style.display = "block";
    }
}

function decrementQuantity(update_btn , elem) {
    if (parseInt(elem.value) == 1) {
        createMessage("You have reached the minimum quantity!", "error");
    } else {
        elem.value = parseInt(elem.value) - 1;
        update_btn.style.display = "block";
    }
}

function createMessage(messageContent, messageStatus) {
    let messageDiv = document.createElement('div');
    messageDiv.classList.add('message');
    messageDiv.setAttribute('message_status', messageStatus);

    let messageText = document.createElement('p');
    messageText.innerHTML = messageContent;

    let closeButton = document.createElement('i');
    closeButton.classList.add('fa-solid', 'fa-x', 'x-mark');
    closeButton.addEventListener('click', () => close_message(messageDiv));

    messageDiv.appendChild(messageText);
    messageDiv.appendChild(closeButton);

    document.body.appendChild(messageDiv);

    setTimeout(() => close_message(messageDiv), 3000);
}
function close_message(messageDiv) {
    messageDiv.style.transform = 'translateY(-1000px)';
}


document.addEventListener('DOMContentLoaded', () => {
    let pending_count = 0;
    let pending_total_producs = 0;
    let processing_count = 0;
    let processing_total_product = 0;
    let product_prices = document.querySelectorAll(".product_total_price ");
    let quantity = document.querySelectorAll("#quantity_inp");
    for (let i = 0; i < product_prices.length; i++) {
        if(product_prices[i].getAttribute("status") == "pending"){
            pending_count += Number(product_prices[i].textContent.replace(/\s+/g, ''));
        } else if (product_prices[i].getAttribute("status") == "processing" ){
            processing_count += Number(product_prices[i].textContent.replace(/\s+/g, ''));
        }
    }
    for (let i = 0; i < quantity.length; i++) {
        if (quantity[i].getAttribute("status") == "processing"){
            processing_total_product += Number(quantity[i].value);
        }else if(quantity[i].getAttribute("status") == "pending"){
            pending_total_producs += Number(quantity[i].value);
        }
    }

    document.querySelector(".pending_count").textContent = pending_count.toFixed(2);
    document.querySelector(".pending_total_product").textContent = pending_total_producs.toFixed(0);
    document.querySelector(".processing_count").textContent = processing_count.toFixed(2);
    document.querySelector(".processing_total_product").textContent = processing_total_product.toFixed(0);
 
});

