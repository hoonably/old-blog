// assets/js/external-links.js

document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("a").forEach(link => {
    const href = link.getAttribute('href');

    // (1) class 예외
    const isNoTargetBlank = link.classList.contains('no-target-blank');

    // (2) 앵커 또는 내부 링크 예외
    const isAnchorLink = href && href.startsWith('#');
    const isInternalLink = href && (href.startsWith('/') || href.startsWith(window.location.origin));

    // (3) 외부 링크만 새 탭으로 열기
    if (!isNoTargetBlank && !isAnchorLink && !isInternalLink) {
      link.setAttribute('target', '_blank');
    }
  });
});
