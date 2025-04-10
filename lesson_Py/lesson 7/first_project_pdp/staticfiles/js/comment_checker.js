document.querySelector(".add_comment > h3").addEventListener('click', () => {
    document.querySelector(".add_comment").classList.toggle('active_comment_block');
});

function limitInput(subbtn, textarea, letterIndicator, wordsIndicator) {
    let text = textarea.value;
    subbtn.disabled = text.length === 0;
    let lastWord = text.split(' ').pop();
    let maxLength = 25;
    let remaining = maxLength - lastWord.length;
    if (lastWord.length > maxLength) {
        textarea.value = text.substring(0, text.length - 1);
        remaining = 0;
    }
    if (lastWord.length < 10) {
        letterIndicator.style.color = '#10B981';
    } else if (lastWord.length < 20) {
        letterIndicator.style.color = '#F59E0B';
    } else {
        letterIndicator.style.color = '#EF4444';
    }
    letterIndicator.innerText = `max lettr: 25 / ${lastWord.length}`;
    if (text.length < 100) {
        wordsIndicator.style.color = '#10B981';
    } else if (text.length < 200) {
        wordsIndicator.style.color = '#F59E0B';
    } else {
        wordsIndicator.style.color = '#EF4444';
    }
    wordsIndicator.innerHTML = `max length: 250 / ${text.length}`;
    if (text.length >= 250) {
        wordsIndicator.innerHTML += ' (You have reached the maximum length limit!)';
    }
}