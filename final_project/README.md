    # SPOTIFY STREAMING HISTROY SUMMARY
    #### Video Demo:  https://youtu.be/yRLut725rh0
    #### Description:
    **0 Index**
    I decided that I wanted to do something related to data and data analysis. Although the result so far is pretty basic, I have the intention of developing it farther. So the idea came from the yearly Spotify summary that each user gets in December. As a big music enthusiast myself, I always feel excited about it, so I thought why not to make it?
    Firstly, I thought about using requests as we did in bitcoin problem set, but then I found out that you can actually request your streaming data directly from Spotify which was of great help, though it took me a few days of waiting.
    Data obtained, I started investigating and quickly understood that I would be using the JSON files with date of a song listened, artist, name of the song in question and amount of time.
    **First Touches**
    So my first task was to actually make one file out of the four I was provided. This kind of a program is aimed at analyzing different data, so the number of files might differ. So at the end I thought that I need just one file. Probably this took me the longest as I simply couldn't manage to merge those files. Even tried ChatGPT, that code didn't work. Eventually, after some solid research on stackoverflow I found *the one*. The code that worked. So basically my mistake was that I was appending the files when I just had to extend them. Well, at least I know it for the future.
    **Second Touches (that should had been first)**
    Then I worked on accepting user input. In fact, I realized that I had to work on it firstly, but my obsession with merging the files was too strong. So this part is about checking the command line for the name and the "usage" practice showed at the last lecture. Then it's about collecting input. I used regular expression (I must admit this was the hardest to grasp during the lecture, but turned out to be very useful) to collect input. Filenames were stored into a list. When filename is incorrect, there's a message that says it and then it exits with "done". Thanks to so much practice with this in problem sets it was easy.
    **Human-like touches**
    Here I worked a bit with the main to make it a bit more "alive" (if you allow me to say that). It just provides the basic information about the project. Then I also used main only for calling the methods as I have learnt that you're better to keep your main clean and simple for yout own sake.
    **Pandas Tiny Bit**
    Just before I was reading about pandas library, so I thought first that I wanted to convert the JSON file into CSV as I had worked with it so much in problem sets. And then I remembered that basically I saw something about it a day before. So I used it and was extremely proud of myself.
    **In the Shadow of Java**
    My programming experience actually started with Java, so object-oriented stuff is my thing. Java is all about that even when it seems like isn't. So before I finished everything with CSV, I knew I would use it. This is how my SpotifyDataAnalyzer class came in. It takes the CSV file that was created and directly in init makes a library with another method.
    **Data for Summary**
    I chose five summary points and basically made classes based on those. Listening period relies on datatime library that was used in problem sets. So it basically takes the first entry and the last. Then defines duration by subtraction. Total listening time simply sums all entries from the created library (firstly converting miliseconds to minutes), then it provides total of minutes, hours and days.
    **Tops for Summary**
    Defining top performers, songs and days has the same logic. It creates a library for each entry, then iterates through the CSV-made library and sums up minuted listened. Then it just sorts the results by minutes listened. Looking back this looks pretty easy, although I had to dedicate a lot of time to planning and trying and failing actually. First I tried to make it on the spot, then I wrote it on a piece of paper. Then changed it a few times and maybe made a few schemes. In total it took some time for it to work. But when it did I was exceptionally relieved. At the and it basically provides the top 5 list with enumerate which I learnt thanks to this one.
    **About Testing**
    So I made testing only on one of the files and I had to change the return statements of the get methods to make the testing. I don't know how good this practice actually is but it passes.
    **Finishing**
    At the end I made the get_data and also added colors to make it a bit more interesting. Though I'm happy I have been able to work on this amount of data and get the results pretty fast. I would like to expand on this in the future.
    **THANKS CS50**