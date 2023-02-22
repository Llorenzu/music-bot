import random
import webbrowser

# Dictionary of artists and their songs
songs = {
    "Arctic Monkeys": ["Do I Wanna Know?", "R U Mine?", "505", "Fluorescent Adolescent", "Why'd You Only Call Me When You're High?"],
    "Tame Impala": ["The Less I Know The Better", "Elephant", "Feels Like We Only Go Backwards", "Mind Mischief", "Let It Happen"],
    "Lana Del Rey": ["Summertime Sadness", "Video Games", "Young and Beautiful", "Born to Die", "West Coast"],
    "The Weeknd": ["Blinding Lights", "Can't Feel My Face", "Starboy", "The Hills", "I Feel It Coming"],
    "Nirvana": ["Smells Like Teen Spirit", "Come As You Are", "Lithium", "In Bloom", "Heart-Shaped Box"],
    "The 1975": ["Love It If We Made It", "Chocolate", "Robbers", "The Sound", "Somebody Else"],
    "Mitski": ["Your Best American Girl", "Nobody", "Geyser", "Class of 2013", "Townie"],
    "Boy Genius": ["Me & My Dog", "Stay Down", "Salt in the Wound", "Bite the Hand", "Ketchum, ID"],
    "Boy Pablo": ["Everytime", "Sick Feeling", "Hey Girl", "Feeling Lonely", "Dance, Baby!"],
    "Peter Bjorn and John": ["Young Folks", "Second Chance", "Objects of My Affection", "Amsterdam", "Breaker Breaker"],
    "Beabadoobee": ["Coffee", "Care", "Worth It", "Sorry", "If You Want To"],
    "Rivermaya": ["214", "You'll Be Safe Here", "Himala", "Elesi", "Awit ng Kabataan"],
    "Eraserheads": ["Ang Huling El Bimbo", "Ligaya", "Magasin", "Pare Ko", "Overdrive"]
}

# Main loop
while True:
    user_input = input("Enter an artist(Arctic Monkeys, Tame Impala, Lana Del Rey, The Weeknd, Nirvana, The 1975, Mitski, Boy Genius, Boy Pablo, Peter Bjorn and John, Beabadoobee, Rivermaya, and Eraserheads) or type 'quit' to exit: ")
    
    if user_input == "quit":
        break
    
    if user_input in songs:
        artist_songs = songs[user_input]
        suggested_songs = random.sample(artist_songs, 5)
        print("Here are 5 songs by", user_input, ":\n")
        for song in suggested_songs:
            print("-", song)
            
        song_choice = input("\nType the name of a song to get a YouTube link: ")
        if song_choice in suggested_songs:
            query = user_input + " " + song_choice
            url = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open_new(url)
        else:
            print("Sorry, that's not one of the suggested songs.")
            
    else:
        print("Sorry, I don't know that artist.")
