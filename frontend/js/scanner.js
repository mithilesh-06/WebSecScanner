document.getElementById("scanBtn").addEventListener("click", function() {
    let url = document.getElementById("urlInput").value;
    
    fetch("/scanner/scan", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url: url })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = data.ai_report;
    });
});
