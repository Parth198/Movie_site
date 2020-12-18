$(document).ready(function () {
    $.post("/", function (response) {
        console.log(response);


        //Appending
        $.each(response, function (index, value) {
            console.log(value.title);
            
            $("#input").append(`<div class="card card1">
                <img src='https://image.tmdb.org/t/p/w500/${value.poster_path}' alt="No photo">
                <div class="descriptions">
                    <h1>'${value.title}'</h1>
                    <p>
                        '${value.overview}'
                    </p>
                </div>
            </div>`)
        });
    });

});