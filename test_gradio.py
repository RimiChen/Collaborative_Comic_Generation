#!/usr/bin/env python
# coding: utf-8

# In[35]:


import gradio as gr
import numpy as np
import matplotlib.pyplot as plt

HF_PATH = "/home/user/app/"
        

gr.set_static_paths(paths=["/images/"])


# In[36]:


def diffusion(input_img):
    # get the size of image
    # generate new ones by diffusion
    # remove background
    # resize to the original size
    ### testing code: sepia filer
    sepia_filter = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ])
    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    print(input_img.shape, sepia_img.shape)
    
    return sepia_img


# In[40]:


panel_number = 4
# image seqeucne
panel_list = []

with gr.Blocks() as demo:
    with gr.Row():
        
        with gr.Column():
            chara_1 = gr.Image(height = 100, width = 100)
            chara_2 = gr.Image(height = 100, width = 100)
            gr.Button(value = "+")

        
        with gr.Column():
            scene_1 = gr.Image(height = 100, width = 100)
            scene_2 = gr.Image(height = 100, width = 100)
            gr.Button(value = "+")

        with gr.Column():
            with gr.Row():
                # image seqeucne
                # for total_panel in range(panel_number):
                #     panel_list[total_panel].value = "images/panel_"+str(total_panel+1)+".png"
                for total_panel in range(panel_number):
                    image_path = "images/panel_"+str(total_panel+1)+".png"
                    print(image_path)
                    panel_list.append(gr.Image(value=image_path, height = 100, width = 100, type ="pil"))                    
         
            with gr.Row():
                with gr.Row():
                    gr.Label(value = "Nrrative Arc")
                    
                with gr.Row():
                    ### test with plot
                    plt.plot([1,2,3,4], [1,4,9,16], 'ro')
                    plt.axis([0, 6, 0, 20])
                    gr.Plot(value = plt)

        with gr.Column():
            with gr.Row():
                gr.Label(value = "AI suggestions")
                gr.Button(value = "Narrative Arc")
                gr.Button(value = "Panel Transition")
                gr.Button(value = "Composition")
                gr.Button(value = "Narrative Grammar")
                gr.Button(value = "Textboxes")
                gr.Button(value = "Customized icons")
                gr.Button(value = "+")

            with gr.Row():
                gr.Button(value = "Layout")
                
            
demo.launch()


# In[ ]:



