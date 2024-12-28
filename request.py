import fal_client
import json
import requests

def on_queue_update(update):
    if isinstance(update, fal_client.InProgress):
        for log in update.logs:
           print(log["message"])

result = fal_client.subscribe(
    "fal-ai/flux-lora",
    arguments={
        "prompt": "A elegant female ballet dancer in a white tutu and pointe shoes, performing an arabesque pose in a grand theater. Her hair is in a perfect bun, and her makeup is stage-ready. She’s gracefully holding a delicate, swan-shaped card with “/u/PirouettePrincess” written in flowing script. The rich red velvet curtains and ornate gold decorations of the theater create a luxurious backdrop."
    },
    with_logs=True,
    on_queue_update=on_queue_update,
)

print(json.dumps(result, indent=4))


# Extract image URL
image_url = result['images'][0]['url']

# Download the image
response = requests.get(image_url)
if response.status_code == 200:
    with open('downloaded_image.jpg', 'wb') as f:
        f.write(response.content)
    print('Image downloaded successfully.')
else:
    print('Failed to download image.')