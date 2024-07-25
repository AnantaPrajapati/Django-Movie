document.addEventListener("DOMContentLoaded", function () {
    var messageContainer = document.getElementById("message-container");
    if (messageContainer) {
      setTimeout(function () {
        messageContainer.style.display = "none";
      }, 5000);
    }
  });