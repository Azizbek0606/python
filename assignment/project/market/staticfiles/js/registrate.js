let icon = document.querySelectorAll('.show_password')
let pas_inp = document.querySelectorAll('#password_input')

for (let i = 0; i < icon.length; i++) {
    icon[i].addEventListener('click', function () {
        if (pas_inp[i].type === 'password') {
            pas_inp[i].type = 'text'
            icon[i].classList.remove('fa-eye')
            icon[i].classList.add('fa-eye-slash')
        } else {
            pas_inp[i].type = 'password'
            icon[i].classList.remove('fa-eye-slash')
            icon[i].classList.add('fa-eye')
        }
    })
}

function form_validator() {
    let username = document.querySelector('#username').value;
    let phoneNumber = document.querySelector('#phone_number').value;
    let role = document.querySelector('#role').value;
    let password = document.querySelector('.password').value;
    let confirmPassword = document.querySelector('.confirm_password').value;

    if (username === '' || phoneNumber === '' || role === '' || password === '' || confirmPassword === '') {
        let message = document.createElement("div");
        let messageText = document.createElement("p");
        let messageCloser = document.createElement("i");
        message.appendChild(messageText);
        message.appendChild(messageCloser);
        message.className = "message";
        messageText.textContent = "Please fill in all fields";
        messageCloser.className = 'fa-solid fa-x x-mark';
        messageCloser.setAttribute("onclick", "close_message(this)");
        document.body.appendChild(message);
        console.log(
            username ,
            phoneNumber,
            role,
            password,
            confirmPassword
        );
        
        return false;
    }

    if (password !== confirmPassword) {
        let message = document.createElement("div");
        let messageText = document.createElement("p");
        let messageCloser = document.createElement("i");
        message.appendChild(messageText);
        message.appendChild(messageCloser);
        message.className = "message";
        messageText.textContent = "Passwords do not match";
        messageCloser.className = 'fa-solid fa-x x-mark';
        messageCloser.setAttribute("onclick", "close_message(this)");
        document.body.appendChild(message);

        return false;
    }

    return true;
}