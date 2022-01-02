import spleeter
from spleeter.separator import Separator
from spleeter.audio import Codec
# file = Audio(input_file)
files = [
    "inputs/02 Gasoline.mp3",
    "inputs/03 Give Me The Meltdown.mp3",
    "inputs/05 Mockingbird.mp3"
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