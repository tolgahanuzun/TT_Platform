$(function () {
    $('#fullscreen').on('click', function(event) {
        event.preventDefault();
        window.parent.location =  $('#fullscreen').attr('href');
    });
    $('#fullscreen').tooltip();
    /* END DEMO OF JS */
    
    $('.navbar-toggler').on('click', function(event) {
		event.preventDefault();
		$(this).closest('.navbar-minimal').toggleClass('open');
	})
});


/*Timeline Aktifleştirme*/
$(function () {
    $('.timeline-panel').click(function() {
        $('.timeline-body', this).toggle();
    });

});