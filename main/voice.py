from google.cloud import texttospeech
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
    'C:/Users/acer/Downloads/MunishProject02111999-c479c6303f5e.json')

scoped_credentials = credentials.with_scopes(
    ['https://www.googleapis.com/auth/cloud-platform'])


client = texttospeech.TextToSpeechClient(credentials=credentials)


synthesis_input = texttospeech.types.SynthesisInput(text="Hello, MUNISH!")

voice = texttospeech.types.VoiceSelectionParams(
    language_code='en-IN',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

# Select the type of audio file you want returned
audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(synthesis_input, voice, audio_config)

# The response's audio_content is binary.
with open('output.mp3', 'wb') as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')