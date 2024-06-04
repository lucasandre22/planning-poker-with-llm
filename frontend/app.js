$(document).ready(function() {
    $('#chatFormTicket').on('submit', function(e) {
        e.preventDefault();
        const backendUrl = window.location.origin;
        const ticket = $('#chatInput').val();
        console.log("ticket");
        
        //Get response from the backend API
        $.ajax({
            url: backendUrl + '/v1/get-output',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ ticket: message }),
            crossDomain: true,
            success: function(response) {
                const aiMessage = response.result;
                $('#chatBody').children().last().remove();
                $('#chatBody').append(`
                    <div class="message ai">
                        <div class="text">${aiMessage}</div>
                    </div>
                `);
                $('#chatBody').scrollTop($('#chatBody')[0].scrollHeight);
            },
            error: function() {
                $('#chatBody').children().last().remove();
                $('#chatBody').append(`
                    <div class="message ai">
                        <div class="text">Sorry, there was an error processing your request.</div>
                    </div>
                `);
                $('#chatBody').scrollTop($('#chatBody')[0].scrollHeight);
            }
        });
    });

    $('#chatForm').on('submit', function(e) {
        e.preventDefault();
        const message = $('#chatInput').val();
        const backendUrl = window.location.origin;
        if (message.trim() === '') return;

        //Append user's message
        $('#chatBody').append(`
            <div class="message user">
                <div class="text">${message}</div>
            </div>
        `);
        $('#chatInput').val('');

        console.log(message);

        $('#chatBody').append(`
            <div class="message ai">
                <div class="text">Getting response...</div>
            </div>
        `);

        //Get response from the backend API
        $.ajax({
            url: backendUrl + '/v1/ask-question',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ question: message }),
            crossDomain: true,
            success: function(response) {
                const aiMessage = response.result;
                $('#chatBody').children().last().remove();
                $('#chatBody').append(`
                    <div class="message ai">
                        <div class="text">${aiMessage}</div>
                    </div>
                `);
                $('#chatBody').scrollTop($('#chatBody')[0].scrollHeight);
            },
            error: function() {
                $('#chatBody').children().last().remove();
                $('#chatBody').append(`
                    <div class="message ai">
                        <div class="text">Sorry, there was an error processing your request.</div>
                    </div>
                `);
                $('#chatBody').scrollTop($('#chatBody')[0].scrollHeight);
            }
        });
    });
});
