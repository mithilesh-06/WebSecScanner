document.getElementById("testBtn").addEventListener("click", function() {
    let url = document.getElementById("urlInput").value;
    let payload = document.getElementById("payloadInput").value;

    fetch("/ssrf/test", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url: url, payload: payload })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = JSON.stringify(data, null, 2);
    })
    .catch(error => {
        document.getElementById("result").innerText = "Error: " + error;
    });
});
