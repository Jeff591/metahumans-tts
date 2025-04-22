import json

# Transcript JSON file
transcript_file = "Robin_20250402_A.json"

# Output metadata file
metadata_file = "formatted_data.txt"

# Load transcript JSON
with open(transcript_file, 'r', encoding='utf-8') as file:
    transcript = json.load(file)

# Write metadata
with open(metadata_file, mode='w', encoding='utf-8') as file:
    for segment in transcript['segments']:
        audio_id = segment['id'] + 1
        text = segment['text'].strip()
        file.write(f"audio{audio_id}|{text}|{text}\n")

print(f"metadata.txt saved to {metadata_file}")
