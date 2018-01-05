$('.panel-body').toggle();

$('.panel-heading').on('click', function() {
    var body = $(this)
        .closest('.panel')
        .children('.panel-body');
    $(body).toggle();
});
