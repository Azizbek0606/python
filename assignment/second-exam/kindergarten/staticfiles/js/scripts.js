document.addEventListener('DOMContentLoaded', () => {
    const ws = new WebSocket('ws://' + window.location.host + '/ws/inventory/');
    console.log(ws, "lorem ipsum dolr sit");
    ws.onmessage = function (e) {
        const data = JSON.parse(e.data);
        const alertDiv = document.createElement('div');
        alertDiv.className = 'fixed top-4 right-4 p-4 bg-red-100 text-red-700 rounded shadow-lg';
        alertDiv.innerText = data.message;
        document.body.appendChild(alertDiv);
        setTimeout(() => alertDiv.remove(), 5000);
    };
    ws.onclose = function () {
        console.error('WebSocket ulanishi yopildi');
    };
});