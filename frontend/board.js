function make_board() {
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
    relay_pawn_place();
}

function relay_pawn_place(){

    $(function() {
        $.ajax({
            type: 'POST',
            url: "http://localhost:5000/test",
            data: "jack",
            success: function(response) {
                console.log(response)
            },
            error: function(error) {
                console.log(error)
            }
        });
    });
}


