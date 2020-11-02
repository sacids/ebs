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
});