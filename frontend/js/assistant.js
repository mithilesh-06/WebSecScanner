document.getElementById("ask-button").addEventListener("click", async () => {
    const inputField = document.getElementById("question-input");
    const responseField = document.getElementById("response");

    try {
        let response = await fetch("http://127.0.0.1:5000/assistant/ask", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question: inputField.value }),
        });

        let contentType = response.headers.get("content-type");
        if (!contentType || !contentType.includes("application/json")) {
            throw new Error("Invalid response from server. Check API.");
        }

        let data = await response.json();
        responseField.innerText = data.answer;
    } catch (error) {
        responseField.innerText = `Error: ${error.message}`;
    }
});
