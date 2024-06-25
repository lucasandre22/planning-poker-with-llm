$(document).ready(function() {
    $('#chatFormTicket').on('submit', function(e) {
        e.preventDefault();
        const backendUrl = window.location.origin;
        const ticket = $('#ticketInput').val();
        console.log("ticket:" + ticket);

        $.ajax({
            url: 'http://localhost:8080/v1/get-output',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ ticket }),
            crossDomain: true,
            success: function(response) {
                displayTickets(response);
            },
            error: function() {
                console.error('Error fetching tickets:', error);
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

        $('#chatBody').scrollTop = $('#chatBody').scrollHeight

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

function displayTickets(data) {
    const $ticketsContainer = $('#ticketsContainer');
    $ticketsContainer.empty();

    data.similar_tickets.forEach(ticket => {
        const $ticketCard = $('<div>').addClass('ticket-card').css({"overflow" : "auto"});

        const $ticketTitle = $('<h3>').text(ticket.ticket);

        const $ticketName = $('<p>').text(`${ticket.summary}`);

        const $ticketDescription = $('<div>').text(`Description: ${ticket.description}`);
        $ticketDescription.css({"overflow" : "auto"});

        const $link = $('<a>').attr('href', "https://www.google.com.br").text("Open ticket").css({"color": "#4CAF50"});

        const $type = $('<p>').text(`Type: ${ticket.type}`);

        const $story_points = $('<p>').text(`Story points: ${ticket.story_points}`);


        $ticketCard.append($ticketTitle, $ticketName, $ticketDescription, $type, $story_points, $link);
        $ticketsContainer.append($ticketCard);
    });

    const markdownAiReponse = data.result;

    $('#chatBody').append(`
        <div class="message ai">
            <div class="text">${markdownAiReponse}</div>
        </div>
    `);

    const recommendedStoryPoints = $('<div>').text(`Recommended story points: ${data.recommended_story_points}`);

}

