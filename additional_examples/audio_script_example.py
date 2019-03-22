from google.cloud import texttospeech
import os,glob
import json
import shutil
from xlrd import open_workbook


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/opt/course/ozmar_test1/" \
                                               "utils/texto_voz.json"
client = texttospeech.TextToSpeechClient()
VOICE_CONFIG = "/opt/course/pythoncourse/additional_examples/utils/voices.json"


def get_voice_config():
    try:
        with open(VOICE_CONFIG, 'r') as _file:
            return json.load(_file)
    except Exception as e:
        print(f"Couldn't open the voice setting file in {VOICE_CONFIG} "
              f"because of {e}")
        raise Exception("Program execution has stopped")


def get_ssml_gender(gender):
    if gender == "MALE":
        return texttospeech.enums.SsmlVoiceGender.FEMALE
    else:
        return texttospeech.enums.SsmlVoiceGender.MALE


def list_voices():
    """Lists the available voices."""
    voices = client.list_voices()

    for voice in voices.voices:
        print('Name: {}'.format(voice.name))
        for language_code in voice.language_codes:
            print('Supported language: {}'.format(language_code))
        ssml_voice_genders = ['SSML_VOICE_GENDER_UNSPECIFIED', 'MALE',
                              'FEMALE', 'NEUTRAL']
        print('SSML Voice Gender: {}'.format(
            ssml_voice_genders[voice.ssml_gender]))
        print('Natural Sample Rate Hertz: {}\n'.format(
            voice.natural_sample_rate_hertz))


def create_file(output_path, output_file, data):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    file_path = output_path + "/" + output_file
    with open(file_path, 'wb') as out:
        out.write(data)


def process_audio(text, language):
    voice_config = get_voice_config()
    input_text = texttospeech.types.SynthesisInput(text=text)
    ssml_gender = get_ssml_gender(voice_config[language].
                                  get("SSML Voice Gender"))
    voice = texttospeech.types.VoiceSelectionParams(
        name=voice_config[language].get("Name"),
        language_code=voice_config[language].get("Supported language"),
        ssml_gender=ssml_gender)
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)
    return client.synthesize_speech(input_text, voice, audio_config)


def synthesize_text(project, single_audio="", lng="espanol", removefiles=False):
    """Synthesizes speech from the input string of text."""
    input_path = f"/var/opt/test/{project}"
    output_path = f"{input_path}/output"
    if removefiles:
        files_to_remove = os.listdir(output_path)
        for file in files_to_remove:
            if file.endswith(".mp3"):
                os.remove(os.path.join(output_path, file))
    if single_audio:
        response = process_audio(single_audio, lng)
        create_file(output_path, f"{project}_single_audio_file.mp3",
                    response.audio_content)
        print("File created")
        exit()
    os.chdir(input_path)
    input_file = glob.glob("*.xls")[0]
    old_slide = 0
    sub_slide = 1
    if not input_file:
        print(f'No input file was found in project folder {project_name}')
        exit()
    wb = open_workbook(input_path+"/"+input_file)
    for sheet in wb.sheets():
        for row in range(0, sheet.nrows):
            if sheet.ncols == 2:
                slide = int(sheet.cell(row, 0).value)
                if old_slide == slide:
                    sub_slide += 1
                else:
                    sub_slide = 1
                old_slide = slide
                text = sheet.cell(row, 1).value
                output_file = f"S_{slide}_audio{sub_slide}.mp3"
                response = process_audio(text, lng)
                # The response's audio_content is binary.
                create_file(output_path, output_file, response.audio_content)
            else:
                print("More than 2 columns detected in input file, "
                      "stopping execution")
                exit()
    shutil.make_archive(f"{project}_audiofiles", 'zip', output_path)
    print(f"Zip file created")


if __name__ == '__main__':
    # language can be: español, ingles1, ingles2
    project_name = "my_project"
    single_audio = ""
    synthesize_text(project_name, single_audio, removefiles=False)
