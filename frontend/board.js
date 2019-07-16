function make_board() {
    var player = localStorage.getItem("playerName");
    var opponent = localStorage.getItem("opponentName");

    // Create a board for gameplay
    var title = document.createElement("div");
    title.innerText = player + " vs " + opponent;
    document.body.appendChild(title);


    var table = document.createElement("table");
    table.className = "board";
    for (var i = 0; i < 8; i++) {
        var tr = document.createElement('tr');
        for (var j = 0; j < 8; j++) {
            var td = document.createElement('td');
            td.id = j.toString() + "_" + (7 - i).toString();
            td.onclick = place_pawn;
            // td.addEventListener("click", place_pawn(td));

            if (i%2 == j%2) {
                td.className = "white";
            } else {
                td.className = "black";
            }
            tr.appendChild(td);
        }
        table.appendChild(tr);
    }
    var div = document.createElement("div");
    div.id = "outer_box";
    div.appendChild(table);
    document.body.appendChild(div);
}
window.onload = make_board;


function place_pawn(click_event) {
    // Click on a square that you want pawn to be placed at, relay message to server
    // Have server redraw the board with the placed pawn,
    // Then block until opponent has placed a pawn

    var td = click_event["path"][0];

    var pawn_elem = document.createElement("img");
    pawn_elem.className = "piece_image";

    if (parseInt(td.id.slice(-1)) < 4){
        pawn_elem.src = "white_pawn.png";
    }
    else{
        pawn_elem.src = "black_pawn.png";

    }
    var div = document.createElement("div");
    div.className = "square";
    div.appendChild(pawn_elem);
    td.appendChild(div);
    relay_pawn_place(click_event);
}

function relay_pawn_place(event){
    // Send message to server with pawn place -- necessary?
    console.log(event.path);
    var selectedText = "jack";

    $.ajax({
        type: 'POST',
        url: "http://localhost:5000/test",
        data: {"position": event.path[0].id},
        success: function(response) {
            console.log(response)
        },
        error: function(error) {
            console.log(error)
        }
    });

}

function place_pieces_from_server(matrix){
    // Given a matrix representing where all pieces are located, place the images of the pieces
    // at each of the positions on the board.
}


function highlight_squares(square_list){
    //highlight previous move, or highlight possible moves on hover or click?

}

function select_piece(){
    // After pawns of been placed, this function will be assigned to the onclick event for the pieces (images)
    // Highlights selected piece and assigns onclick commands to other elements on the board that will then relay
    // possible move to server
}

function deselect_piece(){
    //deselect piece
}

function assign_select_onclick(){
    // Assigns select commands to all pieces (imgs?) on the board
}

function assign_move_onclick(){
    // Assigns move commands to all locations on the board (except selected piece, which gets deselected on click)
}

function move_pieces(){
    //After a piece has been selected, and a second square is clicked as a possible move, relay this info to the server
    // to see if the potential move is legal. If it is move the piece, if not don't. TODO: Some sort of confirmation message?
}

function upgrade_piece(){
    // Once you lose a piece, at the beginning of your turn you can choose a piece to upgrade
}



