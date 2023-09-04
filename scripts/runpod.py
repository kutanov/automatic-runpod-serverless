import modules.scripts as scripts
import gradio as gr
import runpod
import os
import aiohttp
import asyncio
import ujson

def handler(event):
        with aiohttp.ClientSession() as session:
                request = session.post('http://localhost:3000/sdapi/v1/txt2img', json=event.input)
                return request



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
