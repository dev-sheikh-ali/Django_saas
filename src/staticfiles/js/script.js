$(document).ready(function() {
    // Logout Modal
    $(document).on('click', "a[href='{% url 'account_logout' %}']", function(event) {
        event.preventDefault();
        $('#logoutModal').modal('show');
    });

    $('#confirmLogoutBtn').on('click', function() {
        window.location.href = "{% url 'account_logout' %}";
    });

    // Change Password Modal
    $('#changePasswordModalTrigger').on('click', function(event) {
        event.preventDefault();
        $('#changePasswordModal').modal('show');
    });
});