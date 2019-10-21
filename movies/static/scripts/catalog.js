function getData(){
    $.ajax({
        url:'/api/movies',
        type:'GET',
        success:function(res){
            var movies = res.objects;
            for(var i = 0; i < movies.length; i++){
                displayMovie(movies[i]);
            }
        },
        error:function(details){
            console.log("Error on get req", details)
        }
    });
}

function displayMovie(movie){
    console.log(movie);

    var container = $(".cat-container");

    var li = `<li>${movie.title}</li>`;
    container.append(li);
};

function init() {
    console.log('Hello Catalog Page')

    getData();
}

window.onload=init();