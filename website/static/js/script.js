document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("user-input").addEventListener("keydown", function(e) {
        if (e.key === "Enter" && e.ctrlKey) {
            document.getElementById("user-input").submit();
            document.getElementById("submit-btn").disabled = true;
            try {
                document.getElementById("loadingSpinner").style.display = "block"; // Show the spinner
            } catch (error) {
                console.error("Caught an error:", error.message)
            }
            try {
                document.getElementById("gpt-output").innerHTML = "";
            } catch (error) {
                console.error("Caught an error:", error.message)
            }
          }
    });
    document.getElementById("user-input").addEventListener("submit", function () {
        document.getElementById("submit-btn").disabled = true;
        try {
            document.getElementById("loadingSpinner").style.display = "block"; // Show the spinner
        } catch (error) {
            console.error("Caught an error:", error.message)
        }
        try {
            document.getElementById("gpt-output").innerHTML = "";
        } catch (error) {
            console.error("Caught an error:", error.message)
        }
    });
  });