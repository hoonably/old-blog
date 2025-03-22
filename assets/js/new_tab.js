// assets/js/external-links.js

document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("a").forEach(link => {
      if (!link.classList.contains('no-target-blank')) {
        link.setAttribute('target', '_blank');
      }
    });
  });
  