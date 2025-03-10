# Transcribe Audio Files with Python by AssemblyAI AND Delete Audio Files on AssemblyAI.

import requests
import assemblyai as aai
from api_secrets import API_KEY_ASSEMBLYAI
import sys
from datetime import date

aai.settings.api_key = API_KEY_ASSEMBLYAI
filename  = sys.argv[1]

OUTPUT_FILENAME = str(date.today())+" .txt"
 
config = aai.TranscriptionConfig(
    punctuate = True,
    format_text = True
)

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(filename, config)
# print(transcript.text)
print(transcript.id)

if OUTPUT_FILENAME:
    with open(OUTPUT_FILENAME, "w") as file:
            file.write(transcript.text)
else:
    print(transcript.text)

# Delete transcript (DELETE /v2/transcript/:transcript_id)
response = requests.delete(
  "https://api.assemblyai.com/v2/transcript/"+transcript.id,
  headers={
    "Authorization": API_KEY_ASSEMBLYAI
  },
)
