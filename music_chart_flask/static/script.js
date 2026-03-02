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




const button = document.getElementById("search");
const input = document.getElementById("song_name");
const resultsContainer = document.getElementById("results");


async function input_handler() {
    const name = input.value.trim();

    if (!name) {
        resultsContainer.innerHTML = "";
        return;
    }

    try {
        const response = await fetch(
            "http://127.0.0.1:5000/search?query=" + encodeURIComponent(name)
        );

        if (!response.ok) {
            throw new Error("Network response was not ok");
        }

        const songs = await response.json();

        // Clear old results
        resultsContainer.innerHTML = "";

        songs.forEach((value) => {
            if (value.song_name.toLowerCase().includes(name.toLowerCase())) {
                const div = document.createElement("div");
                div.textContent = value.artist + " - " + value.song_name;
                resultsContainer.appendChild(div);
            }
        });

    } catch (error) {
        console.error("Error:", error);
    }
}

try {
    input.addEventListener("input", input_handler);
    button.addEventListener("click", input_handler);
} catch (error) {

}