import modules.scripts as scripts
import gradio as gr
import runpod
import os

from modules import images, script_callbacks
from modules.processing import process_images, Processed
from modules.processing import Processed
from modules.shared import opts, cmd_opts, state

from modules.api.api import img2imgapi

def handler(event):
        return img2imgapi(event.input)


class RunPodServerlessScript(scripts.Script):
        # Extension title in menu UI
        def title(self):
                return "RunPodServerless"

        def show(self, is_img2img):
                return scripts.AlwaysVisible
        
        
        def on_app_started(self, block):
                runpod.serverless.start({
                        "handler": self.handler
                })
