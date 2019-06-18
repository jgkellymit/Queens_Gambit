function make_board() {
    console.log("hello")
    var table = document.createElement("table");
    table.className = "board";
    for (var i = 1; i < 9; i++) {
        var tr = document.createElement('tr');
        for (var j = 1; j < 9; j++) {
            var td = document.createElement('td');
            if (i%2 == j%2) {
                td.className = "white";
            } else {
                td.className = "black";
            }
            tr.appendChild(td);
        }
        table.appendChild(tr);
    }
    var div = document.createElement("div")
    div.id = "test"
    div.appendChild(table)
    document.body.appendChild(div);
}
window.onload = make_board;
