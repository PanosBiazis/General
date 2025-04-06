// script.js
function sendMessage() {
    const input = document.getElementById('userInput').value;
    if (input.trim() === '') return;
    
    document.getElementById('userInput').value = '';

    const userMessage = document.createElement('div');
    userMessage.className = 'user-message';
    userMessage.textContent = 'You: ' + input;
    document.getElementById('messages').appendChild(userMessage);

    fetch('api_response.php?input=' + encodeURIComponent(input))
        .then(response => response.json())
        .then(data => {
            const botMessage = document.createElement('div');
            botMessage.className = 'bot-response';
            botMessage.textContent = 'Chatbot: ' + data.response;
            document.getElementById('messages').appendChild(botMessage);
        });
}
