import os
import shutil

# ==============================================================================
# --- CONFIGURATION ---
# ==============================================================================

# 1. SET YOUR FOLDER PATHS
SOURCE_FOLDER = "path/to/your/unorganized/files"
TARGET_FOLDER = "path/to/your/new/sorted/folder"

# 2. SET THE MAXIMUM SEARCH DEPTH (None for unlimited)
MAX_DEPTH = None

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
        'destination': 'Samples/Drums/Kicks',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['kick']
    },
    {
        'priority': 99,
        'destination': 'Samples/Drums/Kicks',
        'extensions': ['.wav', '.mp3'],
        'keywords': ['bd']
    },
    {
        'priority': 100,
        'destination': 'Samples/Drums/Snares',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['snare']
    },
    {
        'priority': 101,
        'destination': 'Samples/Drums/Claps',
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
        'destination': 'Samples/Drums/Cymbals/Hats',
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
        'priority': 50,
        'destination': 'Samples/Drums/Percussion/Unsorted',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['percussion']
    },
    {
        'priority': 50,
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

    # -- FX --


    # -- SYNTHS --
    # -- INSTRUMENTS --
    

    # -- SAMPLES: VOCALS --
    # The more specific rule for "vocal chops" has a higher priority.
    # A file named "Vocal Chop 1.wav" will match both vocal rules, but this one will win.
    {
        'priority': 10,
        'destination': 'Samples/Vocals/Chops',
        'extensions': ['.wav', '.mp3'],
        'keywords': ['vocal', 'chop']
    },
    # The general "vocal" rule has a lower priority.
    {
        'priority': 5,
        'destination': 'Samples/Vocals/One Shots',
        'extensions': ['.wav', '.mp3'],
        'keywords': ['vocal']
    },
]

