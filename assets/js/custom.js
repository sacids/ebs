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

    //hide or show question 107 (2.9)
    let answer_105 = $('input:radio[name="answer[105]"]').val();
    if (answer_105 == "YES")
        $("#qn_106").show();
    else if (answer_105 == "NO")
        $("#qn_106").hide();

    //on change value    
    $('input:radio[name="answer[105]"]').change(function () {
        if ($(this).val() == 'YES') {
            $("#qn_106").show();
        } else if ($(this).val() == 'NO') {
            $("#qn_106").hide();
        }
    });




    //form-wizard
    var current_fs, next_fs, previous_fs; //fieldsets
    var opacity;

    $(".next").click(function () {
        current_fs = $(this).parent();
        next_fs = $(this).parent().next();

        //Add Class Active
        //$("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");

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
        var data = $('#msform').serialize();
        alert(data)
        return false;
    })



    /** 
 * generic form submission for sections - ajax
 * HowTo
 * 1 - for each section enscapsulate form elements in form tag
 * 2 - Set form id
 * 3 - In submit buttons add an attribute called action with URL of script that will handle the request
 * 4 - In submit buttons add class section_submit
 * 5 - Each  script in action url should return URL of next page when succesful and 0 when submission fails
 * 6 - Set method of form in form tag
 */


    $('.submit_section').on('click', function (e) {

        e.preventDefault();
        var action = $(this).attr('action');
        var form_id = $(this).closest('form');
        var method = $('#' + form_id).attr('method');
        var data = $('#' + form_id).serialize();

        //alert(form_id)
        //alert(data)
        //alert(action)
        //alert(action)

        var jqXHR = $.ajax({
            type: method,
            url: action,
            data: data,
        }).done(function (new_url) {

            // return 0 on failure and url of next page on success    
            if (new_url) {
                // success move (redirect) to next page
                window.location.href = 'http://' + new_url;

            } else {
                console.log('failed to submit form ' + form_id);
                // display some error message in div
            }
        }).fail(function (jqXHR, textStatus, errorThrown) {
            console.log(textStatus);
        }).always(function () {

        });


    });
});