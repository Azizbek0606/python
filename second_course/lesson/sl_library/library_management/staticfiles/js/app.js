let cards = document.querySelectorAll('.book-card');
let searchInput = document.getElementById('search-input');
searchInput.addEventListener('input', function(e) {
    let searchWord = e.target.value.toLowerCase();
    cards.forEach(function(card) {
        let title = card.querySelector('#card-title').textContent.toLowerCase();
        let author = card.querySelector('#card-author').textContent.toLowerCase();
        if (title.includes(searchWord) || author.includes(searchWord)) {
            card.style.cssText = `visibility: visible;`;
        } else {
            card.style.cssText = `visibility: hidden;`;
        }
    })
});
let comfirmLogOut = document.getElementById('comfirm-logout');
let logoutUrl = comfirmLogOut.getAttribute('data-url');
comfirmLogOut.addEventListener('click', function(e) {
    let confirm = window.confirm('Are you sure you want to log out?');
    if(confirm) {
        window.location.href = logoutUrl;
    }
});