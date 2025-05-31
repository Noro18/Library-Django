$(document).ready(function () {
    $('.modal').on('shown.bs.modal', function () {
        const $textarea = $(this).find('textarea[id^="summernote-"]');
        if (!$textarea.hasClass('summernote-initialized')) {
        $textarea.summernote({
            height: 200,
            toolbar: [
            ['style', ['bold', 'italic', 'underline', 'clear']],
            ['font', ['strikethrough', 'superscript', 'subscript']],
            ['fontsize', ['fontsize']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['height', ['height']],
            ['insert', ['link']],
            ['view'] , ['fullscreen']
            ]
        });
        $textarea.addClass('summernote-initialized');
        }
    });
});

$(document).ready(function() {
    // Initialize Summernote for the deskrisaun field
    $('#summernote').summernote({
        height: 200, // Set the height of the editor
        toolbar: [
        ['style', ['bold', 'italic', 'underline', 'clear']],
        ['font', ['strikethrough', 'superscript', 'subscript']],
        ['fontsize', ['fontsize']],
        ['color', ['color']],
        ['para', ['ul', 'ol', 'paragraph']],
        ['height', ['height']],
        ['insert', ['link']],
        ['view'] , ['fullscreen']
        ]
    });
});