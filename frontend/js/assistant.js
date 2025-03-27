document.getElementById("askBtn").addEventListener("click", function() {
    let question = document.getElementById("question").value;
    
    fetch("/assistant/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: question })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("response").innerText = data.answer;
    });
});
