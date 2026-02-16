// Список пісень
const songs = [
    "Imagine Dragons - Believer",
    "Ed Sheeran - Shape of You",
    "Beyoncé - Halo",
    "The Weeknd - Blinding Lights",
    "Coldplay - Viva La Vida",
    "Adele - Rolling in the Deep",
    "Maroon 5 - Sugar",
    "OneRepublic - Counting Stars",
    "Taylor Swift - Shake It Off",
    "Post Malone - Circles",
    "Shawn Mendes - Treat You Better",
    "Justin Bieber - Love Yourself",
    "Dua Lipa - Don't Start Now",
    "Lady Gaga - Shallow",
    "Billie Eilish - Bad Guy",
    "Bruno Mars - Uptown Funk",
    "Harry Styles - Watermelon Sugar",
    "Chainsmokers - Closer",
    "Linkin Park - Numb",
    "Katy Perry - Roar",
    "Sam Smith - Stay With Me"
];


window.onload = function(){
const songs_list = document.getElementById("songs_list");
songs.forEach(function(value, index){
        if(value.includes(name)){
            songs_list.innerHTML += "<li>" + value + "</li><br>";
        }
})

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