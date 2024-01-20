# TeamB Dsl : MusicML 🎵 

This repository contains an internal Domain-Specific Language (DSL) for composing music using Python and textx as a language development framework. The DSL operates on the MIDI standard and is implemented using the `midiutil` Python library.

The DSL is designed for musicians who want to write their partitions using our language and have it generated as a MIDI file that is playable on any MIDI player.

## Extensions and AddOn done :
Here are the extensions that have been implemented on top of our language:
- **Support for bar modifications** 
- **Support for human like errors**
- **Support for user interactive input**
Additionally, the following add-ons have been integrated:
- **MIDI Visualizer & Player** : Enables users to witness their musical creations come to life interactively and instantly.
- **Monaco Editor** : External validator for our DSL, enhancing the editing and validation process.

## Content

The repository contains the following:

- **docs** : This section includes :
  - `music-ml.bnf` : the grammar defined in Backus–Naur Form (BNF).
  - `notes.md` : detailed notes providing explanations about MIDI.
  - `architecture.svg`: a metamodel representing the MusicML model.

- **src** : It contains the kernel of the developped language, and the extensions developped. It contains the following sub-directories :
  - `app`  : This sub-directory contains the source code for the interactive interface dedicated to visualizing the composed piece.
  - `textxmonaco` : This sub-directory hosts the Monaco editor designed for the application DSL. For more details, refer to [src/textx-monaco/README.md](https://github.com/benaissanadim/DSL-MusicML-TeamB/blob/main/src/textx-monaco/README.md) 

- **scenarios** : This section comprises various examples and scenarios in the `.mml` format, demonstrating the full range of functionalities achievable using our DSL. For more information about these scenarios, refer to the report in the `docs`section.

- **generated** : This section specifically houses MIDI files in the `.mid` format, generated from the implemented scenarios, providing tangible results that highlight the expressive capabilities of the DSL.

## Usage
**1. Install Python :**

First, ensure that Python is installed on your system. If not, you can download and install it from the [official Python website](https://www.python.org/). The recommended version is 3.8.

**2. Install Libraries :**

Run the setup.sh script located in the root directory  to install the necessary libraries.
```
./setup.sh
```
This script checks the installation status of the  `midiutil`, `textx` and  `Flask`packages using pip, installing them if they are not already present.

**3. Use DSL:**

To use our Domain-Specific Language (DSL), follow these steps:
- Write  a scenario following our language specifications and save it in the "scenarios" directory with the .mml format.
-  Execute the scenario using the following command:
```
./run-scenario.sh <file>.mml
```
**NB:**
To activate the interactive interface dedicated to visualizing the composed piece, you need to add the following line at the beginning of your DSL written in the `<file>.mml`:
```plaintext
Live on
```

## Resources :

- For the MIDI visualizer and player : [webaudiofont](https://surikov.github.io/webaudiofont/)
- For the Internal DSL : [textX](https://github.com/textX)
