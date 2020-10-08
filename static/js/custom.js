//jquery
$(document).ready(function () {
    //show department users
    $('#council').on('change', function () {
        council = $(this).val();
        alert(council)

        base_url = window.location.origin;

        $.ajax({
            url: base_url + "/users/departments/" + department_id,
            type: "get",

            success: function (data) {
                $('#supervisor_ids').html(data);
            }
        });
    });

}