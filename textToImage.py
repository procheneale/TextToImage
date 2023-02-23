import logging
import boto3
from botocore.exceptions import ClientError
import os
from PIL import Image, ImageDraw
import cv2
import numpy as np
from IPython.display import HTML
from base64 import b64encode

import torch
from torch import autocast
from torch.nn import functional as F
from diffusers import StableDiffusionPipeline, AutoencoderKL
from diffusers import UNet2DConditionModel, PNDMScheduler, LMSDiscreteScheduler
from diffusers.schedulers.scheduling_ddim import DDIMScheduler
from transformers import CLIPTextModel, CLIPTokenizer
from tqdm.auto import tqdm
from diffusers import StableDiffusionPipeline


def generateImage(prompt):
    pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
    pipe = pipe.to("mps")
    pipe.enable_attention_slicing()
    _ = pipe(prompt, num_inference_steps=1)
    image = pipe(prompt).images[0]
    image.save(f"generatedImages/" + prompt + ".png")
    print("Done Processing")

def main():
    imgString = input("Type an image to be generated: ")
    folderName = "generatedImages"
    #bucketName = ""
    if not os.path.exists(folderName):
        os.makedirs(folderName)
    if not os.path.exists(folderName + "/" + imgString + ".png"):
        generateImage(imgString)
    #    s3 = boto3.resource('s3')
    #    s3.meta.client.upload_file(folderName + "/" + imgString + ".png", bucketName, imgString + ".png")
    else:
        print("Image already generated")

if __name__ == "__main__":
    main()
