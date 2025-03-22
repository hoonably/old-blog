// Description: Add a copy button to code blocks.

document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("pre").forEach(block => {
    const button = document.createElement("button");
    button.className = "copy-button";
    button.textContent = "Copy";

    button.addEventListener("click", () => {
      const code = block.querySelector("code").innerText;
      navigator.clipboard.writeText(code).then(() => {
        button.textContent = "Copied!";
        setTimeout(() => {
          button.textContent = "Copy";
        }, 2000);
      }).catch(err => {
        console.error("Failed to copy text: ", err);
      });
    });

    block.appendChild(button);
  });
});
