import eel
import os

eel.init('web')

MUSIC_EXTENSIONS = ('.mp3', '.wav', '.ogg')

@eel.expose
def get_music_files(folder_path):
    files = []
    try:
        for file in os.listdir(folder_path):
            if file.endswith(MUSIC_EXTENSIONS):
                files.append({
                    "name": file,
                    "path": os.path.join(folder_path, file)
                })
    except Exception as e:
        return {"error": str(e)}

    return files


@eel.expose
def open_file(path):
    # Just returns path for frontend audio
    return path


if __name__ == "__main__":
    eel.start('index.html', size=(1000, 700))