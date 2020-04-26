from google.cloud import speech_v1p1beta1
from google.cloud.speech_v1p1beta1 import enums


def sample_recognize(file_name):
    storage_uri = 'gs://mbothox-audio-files/' + file_name

    # The language of the supplied audio
    language_code = "fr-FR"

    # Sample rate in Hertz of the audio data sent
    sample_rate_hertz = 44100

    # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats.
    encoding = enums.RecognitionConfig.AudioEncoding.MP3

    config = {
        "language_code": language_code,
        "sample_rate_hertz": sample_rate_hertz,
        "encoding": encoding,
    }

    audio = {"uri": storage_uri}

    client = speech_v1p1beta1.SpeechClient()

    operation = client.long_running_recognize(config=config, audio=audio)

    print("Launched trnascription of " + file_name)

    op_result = operation.result()

    file_name_without_extension = file_name.split('.')[0]

    output_file_name = file_name_without_extension + '.txt'

    f = open('./' + output_file_name, "a")

    for result in op_result.results:
        for alternative in result.alternatives:
            f.writelines(alternative.transcript)
            f.writelines('\n' + '=' * 20 + '\n')
    f.close()
    print("Wrote transcription to " + output_file_name)


sample_recognize(file_name='')
