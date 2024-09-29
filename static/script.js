document.addEventListener("DOMContentLoaded", function() {
    // Manejar el evento de navegación hacia atrás
    window.addEventListener('pageshow', function(event) {
        if (event.persisted) {
            window.location.reload();
        }
    });

    document.querySelectorAll('a').forEach(function(link) {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            let targetUrl = this.getAttribute('href');
            
            if (targetUrl) {
                document.body.classList.add('fade-exit-active');
                setTimeout(function() {
                    window.location.href = targetUrl;
                }, 500); // Debe coincidir con la duración de la transición en CSS
            }
        });
    });

    document.body.classList.add('fade-enter-active');
});
