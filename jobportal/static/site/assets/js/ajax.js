$(document).ready(function() {
    $('.notification-item').on('click', function() {
        var notificationId = $(this).data('id');
        var $this = $(this);

        $.ajax({
            url: "{% url 'mark_as_read' %}",
            type: "POST",
            data: {
                'notification_id': notificationId,
                'csrfmiddlewaretoken': $('meta[name="csrf-token"]').attr('content')
            },
            success: function(response) {
                if (response.status === 'success') {
                    $this.remove(); // Remove the notification item from the dropdown
                } else {
                    alert('Error: ' + response.message);
                }
            },
            error: function(xhr, status, error) {
                alert('An error occurred: ' + error);
            }
        });
    });
});