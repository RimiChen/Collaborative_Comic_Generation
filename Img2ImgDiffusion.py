### import libraries

# import inspect
# import warnings

from typing import List, Optional, Union
import torch
from torch import autocast
from tqdm.auto import tqdm

from diffusers import StableDiffusionImg2ImgPipeline

import requests
from io import BytesIO
from PIL import Image

import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
from diffusers import LMSDiscreteScheduler
from diffusers import PNDMScheduler


class Img2ImgDiffusion():
    def __init__(self, model_name):
        self.model_name = model_name

        prompt = "only need one character, trending on artstation, children will like it, no background"
        # when using a lower value for `strength`, the generated image is more closer to the original `init_image`
        strength = 0.75
        guidance_scale = 7.5

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
    
    ### set parameters
    def changeParameters(self, prompt, strength, guidance_scale):
        self.prompt = prompt
        self.strength = strength
        self. guidance_scale = guidance_scale
    
    ### define test
    def testMethod(self):
        print('Import: ', self.model_name)
        print("Testing the Image diffusion")
        # processing the image
        image_path = "https://raw.githubusercontent.com/CompVis/stable-diffusion/main/assets/stable-samples/img2img/sketch-mountains-input.jpg"
        img_width = 768
        img_height = 512
        init_img = self.url_str2PIL_Image(image_path, img_width, img_height)   
        result_1 = self.diffusion_function(init_img)
        print("show result 1")
        plt.imshow(result_1)
        plt.show()



# ### Main starting point
# if __name__ == "__main__":
 

#     print("Testing the diffution mdoel: Stable diffusion")
    
#     prompt = "only need one character, trending on artstation, children will like it, no background"
#     # when using a lower value for `strength`, the generated image is more closer to the original `init_image`
#     strength = 0.75
#     guidance_scale = 7.5

#     diffuser = Img2ImgDiffuser(prompt, strength, guidance_scale)
 
#      # processing the image
#     image_path = "https://raw.githubusercontent.com/CompVis/stable-diffusion/main/assets/stable-samples/img2img/sketch-mountains-input.jpg"
#     img_width = 768
#     img_height = 512
#     init_img = diffuser.url_str2PIL_Image(image_path, img_width, img_height)    
    
#     # show original image
#     plt.imshow(init_img)
#     plt.show()

#     result_1 = diffuser.diffusion_function(init_img)
#     print("show result 1")
#     plt.imshow(result_1)
#     plt.show()


#     result_2 = diffuser.diffusion_with_LMSDiscreteScheduler(init_img)
#     print("show result 2")
#     plt.imshow(result_2)
#     plt.show()