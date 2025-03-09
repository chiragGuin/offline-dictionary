document.getElementById("searchBtn").addEventListener("click", function() {
  let word = document.getElementById("searchInput").value;
  
  fetch(`http://127.0.0.1:5000/search?word=${word}`)
    .then(response => response.json())
    .then(data => {
      document.getElementById("result").innerHTML = data.meaning ?
        `<strong>${word}:</strong> ${data.meaning}` :
        "Word not found.";
    })
    .catch(error => console.error("Error:", error));
});
