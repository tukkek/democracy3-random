# Random country generator for [Democracy 3](https://store.steampowered.com/app/245470/Democracy_3/)

This Python script generates a random country (Randomia) based on configuration and policy ranges from the official countries in the base game and its DLCs. The resulting country is not guaranteed to be balanced but neither are the mods found on the Steam Workshop (in fact, in my experience they usually aren't).

Being based on the official country examples, Randomia is expected to be relatively balanced for most resulting outputs. This also means the resulting countries are pretty standard as they're not truly random - for example, you won't end up with a military dictatorship or religious fanatic nation since none of the built-in countries are examples of this.

## Installation

Copy the `Random` folder to the base Democracy 3 directory. Copy the `Random.txt` file to the existing `data/mods/` installation folder.

To generate a new random country before launching the game, run the script and manually copy the result into the `randomia.txt` file. Sadly, this is necessary as the game doesn't allow you to run arbitrary code on startup.

On Linux you can automate this process by linking the aforementioned files or folders instead of copying them and then running the provided launcher script to start the game instead.
