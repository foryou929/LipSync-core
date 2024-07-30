# LipSync

## Install on ubuntu 

### Construct python virtual environment

`sudo apt install python3.8-venv`

`python3 -m venv env`

### Install python modules

`pip install -r requirements.txt`

### Correct following file

Open `./env/lib/python3.8/site-packages/basicsr/data/degradations.py` and on line 8, simply change:

from

```
from torchvision.transforms.functional_tensor import rgb_to_grayscale
```

to

```
from torchvision.transforms.functional import rgb_to_grayscale
```

### Run install.py

`python install.py`

### Install ffmpeg

`sudo apt-get install ffmpeg`

### Run run.py

```
python run.py -video_file YOUR_VIDEO_FILE -vocal_file YOUR_VOICE_FILE -output_file YOUR_OUTPUT_FILE
```
