version = 'v1.0'

import os
from enhance import load_sr
from easy_functions import load_file_from_url, load_model, load_predictor

working_directory = os.getcwd()

# Download and initialize both wav2lip models
print("Downloading wav2lip essentials")

load_file_from_url(
    url="https://github.com/foryou929/LipSync-core/releases/download/1.0/Wav2Lip_GAN.pth",
    model_dir="checkpoints",
    progress=True,
    file_name="Wav2Lip_GAN.pth",
)
model = load_model(os.path.join(working_directory, "checkpoints", "Wav2Lip_GAN.pth"))
print("Wav2lip_gan loaded")

load_file_from_url(
    url="https://github.com/foryou929/LipSync-core/releases/download/1.0/Wav2Lip.pth",
    model_dir="checkpoints",
    progress=True,
    file_name="Wav2Lip.pth",
)
model = load_model(os.path.join(working_directory, "checkpoints", "Wav2Lip.pth"))
print("wav2lip loaded")

# download gfpgan files
print("Downloading gfpgan essentials")
load_file_from_url(
    url="https://github.com/foryou929/LipSync-core/releases/download/1.0/GFPGANv1.4.pth",
    model_dir="checkpoints",
    progress=True,
    file_name="GFPGANv1.4.pth",
)
load_sr()

# load face detectors
print("Initializing face detectors")
load_file_from_url(
    url="https://github.com/foryou929/LipSync-core/releases/download/1.0/shape_predictor_68_face_landmarks_GTX.dat",
    model_dir="checkpoints",
    progress=True,
    file_name="shape_predictor_68_face_landmarks_GTX.dat",
)

load_predictor()

# write a file to signify setup is done
with open("installed.txt", "w") as f:
    f.write(version)
print("Installation complete!")
