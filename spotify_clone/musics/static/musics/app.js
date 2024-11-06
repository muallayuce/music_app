document.getElementById("logout-button").addEventListener("click", function () {
    window.location.href = this.getAttribute("data-url");
  });
  
 document.getElementById("my-profile").addEventListener("click", function () {
    window.location.href = this.getAttribute("data-url");
  });
  
document.getElementById("my-music").addEventListener("click", function () {
    window.location.href = this.getAttribute("data-url");
  });
  

  document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("back-to-home").addEventListener("click", function () {
      window.location.href = this.getAttribute("data-url");
    });
  });
  