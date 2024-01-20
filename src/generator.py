#!/usr/bin/env python3
import sys

from app.midi_player import play

sys.path.append('compilers')
sys.path.append('app')
from midiutil import MIDIFile
from compilers.track_compiler import *
from compilers.section_compiler import *


def generate_midi_file(music_ml_meta, music_ml_model, ml_file_name):
    # Create the MIDIFile Object
    if textx_isinstance(music_ml_model.song, music_ml_meta['SingleSection']):
        track_number = len(music_ml_model.song.tracks)
    else:
        track_number = len(music_ml_model.song.trackNumber)
    if music_ml_model.ticksPerQuarterNote != 0:
        midi_file = MIDIFile(track_number, eventtime_is_ticks=True,
                             ticks_per_quarternote=music_ml_model.ticksPerQuarterNote)
    else:
        midi_file = MIDIFile(track_number, eventtime_is_ticks=True)

    if textx_isinstance(music_ml_model.song, music_ml_meta['SingleSection']):

        for i, track in enumerate(music_ml_model.song.tracks):
            compile_track(music_ml_model, music_ml_meta, track, midi_file, i)
    else:
        for i, trackDef in enumerate(music_ml_model.song.trackDefs):
            track_settings(midi_file, music_ml_model, music_ml_meta, trackDef,
                           track_number)
            program_number = instrument_program_number(trackDef.instrument)
            if program_number is None:
                raise TextXSemanticError('Instrument not found: ' + trackDef.instrument, **get_location(trackDef))
            channel = default_channel(trackDef.instrument)
            if trackDef.channel != 0:
                channel = trackDef.channel
            midi_file.addProgramChange(track_number, channel-1, 0, program_number)
        position = 0
        for arranged_section in music_ml_model.song.arrange:
            section = get_section(music_ml_model.song, arranged_section.name)
            position = compile_section(music_ml_model, music_ml_meta, section, midi_file, position)

    bin_file = open(ml_file_name + '.mid', 'wb')
    midi_file.writeFile(bin_file)
    bin_file.close()

    if music_ml_model.live == 'on':
        play(ml_file_name)


def get_section(song, name):
    section = None
    for section_def in song.sections:
        if section_def.name == name:
            section = section_def
            break
    if section is None:
        raise TextXSemanticError('Section not found: ' + name, **get_location(song))
    return section
