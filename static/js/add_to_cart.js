document.addEventListener('DOMContentLoaded', function() {
    // Handle all add to cart forms
    const forms = document.querySelectorAll('.add-to-cart-form');

    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();

            fetch(this.action, {
                method: 'POST',
                body: new FormData(this),
                headers: {
                    'X-CSRFToken': this.querySelector('[name=csrfmiddlewaretoken]').value,
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(response => {
                if (response.ok) {
                    // Show success modal
                    const modal = new bootstrap.Modal(document.getElementById('addedToCartModal'));
                    modal.show();
                } else {
                    console.error('Error adding to cart');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });
});