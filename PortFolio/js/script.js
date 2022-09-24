///////////////////////////////////////////////////////////
// MOBILE NAVIGATION
const btnNavEl = document.querySelector(".btn-mobile-nav");
const headerEl = document.querySelector(".header");

btnNavEl.addEventListener("click", function () {
  headerEl.classList.toggle("nav-open");
});

///////////////////////////////////////////////////////////
// Smooth scrolling animation
const allLink = document.querySelectorAll("a:link");
allLink.forEach(function (link) {
  link.addEventListener("click", function (e) {
    const href = link.getAttribute("href");
    console.log(href);

    if (href === "#") {
      e.preventDefault();
      window.scrollTo({
        top: 0,
        behavior: "smooth",
      });
    }

    if (href !== "#" && href.startsWith("#")) {
      e.preventDefault();
      const section = document.querySelector(href);
      section.scrollIntoView({ behavior: "smooth" });
    }

    if (link.classList.contains("main-nav-link")) {
      headerEl.classList.remove("nav-open");
    }
  });
});

///////////////////////////////////////////////////////////
// Fixed-nav

const sectionHeroEL = document.querySelector(".section-hero");

const obs = new IntersectionObserver(
  function (entries) {
    const ent = entries[0];
    if (!ent.isIntersecting) {
      // console.log(ent);
      document.querySelector(".fixed-nav").classList.remove("display-none");
    }
    if (ent.isIntersecting) {
      document.querySelector(".fixed-nav").classList.add("display-none");
    }
  },
  {
    // In the viewport
    root: null,
    threshold: 0,
    rootMargin: "-300px",
  }
);
obs.observe(sectionHeroEL);

///////////////////////////////////////////////////////////
// CONTACT-ANIMATION
// const contact = document.querySelector(".btn--form");
// contact.addEventListener("click", function (e) {
//   e.preventDefault();
//   if (
//     String(document.getElementById("phone").value).trim().length != 0 &&
//     String(document.getElementById("email").value).trim().length != 0 &&
//     String(document.getElementById("full-name").value).trim().length != 0
//   ) {
//     contact.classList.add("display-none");
//     document
//       .querySelector(".contact-animation")
//       .classList.remove("display-none");
//   }
//   document.getElementById("phone").value = "";
//   document.getElementById("email").value = "";
//   document.getElementById("full-name").value = "";
// });

///////////////////////////////////////////////////////////
// REVEAL SECTIONS
// const allSections = document.querySelectorAll(".section");

// const revealSection = function (entries, observer) {
//   const [entry] = entries;
//   console.log(entry);

//   if (!entry.isIntersecting) return;

//   entry.target.classList.remove("section--hidden");
// };

// const sectionObserver = new IntersectionObserver(revealSection, {
//   root: null,
//   threshold: 0.15,
// });

// allSections.forEach(function (section) {
//   sectionObserver.observe(section);
//   section.classList.add("section--hidden");
// });

///////////////////////////////////////////////////////////
// Fixing flexbox gap property missing in some Safari versions
function checkFlexGap() {
  var flex = document.createElement("div");
  flex.style.display = "flex";
  flex.style.flexDirection = "column";
  flex.style.rowGap = "1px";

  flex.appendChild(document.createElement("div"));
  flex.appendChild(document.createElement("div"));

  document.body.appendChild(flex);
  var isSupported = flex.scrollHeight === 1;
  flex.parentNode.removeChild(flex);
  // console.log(isSupported);

  if (!isSupported) document.body.classList.add("no-flexbox-gap");
}
checkFlexGap();

// Anim Morph

var morphing = anime({
  targets: ".morph",
  points: [
    //Debut
    {
      value:
        "460.677372 125.296036 108.040017 24.8652344 112.454079 125.296036",
    },
    //Fin
    {
      value:
        "460.677372 157.296036 112.758683 38.9677241 119.111306 145.719727",
    },
  ],
  easing: "easeInOutQuad",
  duration: 3000,
  loop: true,
});

var morphing = anime({
  targets: ".morph2",
  points: [
    //Debut
    { value: "108.040017 24.8652344 168.780251 0 460.677372 125.296036" },
    //Fin
    { value: "112.758683 38.9677241 184.146186 0 460.677372 157.296036" },
  ],
  easing: "easeInOutQuad",
  duration: 3000,
  loop: true,
});

var morphing = anime({
  targets: ".morph3",
  points: [
    //Debut
    { value: "75.3147561 38.1354167 460.677372 125.296036 0 68.5184024" },
    //Fin
    { value: "78.250435 57.8044647 460.677372 157.296036 0 100.518402" },
  ],
  easing: "easeInOutQuad",
  duration: 3000,
  loop: true,
});

// Copy to Clipboard
// Sources : https://alligator.io/js/copying-to-clipboard/

const ctcMail = document.querySelectorAll(".contact");

ctcMail.forEach((mail) => {
  mail.addEventListener("click", () => {
    const selection = window.getSelection();
    const range = document.createRange();
    range.selectNodeContents(mail);
    selection.removeAllRanges();
    selection.addRange(range);

    try {
      document.execCommand("copy");
      selection.removeAllRanges();

      mail.getElementsByClassName("mail")[0].dataset.status = "Copied!";
      mail.classList.add("success");

      setTimeout(() => {
        mail.classList.remove("success");
        mail.getElementsByClassName("mail")[0].dataset.status = "Click to Copy";
      }, 1200);
    } catch (e) {}
  });
});
