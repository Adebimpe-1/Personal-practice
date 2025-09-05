function updateLocalDateTime() {
    const dateTimeElement = document.getElementById('localDateTime');
    const now = new Date();
    // Format date and time nicely - e.g., "Thursday, September 5, 2025, 2:34 PM"
    const options = {
        weekday: 'long', year: 'numeric', month: 'long',
        day: 'numeric', hour: 'numeric', minute: 'numeric', second: 'numeric',
        hour12: true
    };
    const localDateTimeString = now.toLocaleString(undefined, options);
    dateTimeElement.textContent = ` ${localDateTimeString}`;
}

// Call the function on page load
document.addEventListener('DOMContentLoaded', () => {
    updateLocalDateTime();
});

document.addEventListener('DOMContentLoaded', () => {
    const bookingModal = document.getElementById('bookingModal');
    const bookingTourName = document.getElementById('bookingTourName');
    const closeModal = document.getElementById('closeModal');
    const bookingForm = document.getElementById('bookingForm');
    const contactForm = document.getElementById('contactForm');

    // Open booking modal when clicking a "Book Now" button
    document.querySelectorAll('.tour-card button').forEach(button => {
        button.addEventListener('click', () => {
            bookingTourName.textContent = 'Book: ' + button.dataset.tour;
            bookingModal.classList.remove('hidden');
        });
    });
// Close booking modal
    closeModal.addEventListener('click', () => {
        bookingModal.classList.add('hidden');
    });

    // Booking form submission
    bookingForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const name = document.getElementById('bookerName').value.trim();
        const email = document.getElementById('bookerEmail').value.trim();

        if (!name || !email) {
            alert('Please fill out all booking fields.');
            return;
        }
        alert(`Thank you, ${name}! Your booking has been received.`);
        bookingModal.classList.add('hidden');
        bookingForm.reset();
    });

    // Contact form submission
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const message = document.getElementById('message').value.trim();

        if (!name || !email || !message) {
            alert('Please fill out all fields.');
            return;
        }
        alert(`Thank you, ${name}! Your message has been sent.`);
        contactForm.reset();
    });
});
