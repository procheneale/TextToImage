# TextToImage Generator

TextToImage Generator is a simple image generator built using Stable Diffusion and Diffusers

## Goal

I want to create a web service that allows clients to generate an image based off of text. Clients would send an API call to the service, and the service would generate the image and upload it to their S3 storage. This solution leverages Stable Diffusion and Diffusers for the image generating model. Currently, this implementation is designed to run locally on an Apple M1 machine. Further advanced design changes may be made to allow the model to run on other platforms.

## Features

- Generate image based on text typed on terminal
- Uploads generated image onto S3 bucket and local device

## Tech

TextToImage uses the following open source projects to work properly:

- [Diffusers](https://github.com/huggingface/diffusers) - provides pretrained diffusion models across multiple modalities, such as vision and audio, and serves as a modular toolbox for inference and training of diffusion models.
- [Stable Diffusion](https://github.com/CompVis/stable-diffusion) - is a latent text-to-image diffusion model

## Installation

Recommended to use a virtual environment
```sh
$ git clone https://github.com/procheneale/TextToImage.git
$ cd TextToImage
$ source env/bin/activate
(<env_name>)$ pip install -r requirements.txt
```

## Configurations

To use the upload to S3 feature, please uncomment lines 34, 39, and 40 and input bucket name. (Note: Bucket should have generatedImages/ folder)
```
#bucketName = ""
    #    s3 = boto3.resource('s3')
    #    s3.meta.client.upload_file(folderName + "/" + imgString + ".png", bucketName, imgString + ".png")
```

Additionally, please ensure the AWS CLI has [programmatic access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) and S3 has the proper [permissions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html).

## Running
```sh
python textToImage.py
```
At some point, you will receive a prompt to input [Hugging Face Access token](https://huggingface.co/docs/hub/security-tokens). (Note: A Hugging Face account must be made and create a Hugging Face Access token)

## Demo
[![Text To Image Generator](https://www.youtube.com/watch?v=3S6sABBbmZE/0.jpg)](https://www.youtube.com/watch?v=3S6sABBbmZE "Text To Image Generator")

## System Design (For full implementation)
![Screenshot](SystemDesign.png)
