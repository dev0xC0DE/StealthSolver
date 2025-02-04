# src/chat.py
"""This module provides a function for sending an image and prompt to an AI model for chat completion."""

import os
import asyncio
import g4f
import g4f.Provider

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


def chat_completion(prompt, provider_name="Blackbox", media_folder="media"):
    """Sends an image and prompt to an AI model for chat completion."""
    provider_class = getattr(g4f.Provider, provider_name, None)
    client = g4f.Client(provider=provider_class)

    if not os.path.exists(media_folder):
        os.makedirs(media_folder)

    image_files = [
        [open(os.path.join(media_folder, filename), "rb"), filename]
        for filename in os.listdir(media_folder)
        if filename.endswith((".jpg", ".png", ".jpeg"))
    ]

    print(image_files)

    # Send the image and prompt to the default model from gpt4free
    response = client.chat.completions.create(
        messages=[{"content": prompt, "role": "user"}], model="", images=image_files
    )
    return response.choices[0].message.content
