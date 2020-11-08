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


    $('.submit_section').on('click',function(e){

        e.preventDefault();
        var action      = $(this).attr('action');
        var form_id     = $(this).closest('form');
        var method      = $('#'+form_id).attr('method');
        var data        = $('#'+form_id).serialize();

        //alert(form_id)
        //alert(data)
        //alert(action)
        //alert(action)

        var jqXHR = $.ajax({
            type:method,
            url:action,
            data: data,
        }).done(function (new_url){

            // return 0 on failure and url of next page on success    
            if(new_url){
                // success move (redirect) to next page
                window.location.href    = 'http://'+new_url;

            }else{
                console.log('failed to submit form '+form_id);
                // display some error message in div
            }
        }).fail(function(jqXHR, textStatus, errorThrown){
            console.log(textStatus);
        }).always(function() {

        });


    });


});