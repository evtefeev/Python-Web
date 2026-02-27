// Список пісень
const songs = $SONGS$;


window.onload = function(){
const songs_list = document.getElementById("songs_list");
    if(songs_list){
    songs.forEach(function(value, index){
            
        songs_list.innerHTML += "<li>" + value + "</li><br>";
            
    })

} 
}



const button = document.getElementById("search");
const input = document.getElementById("song_name");
const results = document.getElementById("results");

button.addEventListener("click", function(){
    const name = input.value;
    songs.forEach(function(value, index){
        if(value.includes(name)){
            results.textContent = value;
        }
    })
});