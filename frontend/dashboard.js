$(document).ready(function() {
    // Fetching dashboard data from the backend
    $.ajax({
        url: '/dashboard',
        type: 'GET',
        success: function(response) {
            // Populate the dashboard with the response data
            populateDashboard(response);
        },
        error: function(error) {
            console.log(error);
        }
    });

    function populateDashboard(data) {
        // Populate tasks
        $('#tasks').html(data.tasks);

        // Populate upcoming posts
        $('#upcomingPosts').html(data.upcomingPosts);

        // Populate content performance metrics
        $('#contentPerformance').html(data.contentPerformance);
    }

    // Event listener for task completion
    $('.task-complete').click(function() {
        var taskId = $(this).data('id');

        // Send task completion to the backend
        $.ajax({
            url: '/tasks/complete',
            type: 'POST',
            data: { id: taskId },
            success: function(response) {
                // Update the task in the dashboard
                $(`#task-${taskId}`).remove();
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});