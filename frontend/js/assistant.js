document.getElementById("ask-ai-btn").addEventListener("click", async () => {
    const question = document.getElementById("question-input").value;
    const responseBox = document.getElementById("response-box");

    try {
        const response = await fetch("http://127.0.0.1:5000/assistant/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();  // ✅ Ensure parsing JSON
        responseBox.innerText = data.answer;
    } catch (error) {
        responseBox.innerText = `Error: ${error.message}`;
    }
});
