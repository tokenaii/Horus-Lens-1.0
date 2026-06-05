import torch
import neuralnode as nn

# Load the standard Horus Lens 1.0 model in float16 (half) precision
# This is highly recommended to save GPU memory (VRAM)
print("Loading model in fp16 precision...")
model = nn.HorusLensModel(
    model_id="tokenaii/Horus-Lens-1.0",
    torch_dtype=torch.float16
).load()

# Generate the image
print("Generating image in fp16...")
model.generate_image(
    prompt="A serene lake reflecting mountains at sunset, realistic, oil painting style",
    output_path="outputs/fp16_sunset.png",
    seed=999
)

print("Saved generated image to outputs/fp16_sunset.png")
