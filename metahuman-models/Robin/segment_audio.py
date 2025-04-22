import argparse
import os
from pydub import AudioSegment
import json

def segment_audio(audio_file, json_file):
    # Load the Whisper JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Load the full audio file
    audio = AudioSegment.from_file(audio_file)

    # Create the 'wav' directory if it doesn't exist
    output_dir = 'wav'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate over the segments to slice the audio
    for i, segment in enumerate(data['segments']):
        start_time = segment['start'] * 1000  # Convert start time from seconds to milliseconds
        end_time = segment['end'] * 1000  # Convert end time from seconds to milliseconds
        
        # Extract the audio segment
        segment_audio = audio[start_time:end_time]
        
        # Save the audio segment as a .wav file in the 'wav' folder
        output_file = os.path.join(output_dir, f"audio_segment_{i+1}.wav")
        segment_audio.export(output_file, format="wav")
    
    print(f"Audio splitting is complete. All segments are saved in the '{output_dir}' folder.")

if __name__ == "__main__":
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Split audio into segments based on Whisper JSON.")
    parser.add_argument('audio_file', type=str, help="Path to the audio file (e.g., 'path_to_file.mp3')")
    parser.add_argument('json_file', type=str, help="Path to the Whisper JSON file (e.g., 'transcripts.json')")
    
    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the function to segment the audio
    segment_audio(args.audio_file, args.json_file)
