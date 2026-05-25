const sessionId =
    localStorage.getItem("sessionId")
    || crypto.randomUUID();

localStorage.setItem(
    "sessionId",
    sessionId
);

async function sendMessage() {

    const messageInput =
        document.getElementById("message");

    const chatBox =
        document.getElementById("chat-box");

    const message =
        messageInput.value.trim();

    if (!message) return;

    chatBox.innerHTML += `
        <div class="user-message">
            <b>You:</b> ${message}
        </div>
    `;

    messageInput.value = "";

    const response = await fetch(
        "/api/chat",
        {
            method: "POST",

            headers: {
                "Content-Type":
                "application/json"
            },

            body: JSON.stringify({
                sessionId,
                message
            })
        }
    );

    const data =
        await response.json();

    chatBox.innerHTML += `
        <div class="bot-message">
            <b>Bot:</b> ${data.reply}
        </div>
    `;

    chatBox.scrollTop =
        chatBox.scrollHeight;
}