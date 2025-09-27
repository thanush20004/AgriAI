// Add interactivity for like and comment buttons

document.addEventListener('DOMContentLoaded', function() {
    // Like button AJAX
    document.querySelectorAll('.like-form').forEach(function(form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            fetch(form.action, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': form.querySelector('[name=csrfmiddlewaretoken]').value
                }
            }).then(response => {
                if (response.ok) {
                    window.location.reload();
                }
            });
        });
    });

    // Comment form AJAX
    document.querySelectorAll('.comment-form').forEach(function(form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(form);
            fetch(form.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': form.querySelector('[name=csrfmiddlewaretoken]').value
                }
            }).then(response => {
                if (response.ok) {
                    window.location.reload();
                }
            });
        });
    });
});
