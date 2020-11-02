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

    //delete
    $("a.delete").click(function (e) {
        var confirmDelete = confirm("Are you sure you want to delete?");

        if (confirmDelete) {
            return true;
        } else {
            e.preventDefault();
        }
    });

    //toggle modal
    $(".qn-modal").on('click', function (e) {
        var qn_id = $(this).attr('question-id');
        var base_url = window.location.origin;

        $.ajax({
            url: base_url + "/show_question/?question_id=" + qn_id,
            type: "get",
            dataType: "json",

            //success
            success: function (data) {
                $('#qnModalBody').text(data.placeholder)
            }
        });

        // show modal
        $("#qnModal").modal('show');
    });

    //form-wizard
    var current_fs, next_fs, previous_fs; //fieldsets
    var opacity;

    $(".next").click(function () {

        current_fs = $(this).parent();
        next_fs = $(this).parent().next();

        //Add Class Active
        $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");

        //show the next fieldset
        next_fs.show();
        //hide the current fieldset with style
        current_fs.animate({ opacity: 0 }, {
            step: function (now) {
                // for making fielset appear animation
                opacity = 1 - now;

                current_fs.css({
                    'display': 'none',
                    'position': 'relative'
                });
                next_fs.css({ 'opacity': opacity });
            },
            duration: 600
        });
    });

    $(".previous").click(function () {
        current_fs = $(this).parent();
        previous_fs = $(this).parent().prev();

        //Remove class active
        $("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");

        //show the previous fieldset
        previous_fs.show();

        //hide the current fieldset with style
        current_fs.animate({ opacity: 0 }, {
            step: function (now) {
                // for making fielset appear animation
                opacity = 1 - now;

                current_fs.css({
                    'display': 'none',
                    'position': 'relative'
                });
                previous_fs.css({ 'opacity': opacity });
            },
            duration: 600
        });
    });

    //submit
    $(".submit").click(function () {
        return false;
    })
});