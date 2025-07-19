document.addEventListener('DOMContentLoaded', function() {
    let prevSlider = document.getElementById('prev-slider');
    let nextSlider = document.getElementById('next-slider');
    let courses = document.getElementsByClassName('course');
    let currentIndex = 0;
    const coursesPerPage = 3;

    function updateVisibility() {
        for (let i = 0; i < courses.length; i++) {
            courses[i].style.display = 'none';
        }
        
        for (let i = currentIndex; i < currentIndex + coursesPerPage && i < courses.length; i++) {
            courses[i].style.display = 'block';
        }
    }

    updateVisibility();

    nextSlider.onclick = function() {
        currentIndex += 1;
        if (currentIndex >= courses.length) {
            currentIndex = 0;
        }
        updateVisibility();
    };

    prevSlider.onclick = function() {
        currentIndex -= 1;
        if (currentIndex < 0) {
            currentIndex = Math.max(0, courses.length - 1);
        }
        updateVisibility();
    };
});