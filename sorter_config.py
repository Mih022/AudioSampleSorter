import os
import shutil

# ==============================================================================
# --- CONFIGURATION ---
# ==============================================================================

# 1. SET YOUR FOLDER PATHS
SOURCE_FOLDER = "D:\\mladi\\Documents\\FL relief"
TARGET_FOLDER = "D:\\mladi\\Documents\\FL relief sorted"

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

    # -- LOOPS --

    {
        'priority': 10,
        'destination': 'Samples/Loops/',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['loop']
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
        'keywords': ['ambiance', 'Hard Strikes']
    },
    {
        'priority': 90,
        'destination': 'Samples/FX/Ambiance/Pretty',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['ambiance', 'Pretty']
    },
    {
        'priority': 90,
        'destination': 'Samples/FX/Ambiance/Rain',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['ambiance', 'rain']
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
        'keywords': ['amb', 'Hard Strikes']
    },
    {
        'priority': 80,
        'destination': 'Samples/FX/Ambiance/Pretty',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['amb', 'Pretty']
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
        'priority': 50,
        'destination': 'Samples/FX/Sub Drops',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['Sub Drop']
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
        'keywords': ['sweep', 'Down', 'long'],
    },
    {
        'priority': 50,
        'destination': 'Samples/FX/Sweeps/Down/Short',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['sweep', 'Down', 'short'],
    },
    {
        'priority': 50,
        'destination': 'Samples/FX/Sweeps/Down/Medium',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['sweep', 'Down', 'medium'],
    },
    {
        'priority': 49,
        'destination': 'Samples/FX/Sweeps/Down/Other',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['sweep', 'Down'],
    },
    {
        'priority': 45,
        'destination': 'Samples/FX/Sweeps/Other',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['sweep']
    },

    {
        'priority': 50,
        'destination': 'Samples/FX/Tape Stops',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['Tape Stop']
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
        'keywords': ['War Horn']
    },
    {
        'priority': 50,
        'destination': 'Samples/FX/Water Drops',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['Water Drop']
    },
    {
        'priority': 10,
        'destination': 'Samples/FX/Zipties',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['Zip']
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
        'priority': 50,
        'destination': 'Samples/Instruments/Ethnic/Main',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['Bansuri']
    },
    {
        'priority': 50,
        'destination': 'Samples/Instruments/Ethnic/Main',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['Bayan']
    },
    {
        'priority': 50,
        'destination': 'Samples/Instruments/Ethnic/Main',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['Cura']
    },
    {
        'priority': 50,
        'destination': 'Samples/Instruments/Ethnic/Main',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['Duduk']
    },
    {
        'priority': 50,
        'destination': 'Samples/Instruments/Ethnic/Main',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['Harmonium']
    },
    {
        'priority': 10,
        'destination': 'Samples/Instruments/Ethnic/Main',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['Indian']
    },
    {
        'priority': 50,
        'destination': 'Samples/Instruments/Ethnic/Main',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['Kemenche']
    },
    {
        'priority': 10,
        'destination': 'Samples/Instruments/Ethnic/Main',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['Mey']
    },
    {
        'priority': 10,
        'destination': 'Samples/Instruments/Ethnic/Main',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['Morsing']
    },
    {
        'priority': 10,
        'destination': 'Samples/Instruments/Ethnic/Main',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['Ney']
    },
    {
        'priority': 10,
        'destination': 'Samples/Instruments/Ethnic/Main',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['Oud']
    },
    {
        'priority': 10,
        'destination': 'Samples/Instruments/Ethnic/Main',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['Santur']
    },
    {
        'priority': 10,
        'destination': 'Samples/Instruments/Ethnic/Main',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['Oud']
    },
    {
        'priority': 10,
        'destination': 'Samples/Instruments/Ethnic/Main',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['Swarmandal']
    },
    {
        'priority': 10,
        'destination': 'Samples/Instruments/Ethnic/Main',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['Tumbi']
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
        'destination': 'Samples/Synths/Synth Shots',
        'extensions': ['.wav', '.mp3', '.aif'],
        'keywords': ['synth', 'shot']
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
        'priority': 50,
        'destination': 'Samples/Vocals/Vocal Performance',
        'extensions': ['.wav', '.mp3'],
        'keywords': ['vox', 'adlib']
    },

]

