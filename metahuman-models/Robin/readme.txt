Audio Segmentation with Whisper and Python

---

Step 1: Convert Video to Text Transcript Using Whisper

Use Whisper in the terminal to transcribe the video and generate a JSON file containing the text transcript:

whisper "C:\Users\cyberarch30\Downloads\Robin_20250402_A.mp4" --model medium --language en --task transcribe --output_format json --output_dir .

- This will generate a JSON file in the same directory as the video file.

---

Step 2: Segment Audio Based on Transcript

Now, run the Python script to split the audio from the video according to the timestamps in the transcript JSON file:

python segment_audio.py path_to_audio.mp3 path_to_transcripts.json

- Replace path_to_audio.mp3 with the path to your audio file.
- Replace path_to_transcripts.json with the path to the Whisper-generated JSON transcript.
