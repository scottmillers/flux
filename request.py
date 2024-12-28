import fal_client
import json
import requests
import sys

def on_queue_update(update):
    if isinstance(update, fal_client.InProgress):
        for log in update.logs:
           print(log["message"])

def generate_image(prompt):
    # Subscribe to the FAL AI service
    result = fal_client.subscribe(
        "fal-ai/flux-lora",
        arguments={
            "prompt": prompt
        },
        with_logs=True,
        on_queue_update=on_queue_update,
    )
    return result

def download_image(image_url, file_name):
    # Download the image
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(response.content)
        print('Image downloaded successfully.')
    else:
        print('Failed to download image.')



if len(sys.argv) > 2:
    prompt = sys.argv[1]
    print(f"Received prompt: {prompt}")
    filename = sys.argv[2]
    print(f"Received filename: {filename}")
else:
    print("No input received.")
    sys.exit(1)


#prompt = "A elegant female ballet dancer in a white tutu and pointe shoes, performing an arabesque pose in a grand theater. Her hair is in a perfect bun, and her makeup is stage-ready. She’s gracefully holding a delicate, swan-shaped card with “/u/PirouettePrincess” written in flowing script. The rich red velvet curtains and ornate gold decorations of the theater create a luxurious backdrop."
#filename = "downloaded_image.jpg"

result = generate_image(prompt)

print(json.dumps(result, indent=4))


# Extract image URL
image_url = result['images'][0]['url']


# Call the function with the image URL and desired file name
download_image(image_url, filename)