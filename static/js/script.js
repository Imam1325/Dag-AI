// Анимация при прокрутке
document.addEventListener("DOMContentLoaded", function () {
    const sections = document.querySelectorAll("section");

    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("visible");
                }
            });
        },
        {
            threshold: 0.1, // Анимация сработает, когда 10% элемента будет видно
        }
    );

    sections.forEach((section) => {
        observer.observe(section);
    });
});

// Добавляем класс для анимации
document.querySelectorAll("section").forEach((section) => {
    section.classList.add("fade-in");
});
