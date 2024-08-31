### import libraries

# import inspect
# import warnings

from typing import List, Optional, Union
import torch
from torch import autocast
from tqdm.auto import tqdm
import os
from rembg import remove 
from PIL import Image 

from diffusers import StableDiffusionImg2ImgPipeline

import requests
from io import BytesIO
from PIL import Image

import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
from diffusers import LMSDiscreteScheduler
from diffusers import PNDMScheduler


class Img2ImgDiffuser():
    def __init__(self, prompt, strength, guidance_scale):
        # self.init_img = init_img
        self.prompt = prompt
        self.strength = strength
        self.guidance_scale = guidance_scale
        
        self.device = "cuda"
        model_path = "CompVis/stable-diffusion-v1-4"

        self.pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
            model_path,
            revision="fp16",
            torch_dtype=torch.float16,
            use_auth_token=True
        )
        self.generator = torch.Generator(device=self.device).manual_seed(1024)
        self.pipe = self.pipe.to(self.device)


    # difussor using default scheduler
    def diffusion_function(self, init_img):

        pndm = PNDMScheduler(beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear")
        self.pipe.schedular = pndm

        with autocast("cuda"):
            # image = pipe(prompt=prompt, image=init_img, strength=0.75, guidance_scale=7.5, generator=generator).images[0]
            new_img = self.pipe(prompt=self.prompt, image=init_img, strength=self.strength, guidance_scale=self.guidance_scale, generator=self.generator).images[0]

        return new_img
    
    ## difussor using LMSDiscreteScheduler
    def diffusion_with_LMSDiscreteScheduler(self, init_img):
        lms = LMSDiscreteScheduler(beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear")
        self.pipe.scheduler = lms

        with autocast("cuda"):
            init_img = self.pipe(prompt=prompt, image=init_img, strength=0.75, guidance_scale=7.5, generator=self.generator).images[0]       

        return init_img

    # from url to PIL.Image
    def url_str2PIL_Image(self, image_path, width, height):
        response = requests.get(image_path)
        init_img = Image.open(BytesIO(response.content)).convert("RGB")
        init_img = init_img.resize((width, height))

        return init_img

    def local_str2PIL_Image(self, image_path, width, height):
        img = Image.open(r""+image_path).convert("RGB")       
        init_img = img.resize((width, height))
        # print(type(init_img))

        # plt.imshow(init_img)
        # plt.show()

        return init_img
    
    def remove_back_path(self, img_path):
        img = Image.open(r""+image_path).convert("RGB") 
        output = remove(img)  
        return output
    
    def remove_back_img(self, img):
        output = remove(img)  
        return output
### Main starting point
if __name__ == "__main__":
 

    print("Testing the diffution mdoel: Stable diffusion")
    
    prompt = "only need one character, trending on artstation, children will like it, no background"
    # when using a lower value for `strength`, the generated image is more closer to the original `init_image`
    strength = 0.75
    guidance_scale = 7.5

    diffuser = Img2ImgDiffuser(prompt, strength, guidance_scale)
 
     # processing the image
    image_path = "https://raw.githubusercontent.com/CompVis/stable-diffusion/main/assets/stable-samples/img2img/sketch-mountains-input.jpg"
    img_width = 768
    img_height = 512
    init_img = diffuser.url_str2PIL_Image(image_path, img_width, img_height)    
    
    # show original image
    plt.imshow(init_img)
    plt.show()

    # prompt = "new scenary with similar painting style"
    # result_1 = diffuser.diffusion_function(init_img)
    # print("show result 1")
    # plt.imshow(result_1)
    # plt.show()


    # result_2 = diffuser.diffusion_with_LMSDiscreteScheduler(init_img)
    # print("show result 2")
    # plt.imshow(result_2)
    # plt.show()

    local_img_path = "images/Einstein.jpg"

    if os.path.isfile(local_img_path):
        print("File exist!")
    else:
        print("File not exist!")
    chara_img = diffuser.local_str2PIL_Image(local_img_path, img_width, img_height)
    prompt = "only need one character, trending on artstation, children will like it, no background"
    result_3 = diffuser.diffusion_with_LMSDiscreteScheduler(chara_img)
    print("show result 3")
    plt.imshow(result_3)
    plt.show() 

    output = diffuser.remove_back_img(result_3)  
    outpath = "images/Einstein_diffused_noback.png"
    output.save(outpath) 


    back_img_path = "images/back.png"

    if os.path.isfile(back_img_path):
        print("File exist!")
    else:
        print("File not exist!")

    back_img = diffuser.local_str2PIL_Image(back_img_path, img_width, img_height)
    plt.imshow(back_img)
    plt.show() 
    prompt = "new scenary with similar painting style"
    result_4 = diffuser.diffusion_function(back_img)
    print("show result 4")
    plt.imshow(result_4)
    plt.show() 
    # output2 = diffuser.remove_back_img(result_3)  
    outpath2 = "images/new_back_diffused.png"
    result_4.save(outpath2) 