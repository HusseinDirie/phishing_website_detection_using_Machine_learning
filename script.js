// Dark Mode Toggle
function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
}

// GSAP Animations
gsap.from(".card", { duration: 1, opacity: 0, y: -50, ease: "power2.out" });
gsap.from(".btn-warning, .btn-dark, .btn-primary", { duration: 1, scale: 0.5, ease: "elastic.out(1, 0.5)" });

// Speech Recognition for URL Input
function startSpeechRecognition() {
    let recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = "en-US";
    recognition.start();

    recognition.onresult = function (event) {
        document.getElementById("urlInput").value = event.results[0][0].transcript;
    };
}
