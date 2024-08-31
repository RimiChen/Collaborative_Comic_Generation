#!/usr/bin/env python
# coding: utf-8

# In[10]:


#### diffusion model for image to image

### import libraries
# import inspect
# import warnings
# from typing import List, Optional, Union

import torch
from torch import autocast
# from tqdm.auto import tqdm

from diffusers import StableDiffusionImg2ImgPipeline
import requests
from io import BytesIO
from PIL import Image
from functools import singledispatch


# In[18]:


used_strength = 0.75
used_guidance_scale =7.5

### Stable diffusion model
class Img2ImgDiffuser():
    def __init__(self, used_strength, used_guidance_scale, used_prompt):
        self.used_strength = used_strength
        self.used_guidance_scale = used_guidance_scale

    
        device = "cuda"
        # load pretrained model
        model_path = "CompVis/stable-diffusion-v1-4"
        
        self.pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
            model_path,
            variant="fp16",
            torch_dtype=torch.float16,
            use_auth_token=True
        )
        self.pipe = self.pipe.to(device)  
        self.generator = torch.Generator(device=device).manual_seed(1024)
        self.prompt = used_prompt

        print("Diffuser initialized.")
        
    def stable_diffusion_model(self, img:str| Image.Image):
        print("you gave a image path")
        response = requests.get(img)
        init_img = Image.open(BytesIO(response.content)).convert("RGB")
        init_img = init_img.resize((64, 64))
        
        with autocast("cuda"):
            new_img = self.pipe(prompt = self.prompt, image=init_img, strength=self.used_strength, guidance_scale=self.used_guidance_scale, generator=self.generator).images[0]   
            new_img = new_img.resize((128, 128))
        return new_img        

    # @singledispatch
    # def stable_diffusion_model(self, img):
    #     pass
        
    # @stable_diffusion_model.register
    # def _(img: str):
    #     print("you gave a image path")
    #     response = requests.get(img)
    #     init_img = Image.open(BytesIO(response.content)).convert("RGB")
    #     init_img = init_img.resize((64, 64))
        
    #     with autocast("cuda"):
    #         new_img = self.pipe(prompt=prompt, image=init_img, strength=self.used_strength, guidance_scale=self.used_guidance_scale, generator=self.generator).images[0]   
    #         new_img = new_img.resize((128, 128))
    #     return new_img
        
    # @stable_diffusion_model.register
    # def _(img: Image.Image):
    #     init_img = img
    #     print("you gave a pillow image")
    #     self.img = img.resize((64, 64))
    #     with autocast("cuda"):
    #         new_img = self.pipe(prompt=prompt, image=init_img, strength=self.used_strength, guidance_scale=self.used_guidance_scale, generator=self.generator).images[0]  
    #         new_img = new_img.resize((128, 128))
    #     return new_img
            


# In[ ]:





# In[ ]:




