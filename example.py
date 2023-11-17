# winget install ffmpeg
import spleeter
from spleeter import audio
from spleeter.separator import Separator
from spleeter.audio import Codec
from pathlib import Path
# file = audio(input_file)
# files = [str(i) for i in Path("inputs").iterdir()]
files = [
    str(Path("inputs/05 Girl Like That (LP Version).mp3"))
]
separator = Separator(
    params_descriptor="configs/2stems/base_config.json",
    multiprocess=False
)

for file in files:
    separator.separate_to_file(
        audio_descriptor=file,
        destination="outputs/",
        codec=Codec.MP3
    )