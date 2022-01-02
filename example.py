import spleeter
from spleeter.separator import Separator
from spleeter.audio import Codec
from pathlib import Path
# file = Audio(input_file)
files = [str(i) for i in Path("inputs").iterdir()]
# files = [
#     str(Path("inputs/12 Heart Of The World.mp3"))
# ]
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