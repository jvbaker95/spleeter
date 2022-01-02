from spleeter.separator import Separator
input_file = "inputs/02 She's So Mean.mp3"
# file = Audio(input_file)

separator = Separator(
    params_descriptor="configs/2stems/base_config.json",
    multiprocess=False
)

separator.separate_to_file(
    audio_descriptor=input_file,
    destination="outputs/"
)
