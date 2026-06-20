// ==========================
// DOM READY
// ==========================

document.addEventListener("DOMContentLoaded", () => {

    // ==========================
    // MOBILE MENU TOGGLE
    // ==========================

    const menuBtn = document.querySelector(".menu-btn");
    const navLinks = document.querySelector(".nav-links");

    if (menuBtn && navLinks) {
        menuBtn.addEventListener("click", () => {
            navLinks.classList.toggle("active");
        });

        // Click outside — menu close ആകും
        document.addEventListener("click", (e) => {
            if (!menuBtn.contains(e.target) && !navLinks.contains(e.target)) {
                navLinks.classList.remove("active");
            }
        });
    }

    // ==========================
    // SCROLL REVEAL
    // ==========================

    const revealElements = document.querySelectorAll(
        ".service-card, .why-card, .industry-card, .process-step, .testimonial-card, .mission-card, .contact-card"
    );

    revealElements.forEach(el => {
        el.style.opacity = "0";
        el.style.transform = "translateY(40px)";
        el.style.transition = "all 0.8s ease";
    });

    function revealOnScroll() {
        revealElements.forEach(el => {
            const top = el.getBoundingClientRect().top;
            if (top < window.innerHeight - 100) {
                el.style.opacity = "1";
                el.style.transform = "translateY(0)";
            }
        });
    }

    window.addEventListener("scroll", revealOnScroll);
    revealOnScroll(); // page load-ൽ visible items ഉടൻ show ആകും

});

// ==========================
// STICKY NAVBAR
// ==========================

window.addEventListener("scroll", () => {

    const navbar = document.querySelector(".navbar");
    if (!navbar) return;

    if (window.scrollY > 100) {
        navbar.style.padding = "12px 8%";
        navbar.style.boxShadow = "0 5px 20px rgba(0,0,0,0.1)";
    } else {
        navbar.style.padding = "18px 8%";
        navbar.style.boxShadow = "0 2px 20px rgba(0,0,0,.06)";
    }

});

// ==========================
// COUNTER ANIMATION
// ==========================

const counters = document.querySelectorAll(".stat-box h2");
let counterStarted = false;

function startCounter() {
    counters.forEach(counter => {

        const targetText = counter.innerText.trim();
        const target = parseInt(targetText.replace(/\D/g, ""));
        const suffix = targetText.replace(/[0-9]/g, ""); // "+" or "%" etc.

        let count = 0;
        const increment = Math.ceil(target / 100);

        function updateCount() {
            if (count < target) {
                count += increment;
                if (count > target) count = target;
                counter.innerText = count + suffix;
                setTimeout(updateCount, 20);
            } else {
                counter.innerText = targetText;
            }
        }

        updateCount();
    });
}

window.addEventListener("scroll", () => {

    const stats = document.querySelector(".stats");
    if (!stats || counterStarted) return;

    const sectionTop = stats.getBoundingClientRect().top;

    if (sectionTop < window.innerHeight - 100) {
        startCounter();
        counterStarted = true;
    }

});

// ==========================

// PAGE LOADED
// ==========================

window.addEventListener("load", () => {
    document.body.classList.add("loaded");
    console.log(
        "%cCandid Ledger Website Loaded Successfully",
        "color:#38BDF8;font-size:16px;font-weight:bold;"
    );
});


// ==========================
// WHATSAPP CHAT TOGGLE
// ==========================

const whatsappBtn = document.querySelector('.whatsapp-btn');
const chatBox = document.querySelector('.whatsapp-chat');

if (whatsappBtn && chatBox) {

    chatBox.style.display = "none";

    whatsappBtn.addEventListener("click", function(e) {

        e.preventDefault();

        if (chatBox.style.display === "none") {
            chatBox.style.display = "block";
        } else {
            chatBox.style.display = "none";
        }

    });

}

const callToggle = document.getElementById("callToggle");
const callOptions = document.getElementById("callOptions");

if (callToggle && callOptions) {

    callToggle.addEventListener("click", function(e) {
        e.preventDefault();

        callOptions.style.display =
            callOptions.style.display === "flex"
                ? "none"
                : "flex";
    });

    document.addEventListener("click", function(e) {

        if (
            !callToggle.contains(e.target) &&
            !callOptions.contains(e.target)
        ) {
            callOptions.style.display = "none";
        }

    });
}







