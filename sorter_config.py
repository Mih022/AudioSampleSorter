import os
import shutil

# ==============================================================================
# --- CONFIGURATION ---
# ==============================================================================

# 1. SET YOUR FOLDER PATHS
SOURCE_FOLDER = "D:\\mladi\\Documents\\FL relief"
#SOURCE_FOLDER = "C:\\Users\\mladi\\Documents\\Splice"


TARGET_FOLDER = "D:\\mladi\\Documents\\FL relief sorted"

# 2. SET THE MAXIMUM SEARCH DEPTH (None for unlimited)
MAX_DEPTH = None

# 3. SET PATHS TO IGNORE
#    Add any folder names or relative paths you want the script to skip.
#    The paths should be relative to your SOURCE_FOLDER.
#    Example: ["Previews", "Project Files/Old Versions"]
IGNORED_PATHS = [
    "__MACOSX",  # Often contains metadata files you don't need
    ".DS_Store", # macOS system files
    "Sounds of KSHMR",
    "A kapele",
    "FLP remakeovi",
    "MIHO Graphics"
]

# 3. DEFINE YOUR SORTING RULES
#    - 'priority': An integer. Higher numbers have higher priority.
#    - 'destination': The target subfolder.
#    - 'extensions': A list of file extensions to match.
#    - 'keywords': A list of words that MUST ALL be in the filename.
SORTING_RULES = [
    # -- PRESETS --
    # A specific rule for Serum presets has a high priority.
    {
        'priority': 100,
        'destination': 'Presets/Serum',
        'extensions': ['.fxp'],
        'keywords': ['serum']
    },
    # A generic .fxp rule has a very low priority, acting as a fallback.
    {
        'priority': 10,
        'destination': 'Presets/Sylenth1',
        'extensions': ['.fxp'],
        'keywords': []
    },
    {
        'priority': 100,
        'destination': 'Presets/Massive',
        'extensions': ['.nmsv'],
        'keywords': []
    },

    # -- DRUMS --

    {
        'priority': 100,
        'destination': 'Samples/Drums/Kicks/Big Kicks',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['kick', 'big']
    },
    {
        'priority': 100,
        'destination': 'Samples/Drums/Kicks/Punchy Kicks',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['kick', 'punchy']
    },
    {
        'priority': 100,
        'destination': 'Samples/Drums/Kicks/Stomp Kicks',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['kick', 'stomp']
    },
    {
        'priority': 100,
        'destination': 'Samples/Drums/Kicks/Top Kicks',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['kick', 'top']
    },
    {
        'priority': 90,
        'destination': 'Samples/Drums/Kicks/Other',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['kick']
    },
    {
        'priority': 89,
        'destination': 'Samples/Drums/Kicks',
        'extensions': ['.wav', '.mp3'],
        'keywords': ['bd']
    },
    {
        'priority': 100,
        'destination': 'Samples/Drums/808s',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['808']
    },

    {
        'priority': 100,
        'destination': 'Samples/Drums/Snares/Big Snares',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['snare', 'big']
    },
    {
        'priority': 100,
        'destination': 'Samples/Drums/Snares/Hard Snares',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['snare', 'hard']
    },
    {
        'priority': 100,
        'destination': 'Samples/Drums/Snares/Tight Snares',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['snare', 'tight']
    },
    {
        'priority': 90,
        'destination': 'Samples/Drums/Snares/Other',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['snare']
    },

    {
        'priority': 101,
        'destination': 'Samples/Drums/Claps/Drop Claps',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['clap', 'drop']
    },
    {
        'priority': 101,
        'destination': 'Samples/Drums/Claps/Pre-shifted Claps',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['clap', 'shifted']
    },
    {
        'priority': 101,
        'destination': 'Samples/Drums/Claps/Regular Claps',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['clap', 'regular']
    },
    {
        'priority': 101,
        'destination': 'Samples/Drums/Claps/Stadium Claps',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['clap', 'stadium']
    },
    {
        'priority': 91,
        'destination': 'Samples/Drums/Claps/Other',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['clap']
    },
    {
        'priority': 101,
        'destination': 'Samples/Drums/Snaps',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['snap']
    },
    {
        'priority': 101,
        'destination': 'Samples/Drums/Toms',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['tom']
    },

    {
        'priority': 100,
        'destination': 'Samples/Drums/Cymbals/Hats/Closed',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['hat', 'closed']
    },
    {
        'priority': 100,
        'destination': 'Samples/Drums/Cymbals/Hats/Open',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['hat', 'open']
    },
    {
        'priority': 50,
        'destination': 'Samples/Drums/Cymbals/Hats/Other',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['hat']
    },
    {
        'priority': 100,
        'destination': 'Samples/Drums/Cymbals/Rides',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['ride']
    },
    {
        'priority': 100,
        'destination': 'Samples/Drums/Cymbals/Crashes',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['crash']
    },
    {
        'priority': 100,
        'destination': 'Samples/Drums/Cymbals/Transitions',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['cymbal', 'transition']
    },

    {
        'priority': 100,
        'destination': 'Samples/Drums/Percussion/High',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['percussion', 'high']
    },
    {
        'priority': 99,
        'destination': 'Samples/Drums/Percussion/High',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['perc', 'high']
    },
    {
        'priority': 100,
        'destination': 'Samples/Drums/Percussion/Low',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['percussion', 'low']
    },
    {
        'priority': 99,
        'destination': 'Samples/Drums/Percussion/Low',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['perc', 'low']
    },

    {
        'priority': 95,
        'destination': 'Samples/Drums/Percussion/Flams and Rolls',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['percussion', 'flam']
    },
    {
        'priority': 94,
        'destination': 'Samples/Drums/Percussion/Flams and Rolls',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['perc', 'flam']
    },
    {
        'priority': 95,
        'destination': 'Samples/Drums/Percussion/Flams and Rolls',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['percussion', 'roll']
    },
    {
        'priority': 94,
        'destination': 'Samples/Drums/Percussion/Flams and Rolls',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['perc', 'roll']
    },
    {
        'priority': 100,
        'destination': 'Samples/Drums/Percussion/Shakers',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['shaker']
    },
    {
        'priority': 80,
        'destination': 'Samples/Drums/Percussion/Foley',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['foley']
    },

    {
        'priority': 20,
        'destination': 'Samples/Drums/Percussion/Other',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['percussion']
    },
    {
        'priority': 10,
        'destination': 'Samples/Drums/Percussion/Unsorted',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['perc']
    },


    # -- DRUM LOOPS --
    {
        'priority': 100,
        'destination': 'Samples/Drums/Loops/Top Loops',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['loop', 'top']
    },
    {
        'priority': 100,
        'destination': 'Samples/Drums/Loops/Percussion Loops',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['loop', 'percussion']
    },
    {
        'priority': 100,
        'destination': 'Samples/Drums/Loops/Buildup Drums',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['loop', 'percussion']
    },
    {
        'priority': 100,
        'destination': 'Samples/Drums/Loops/Indian Drum Loops',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['loop', 'drum', 'indian']
    },
    {
        'priority': 100,
        'destination': 'Samples/Drums/Loops/Clap Loops',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['loop', 'clap']
    },
    {
        'priority': 100,
        'destination': 'Samples/Drums/Loops/Hat Loops',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['loop', 'hat']
    },
    {
        'priority': 100,
        'destination': 'Samples/Drums/Loops/Shaker Loops',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['loop', 'shaker']
    },
    {
        'priority': 100,
        'destination': 'Samples/Drums/Loops/Stadium Loops',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['loop', 'stadium']
    },
    {
        'priority': 5,
        'destination': 'Samples/Drums/Loops',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['loop', 'drum']
    },

    # -- FILLS --
    {
        'priority': 100,
        'destination': 'Samples/Fills/Acoustic Fills',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['fill', 'acoustic']
    },
    {
        'priority': 100,
        'destination': 'Samples/Fills/Short Fills',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['fill', 'short']
    },
    {
        'priority': 100,
        'destination': 'Samples/Fills/Long Fills',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['fill', 'long']
    },
    {
        'priority': 100,
        'destination': 'Samples/Fills/Synth Fills',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['fill', 'synth']
    },
    {
        'priority': 50,
        'destination': 'Samples/Fills/Synth Fills',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['fill', 'synth']
    },
    {
        'priority': 50,
        'destination': 'Samples/Fills/Dubstep Fills',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['fill', 'dubstep']
    },
    {
        'priority': 10,
        'destination': 'Samples/Fills/Dubstep Fills',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['fill']
    },

    # -- LOOPS --

    {
        'priority': 10,
        'destination': 'Samples/Loops/',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['loop']
    },
    {
        'priority': 11,
        'destination': 'Samples/Loops/Melodies',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['melody']
    },


    # -- FX --

    {
        'priority': 90,
        'destination': 'Samples/FX/Airlocks',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['airlock']
    },
    {
        'priority': 90,
        'destination': 'Samples/FX/Alarms',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['alarm']
    },
    # ambiance
    {
        'priority': 90,
        'destination': 'Samples/FX/Ambiance/Airy',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['ambiance', 'airy']
    },
    {
        'priority': 50,
        'destination': 'Samples/FX/Ambiance/Drone',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['drone']
    },
    {
        'priority': 30,
        'destination': 'Samples/FX/Ambiance/Reverbed',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['reverb']
    },
    {
        'priority': 90,
        'destination': 'Samples/FX/Ambiance/Bird calls',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['ambiance', 'bird', 'call']
    },
    {
        'priority': 90,
        'destination': 'Samples/FX/Ambiance/Fear',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['ambiance', 'fear']
    },
    {
        'priority': 90,
        'destination': 'Samples/FX/Ambiance/Hard Strikes',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['ambiance', 'hard strikes']
    },
    {
        'priority': 90,
        'destination': 'Samples/FX/Ambiance/Pretty',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['ambiance', 'pretty']
    },
    {
        'priority': 40,
        'destination': 'Samples/FX/Ambiance/Rain',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['rain']
    },
    {
        'priority': 85,
        'destination': 'Samples/FX/Ambiance/Nature',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['ambiance', 'nature']
    },
    {
        'priority': 85,
        'destination': 'Samples/FX/Ambiance/Nature',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['ambiance', 'natural']
    },
    {
        'priority': 40,
        'destination': 'Samples/FX/Ambiance/Other',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['ambiance']
    },
    {
        'priority': 40,
        'destination': 'Samples/FX/Ambiance/Other',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['ambience']
    },
    {
        'priority': 80,
        'destination': 'Samples/FX/Ambiance/Airy',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['amb', 'airy']
    },
    {
        'priority': 80,
        'destination': 'Samples/FX/Ambiance/Bird calls',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['amb', 'bird', 'call']
    },
    {
        'priority': 80,
        'destination': 'Samples/FX/Ambiance/Fear',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['amb', 'fear']
    },
    {
        'priority': 80,
        'destination': 'Samples/FX/Ambiance/Hard Strikes',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['amb', 'hard strikes']
    },
    {
        'priority': 80,
        'destination': 'Samples/FX/Ambiance/Pretty',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['amb', 'pretty']
    },
    {
        'priority': 80,
        'destination': 'Samples/FX/Ambiance/Rain',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['amb', 'rain']
    },
    {
        'priority': 75,
        'destination': 'Samples/FX/Ambiance/Nature',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['amb', 'nature']
    },
    {
        'priority': 75,
        'destination': 'Samples/FX/Ambiance/Nature',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['amb', 'natural']
    },
    {
        'priority': 10,
        'destination': 'Samples/FX/Ambiance/Other',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['amb']
    },

    {
        'priority': 50,
        'destination': 'Samples/FX/Animals',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['animals']
    },
    {
        'priority': 50,
        'destination': 'Samples/FX/Clocks',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['clock']
    },
    {
        'priority': 50,
        'destination': 'Samples/FX/Hoovers',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['hoover']
    },
    {
        'priority': 50,
        'destination': 'Samples/FX/Exhausts',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['exhaust']
    },
    {
        'priority': 50,
        'destination': 'Samples/FX/Glitches',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['glitch']
    },
    {
        'priority': 50,
        'destination': 'Samples/FX/Impacts',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['impact']
    },
    {
        'priority': 20,
        'destination': 'Samples/FX/Impacts',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['hit']
    },
    {
        'priority': 50,
        'destination': 'Samples/FX/Reverb Plucks',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['reverb', 'pluck']
    },
    {
        'priority': 50,
        'destination': 'Samples/FX/Reverse',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['reverse']
    },
    {
        'priority': 50,
        'destination': 'Samples/FX/Stabs',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['stab']
    },
    {
        'priority': 40,
        'destination': 'Samples/FX/Sub Drops',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['sub', 'drop']
    },
    # sweeps
    {
        'priority': 50,
        'destination': 'Samples/FX/Sweeps/Transitions',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['sweep', 'transition']
    },
    {
        'priority': 50,
        'destination': 'Samples/FX/Sweeps/Up/Long',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['sweep', 'up', 'long'],
    },
    {
        'priority': 50,
        'destination': 'Samples/FX/Sweeps/Up/Short',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['sweep', 'up', 'short'],
    },
    {
        'priority': 50,
        'destination': 'Samples/FX/Sweeps/Up/Medium',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['sweep', 'up', 'medium'],
    },
    {
        'priority': 49,
        'destination': 'Samples/FX/Sweeps/Up/Other',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['sweep', 'up'],
    },
    {
        'priority': 50,
        'destination': 'Samples/FX/Sweeps/Down/Long',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['sweep', 'down', 'long'],
    },
    {
        'priority': 50,
        'destination': 'Samples/FX/Sweeps/Down/Short',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['sweep', 'down', 'short'],
    },
    {
        'priority': 50,
        'destination': 'Samples/FX/Sweeps/Down/Medium',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['sweep', 'down', 'medium'],
    },
    {
        'priority': 49,
        'destination': 'Samples/FX/Sweeps/Down/Other',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['sweep', 'down'],
    },
    {
        'priority': 45,
        'destination': 'Samples/FX/Sweeps/Other',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['sweep']
    },

    {
        'priority': 100,
        'destination': 'Samples/FX/White Noise/Up',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['white', 'noise', 'up']
    },
    {
        'priority': 100,
        'destination': 'Samples/FX/White Noise/Down',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['white', 'noise', 'down']
    },
    {
        'priority': 100,
        'destination': 'Samples/FX/White Noise/Down',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['white', 'noise', 'splash']
    },
    {
        'priority': 90,
        'destination': 'Samples/FX/White Noise/Other',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['white', 'noise']
    },
    {
        'priority': 10,
        'destination': 'Samples/FX/White Noise/Other',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['noise']
    },

    {
        'priority': 100,
        'destination': 'Samples/FX/Risers/Long',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['riser', 'long']
    },
    {
        'priority': 100,
        'destination': 'Samples/FX/Risers/Short',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['riser', 'short']
    },
    {
        'priority': 90,
        'destination': 'Samples/FX/Risers/Other',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['riser']
    },

        {
        'priority': 100,
        'destination': 'Samples/FX/Downlifters/Long',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['downlifter', 'long']
    },
    {
        'priority': 100,
        'destination': 'Samples/FX/Downlifters/Short',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['downlifter', 'short']
    },
    {
        'priority': 90,
        'destination': 'Samples/FX/Downlifters/Other',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['downlifter']
    },
    {
        'priority': 80,
        'destination': 'Samples/FX/Downlifters/Other',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['faller']
    },


    {
        'priority': 50,
        'destination': 'Samples/FX/Tape Stops',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['tape stop']
    },
    {
        'priority': 90,
        'destination': 'Samples/FX/Vinyl',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['vinyl', 'crackle']
    },
    {
        'priority': 90,
        'destination': 'Samples/FX/Vinyl',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['vinyl', 'scratch']
    },
    {
        'priority': 90,
        'destination': 'Samples/FX/Vinyl',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['vinyl', 'start']
    },
    {
        'priority': 90,
        'destination': 'Samples/FX/Vinyl',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['vinyl', 'stop']
    },
    {
        'priority': 10,
        'destination': 'Samples/FX/Vinyl',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['vinyl']
    },

    {
        'priority': 50,
        'destination': 'Samples/FX/War Horns',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['war horn']
    },
    {
        'priority': 50,
        'destination': 'Samples/FX/Water Drops',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['water drop']
    },
    {
        'priority': 10,
        'destination': 'Samples/FX/Zipties',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['zip']
    },

    # -- LIVE INSTRUMENTS --

    {
        'priority': 100,
        'destination': 'Samples/Instruments/Guitar/Loops',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['guitar', 'loop']
    },
    {
        'priority': 100,
        'destination': 'Samples/Instruments/Guitar/One Shots',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['guitar', 'one', 'shot']
    },
    {
        'priority': 50,
        'destination': 'Samples/Instruments/Guitar/Other',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['guitar']
    },

    {
        'priority': 100,
        'destination': 'Samples/Instruments/Piano/Loops',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['piano', 'loop']
    },
    {
        'priority': 90,
        'destination': 'Samples/Instruments/Piano/One Shots',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['piano', 'one', 'shot']
    },
    {
        'priority': 110,
        'destination': 'Samples/Instruments/Piano/Chords',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['piano', 'chords']
    },
    {
        'priority': 50,
        'destination': 'Samples/Instruments/Piano/Other',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['piano']
    },

    {
        'priority': 50,
        'destination': 'Samples/Instruments/Strings/Violin',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['violin']
    },
    {
        'priority': 50,
        'destination': 'Samples/Instruments/Strings/Other',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['string']
    },
    {
        'priority': 50,
        'destination': 'Samples/Instruments/Bells',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['bell']
    },
    {
        'priority': 50,
        'destination': 'Samples/Instruments/Flute',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['flute']
    },

    {
        'priority': 50,
        'destination': 'Samples/Instruments/Ethnic/Main',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['bansuri']
    },
    {
        'priority': 50,
        'destination': 'Samples/Instruments/Ethnic/Main',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['bayan']
    },
    {
        'priority': 50,
        'destination': 'Samples/Instruments/Ethnic/Main',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['bura']
    },
    {
        'priority': 50,
        'destination': 'Samples/Instruments/Ethnic/Main',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['duduk']
    },
    {
        'priority': 50,
        'destination': 'Samples/Instruments/Ethnic/Main',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['harmonium']
    },
    {
        'priority': 20,
        'destination': 'Samples/Instruments/Ethnic/Main',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['indian']
    },
    {
        'priority': 50,
        'destination': 'Samples/Instruments/Ethnic/Main',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['kemenche']
    },
    {
        'priority': 10,
        'destination': 'Samples/Instruments/Ethnic/Main',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['mey']
    },
    {
        'priority': 10,
        'destination': 'Samples/Instruments/Ethnic/Main',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['morsing']
    },
    {
        'priority': 10,
        'destination': 'Samples/Instruments/Ethnic/Main',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['ney']
    },
    {
        'priority': 10,
        'destination': 'Samples/Instruments/Ethnic/Main',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['oud']
    },
    {
        'priority': 10,
        'destination': 'Samples/Instruments/Ethnic/Main',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['santur']
    },
    {
        'priority': 10,
        'destination': 'Samples/Instruments/Ethnic/Main',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['oud']
    },
    {
        'priority': 10,
        'destination': 'Samples/Instruments/Ethnic/Main',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['swarmandal']
    },
    {
        'priority': 10,
        'destination': 'Samples/Instruments/Ethnic/Main',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['tumbi']
    },

    {
        'priority': 50,
        'destination': 'Samples/Instruments/Ethnic/Sitar/Sitar Ambiance',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['sitar', 'ambiance']
    },
    {
        'priority': 50,
        'destination': 'Samples/Instruments/Ethnic/Sitar/Sitar Loops',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['sitar', 'loop']
    },

    {
        'priority': 50,
        'destination': 'Samples/Instruments/Whistle',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['whistle']
    },
    






    # -- SYNTHS --

    {
        'priority': 80,
        'destination': 'Samples/Synths/Arps',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['arp']
    },
    {
        'priority': 50,
        'destination': 'Samples/Synths/Chords',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['chords']
    },
    {
        'priority': 20,
        'destination': 'Samples/Synths/Keys',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['keys']
    },
    {
        'priority': 80,
        'destination': 'Samples/Synths/Bass/One Shots',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['bass', 'shot']
    },
    {
        'priority': 80,
        'destination': 'Samples/Synths/Bass/Loops',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['bass', 'loop']
    },
    {
        'priority': 80,
        'destination': 'Samples/Synths/Bass/Stabs',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['bass', 'stab']
    },
    {
        'priority': 10,
        'destination': 'Samples/Synths/Bass/Other',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['bass']
    },

    {
        'priority': 30,
        'destination': 'Samples/Synths/Stabs',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['stab']
    },
    {
        'priority': 80,
        'destination': 'Samples/Synths/Growls',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['growl']
    },
    {
        'priority': 80,
        'destination': 'Samples/Synths/One Shots',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['synth', 'shot']
    },
    {
        'priority': 80,
        'destination': 'Samples/Synths/One Shots',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['tonal', 'one', 'shot']
    },
    {
        'priority': 80,
        'destination': 'Samples/Synths/Ear Candy',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['ear', 'candy']
    },
    {
        'priority': 80,
        'destination': 'Samples/Synths/Ear Candy',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['ecfx', 'trill']
    },
    {
        'priority': 20,
        'destination': 'Samples/Synths/Leads',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['lead']
    },
    {
        'priority': 20,
        'destination': 'Samples/Synths/Plucks',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['pluck']
    },
    {
        'priority': 10,
        'destination': 'Samples/Synths/Plucks',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['synth']
    },
    

    # -- SAMPLES: VOCALS --

    {
        'priority': 100,
        'destination': 'Samples/Vocals/Vocal Chops',
        'extensions': ['.wav', '.mp3'],
        'keywords': ['vocal', 'chop']
    },
    {
        'priority': 100,
        'destination': 'Samples/Vocals/Vocal Tones',
        'extensions': ['.wav', '.mp3'],
        'keywords': ['vocal', 'tone']
    },
    {
        'priority': 50,
        'destination': 'Samples/Vocals/Vocal Tones',
        'extensions': ['.wav', '.mp3'],
        'keywords': ['vox', 'tone']
    },
    {
        'priority': 100,
        'destination': 'Samples/Vocals/Vocal Words',
        'extensions': ['.wav', '.mp3'],
        'keywords': ['vocal', 'word']
    },
    {
        'priority': 50,
        'destination': 'Samples/Vocals/Vocal Words',
        'extensions': ['.wav', '.mp3'],
        'keywords': ['vox', 'word']
    },
    {
        'priority': 100,
        'destination': 'Samples/Vocals/Ethnic Vocals',
        'extensions': ['.wav', '.mp3'],
        'keywords': ['Ethnic Vocal']
    },
    {
        'priority': 100,
        'destination': 'Samples/Vocals/Vocal Beds',
        'extensions': ['.wav', '.mp3'],
        'keywords': ['vocal', 'bed']
    },
    {
        'priority': 100,
        'destination': 'Samples/Vocals/Vocal Shouts',
        'extensions': ['.wav', '.mp3'],
        'keywords': ['vocal', 'shout']
    },
    {
        'priority': 50,
        'destination': 'Samples/Vocals/Vocal Chants',
        'extensions': ['.wav', '.mp3'],
        'keywords': ['chant']
    },

    {
        'priority': 100,
        'destination': 'Samples/Vocals/Vocal Performance',
        'extensions': ['.wav', '.mp3'],
        'keywords': ['vocal', 'hook']
    },
    {
        'priority': 50,
        'destination': 'Samples/Vocals/Vocal Performance',
        'extensions': ['.wav', '.mp3'],
        'keywords': ['vox', 'hook']
    },
    {
        'priority': 100,
        'destination': 'Samples/Vocals/Vocal Performance',
        'extensions': ['.wav', '.mp3'],
        'keywords': ['vocal', 'phrase']
    },
    {
        'priority': 50,
        'destination': 'Samples/Vocals/Vocal Performance',
        'extensions': ['.wav', '.mp3'],
        'keywords': ['vox', 'phrase']
    },
    {
        'priority': 100,
        'destination': 'Samples/Vocals/Vocal Performance',
        'extensions': ['.wav', '.mp3'],
        'keywords': ['vocal', 'adlib']
    },
    {
        'priority': 40,
        'destination': 'Samples/Vocals/Vocal Performance',
        'extensions': ['.wav', '.mp3'],
        'keywords': ['adlib']
    },
    {
        'priority': 50,
        'destination': 'Samples/Vocals/Vocal Performance',
        'extensions': ['.wav', '.mp3'],
        'keywords': ['acapella']
    },


    {
        'priority': 10,
        'destination': 'Samples/Vocals/Other',
        'extensions': ['.wav', '.mp3'],
        'keywords': ['vocal']
    },


    # -- MIDI --
    {
        'priority': 100,
        'destination': 'MIDI/',
        'extensions': ['.mid'],
        'keywords': ['']
    },

]

