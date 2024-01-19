#!/usr/bin/env python3
import sys

from app.midi_player import play
sys.path.append('compilers')
sys.path.append('app')
from midiutil import MIDIFile
from compilers.track_compiler import *


def generate_midi_file(music_ml_meta, music_ml_model, ml_file_name):
    # Create the MIDIFile Object
    track_number = len(music_ml_model.tracks)
    if music_ml_model.ticksPerQuarterNote != 0:
        midi_file = MIDIFile(track_number, eventtime_is_ticks=True,
                             ticks_per_quarternote=music_ml_model.ticksPerQuarterNote)
    else:
        midi_file = MIDIFile(track_number, eventtime_is_ticks=True)
    for i, track in enumerate(music_ml_model.tracks):
        midi_file.addTempo(i, 0, music_ml_model.defaultTempo)
        for tempo in music_ml_model.tempos:
            position = position_in_ticks(music_ml_model, music_ml_meta, midi_file, tempo.position)
            midi_file.addTempo(i, position, tempo.value)
        midi_file.addTimeSignature(i, 0, music_ml_model.defaultTimeSignature.numerator,
                                   music_ml_model.defaultTimeSignature.denominator, 24, 8)
        for time_signature in music_ml_model.timeSignatures:
            position = bar_position_in_ticks(music_ml_model, midi_file, time_signature.bar)
            midi_file.addTimeSignature(i, position, time_signature.numerator,
                                       time_signature.denominator, 24, 8)
        compile_track(music_ml_model, music_ml_meta, track, midi_file, i)

    bin_file = open(ml_file_name + '.mid', 'wb')
    midi_file.writeFile(bin_file)
    bin_file.close()

    if music_ml_model.live == 'on':
        play(ml_file_name)
