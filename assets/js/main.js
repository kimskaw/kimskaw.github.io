/* kimskaw.github.io - interactions */
(function () {
  "use strict";

  var root = document.documentElement;

  /* ---- theme toggle (system preference, overridable) ---- */
  var toggle = document.getElementById("theme-toggle");

  function syncToggle() {
    if (!toggle) return;
    var light = root.getAttribute("data-theme") === "light";
    toggle.setAttribute("aria-pressed", light ? "true" : "false");
    toggle.setAttribute("aria-label", light ? "Switch to dark theme" : "Switch to light theme");
  }

  if (toggle) {
    syncToggle();
    toggle.addEventListener("click", function () {
      var light = root.getAttribute("data-theme") === "light";
      if (light) {
        root.removeAttribute("data-theme");
        localStorage.setItem("theme", "dark");
      } else {
        root.setAttribute("data-theme", "light");
        localStorage.setItem("theme", "light");
      }
      syncToggle();
    });
  }

  /* ---- mobile nav ---- */
  var burger = document.getElementById("nav-burger");
  var links = document.getElementById("nav-links");

  function closeNav() {
    if (!links || !burger) return;
    links.classList.remove("open");
    burger.setAttribute("aria-expanded", "false");
    burger.setAttribute("aria-label", "Open menu");
  }

  if (burger && links) {
    burger.addEventListener("click", function (e) {
      e.stopPropagation();
      var open = links.classList.toggle("open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
      burger.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    });

    links.addEventListener("click", function (e) {
      if (e.target.closest("a")) closeNav();
    });

    document.addEventListener("click", function (e) {
      if (!links.classList.contains("open")) return;
      if (!links.contains(e.target) && !burger.contains(e.target)) closeNav();
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && links.classList.contains("open")) {
        closeNav();
        burger.focus();
      }
    });
  }

  /* ---- scroll reveal ---- */
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var revealEls = document.querySelectorAll(".reveal");

  if (reduce || !("IntersectionObserver" in window)) {
    revealEls.forEach(function (el) { el.classList.add("visible"); });
  } else if (revealEls.length) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("visible");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.08, rootMargin: "0px 0px -40px 0px" }
    );
    revealEls.forEach(function (el) { io.observe(el); });
  }

  /* ---- active nav link on scroll (index only) ---- */
  var sections = document.querySelectorAll("main section[id]");
  var navAnchors = document.querySelectorAll('.nav-links a[href^="#"]');
  if (sections.length && navAnchors.length && "IntersectionObserver" in window) {
    var current = null;
    var spy = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) current = entry.target.id;
        });
        navAnchors.forEach(function (a) {
          a.classList.toggle("active", a.getAttribute("href") === "#" + current);
        });
      },
      { rootMargin: "-45% 0px -50% 0px" }
    );
    sections.forEach(function (s) { spy.observe(s); });
  }

  /* ---- footer year ---- */
  var year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();
})();
