'''import os
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from lyzr import LyzrClient
#from lyzr import VoiceBot

app = Flask(__name__)
app.secret_key = 'your_secret_key'
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp3'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

lyzr_client = LyzrClient(api_key='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')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Transcribe the audio file using the Lyzr AI API
        transcription = lyzr_client.transcribe_audio(file_path)
        flash(f'Transcription: {transcription}')
        os.remove(file_path)  # Remove the file after transcription
        
        #vb=VoiceBot(api_key="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")
        #transcript=vb.transcribe(file_path)
        #flash(f'Transcription: {transcription}')
        flash('File uploaded and transcribed successfully')
    else:
        flash('Only MP3 files are allowed')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)






import os
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from lyzr import VoiceBot
from openai import OpenAI
#client = OpenAI()

api_key = "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"
openai.api_key = api_key

app = Flask(__name__)
app.secret_key = 'your_secret_key'
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp3'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#vb = VoiceBot(api_key='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')  # Initialize VoiceBot with your Lyzr API key

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        transcription = client.audio.transcriptions.create(model="whisper-1", file=file_path)
        print(transcription.text)

        # Transcribe the audio file using the VoiceBot
        transcription = vb.transcribe(file_path)
        flash(f'Transcription: {transcription}')
        os.remove(file_path)  # Remove the file after transcription
        flash('File uploaded and transcribed successfully')
    else:
        flash('Only MP3 files are allowed')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)




import os
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from openai import OpenAI

app = Flask(__name__)
app.secret_key = 'your_secret_key'
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp3'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

OpenAI.api_key = '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'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Transcribe the audio file using the OpenAI API
        with open(file_path, "rb") as audio_file:
            response = OpenAI().ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Transcribe the audio file"},
                    {"role": "user", "content": "Transcribe the audio file", "media": audio_file.read().hex()}
                ]
            )

            transcription = response["choices"][0]["message"]["content"]
            flash(f'Transcription: {transcription}')
        os.remove(file_path)  # Remove the file after transcription
        flash('File uploaded and transcribed successfully')
    else:
        flash('Only MP3 files are allowed')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


import os
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from pydub import AudioSegment

from pydub import AudioSegment

# Specify the path to ffmpeg executable
#ffmpeg_path = "C:\\ffmpeg\\bin\\ffmpeg.exe"
#AudioSegment.converter = ffmpeg_path

app = Flask(__name__)
app.secret_key = b'8\x1e\x1b\x99\xd84\xcc\x1a\x01PS`\xd0\xd4[x4\xc4m\x9c\x0eJ\xa7\xf5'
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp3'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        
        # Convert the MP3 file to WAV format
        wav_file_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{filename.split('.')[0]}.wav")
        audio = AudioSegment.from_mp3(file_path)
        audio.export(wav_file_path, format="wav")
        
        # Perform further processing on the WAV file as needed
        
        flash('File uploaded and processed successfully')
    else:
        flash('Only MP3 files are allowed')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)





import os
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
import openai
from pydub import AudioSegment

app = Flask(__name__)
app.secret_key = 'your_secret_key'
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp3'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

openai.api_key = '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'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Convert the audio file to WAV format
        audio = AudioSegment.from_mp3(file_path)
        wav_file_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{filename.rsplit('.', 1)[0]}.wav")
        audio.export(wav_file_path, format="wav")

        # Transcribe the audio file using the OpenAI API
        with open(wav_file_path, "rb") as audio_file:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Transcribe the audio file"},
                    {"role": "user", "content": "Transcribe the audio file", "media": audio_file.read().hex()}
                ]
            )

            transcription = response["choices"][0]["message"]["content"]
            flash(f'Transcription: {transcription}')

        os.remove(file_path)  # Remove the MP3 file
        os.remove(wav_file_path)  # Remove the WAV file
        flash('File uploaded and transcribed successfully')
    else:
        flash('Only MP3 files are allowed')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)




import os
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
import speech_recognition as sr

app = Flask(__name__)
app.secret_key = 'your_secret_key'
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp3'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Transcribe the audio file using the SpeechRecognition library
        recognizer = sr.Recognizer()
        with sr.AudioFile(file_path) as audio_file:
            audio_data = recognizer.record(audio_file)  # Read the entire audio file
            transcription = recognizer.recognize_google(audio_data)
            flash(f'Transcription: {transcription}')
        
        os.remove(file_path)  # Remove the file after transcription
        flash('File uploaded and transcribed successfully')
    else:
        flash('Only MP3 files are allowed')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)'''





import os
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from pocketsphinx import pocketsphinx, Jsgf, FsgModel

app = Flask(__name__)
app.secret_key = b'8\x1e\x1b\x99\xd84\xcc\x1a\x01PS`\xd0\xd4[x4\xc4m\x9c\x0eJ\xa7\xf5'
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp3'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Transcribe the audio file using Pocketsphinx
        config = pocketsphinx.Decoder.default_config()
        config.set_string('-hmm', 'en-us')
        config.set_string('-lm', 'en-us.lm.bin')
        config.set_string('-dict', 'en-us.dic')
        decoder = pocketsphinx.Decoder(config)

        with open(file_path, 'rb') as audio_file:
            decoder.start_utt()
            while True:
                buf = audio_file.read(1024)
                if buf:
                    decoder.process_raw(buf, False, False)
                else:
                    break
            decoder.end_utt()
            transcription = decoder.hyp().hypstr
        
        flash(f'Transcription: {transcription}')
        os.remove(file_path)  # Remove the file after transcription
        flash('File uploaded and transcribed successfully')
    else:
        flash('Only MP3 files are allowed')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

