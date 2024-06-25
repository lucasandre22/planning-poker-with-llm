$(document).ready(function() {
    $('#chatFormTicket').on('submit', function(e) {
        e.preventDefault();
        const backendUrl = window.location.origin;
        const ticket = $('#ticketInput').val();
        console.log("ticket:" + ticket);

        const $ticketsContainer = $('#ticketsContainer');
        $ticketsContainer.empty();
        putLoadingGif();

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
                alert('Error fetching tickets, check the connection to backend');
                removeLoadingGif();
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

function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function putLoadingGif() {
    const $ticketsContainer = $('#ticketsContainer');
    const $div = $('<div>');
    const $text = $('<h3>').text("Wait a little bit, the AI needs to think!").css({"text-align" : "center"});
    const $estimatedTime = $('<p>').text("Estimated time: " + getRandomNumber(23, 45) + " seconds").css({"text-align" : "center"});
    const $loadingGif = $('<img>', {
        id: 'mickey loading',
        src: 'loading.gif',
        alt: '100'
    })
    $div.append($text, $loadingGif, $estimatedTime);
    $ticketsContainer.append($div);
}

function removeLoadingGif() {
    const $ticketsContainer = $('#ticketsContainer');
    $ticketsContainer.empty();
}

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

        const $space = $('<p>')
        const $type = $('<p>').text(`Type: ${ticket.type}`);

        const $story_points = $('<p>').text(`Story points: ${ticket.story_points}`);


        $ticketCard.append($ticketTitle, $ticketName, $ticketDescription, $space, $type, $story_points, $link);
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

document.addEventListener("DOMContentLoaded", () => {
    const cardsContainer = document.querySelector('.cards-container');
    const tableContent = document.querySelector('.table-content');

    cardsContainer.addEventListener('click', (event) => {
        if (event.target.classList.contains('card')) {
            moveCardToTable(event.target);
        }
    });

    tableContent.addEventListener('click', (event) => {
        if (event.target.classList.contains('card')) {
            moveCardToDeck(event.target);
        }
    });

    function moveCardToTable(card) {
        const rect = card.getBoundingClientRect();
        const clone = card.cloneNode(true);
        const tableRect = tableContent.getBoundingClientRect();

        clone.style.position = 'absolute';
        clone.style.top = `${rect.top}px`;
        clone.style.left = `${rect.left}px`;
        clone.style.transition = 'all 1s ease';
        document.body.appendChild(clone);

        setTimeout(() => {
            clone.style.top = `${tableRect.top + tableContent.clientHeight / 2 - clone.clientHeight / 2}px`;
            clone.style.left = `${tableRect.left + tableContent.clientWidth / 2 - clone.clientWidth / 2}px`;
        }, 10);

        setTimeout(() => {
            tableContent.appendChild(clone);
            clone.style.position = 'static';
            clone.style.top = '';
            clone.style.left = '';
            clone.style.transition = '';
            card.style.visibility = 'hidden';
        }, 1010);
    }

    function moveCardToDeck(card) {
        const rect = card.getBoundingClientRect();
        const originalCard = [...cardsContainer.children].find(c => c.dataset.number === card.dataset.number);

        const clone = card.cloneNode(true);
        const cardRect = originalCard.getBoundingClientRect();

        clone.style.position = 'absolute';
        clone.style.top = `${rect.top}px`;
        clone.style.left = `${rect.left}px`;
        clone.style.transition = 'all 1s ease';
        document.body.appendChild(clone);

        setTimeout(() => {
            clone.style.top = `${cardRect.top}px`;
            clone.style.left = `${cardRect.left}px`;
        }, 10);

        setTimeout(() => {
            document.body.removeChild(clone);
            originalCard.style.visibility = 'visible';
            tableContent.removeChild(card);
        }, 1010);
    }
});

