// script.js
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.delete-movie').forEach(button => {
      button.addEventListener('click', (event) => {
        if (!confirm('Are you sure you want to delete this movie?')) {
          event.preventDefault();
        }
      });
    });
  });
  