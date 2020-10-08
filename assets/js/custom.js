//jquery
$(document).ready(function () {
    //show council
    $('#id_council').on('change', function () {
        council = $(this).val();
        base_url = window.location.origin;

        //ajax get
        $.ajax({
            url: base_url + "/get_countries/?council_id=" + council,
            type: "get",

            success: function (data) {
                $('#id_country').html(data);
            }
        });
    });


});