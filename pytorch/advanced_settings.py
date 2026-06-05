import neuralnode as nn

# Load the standard Horus Lens 1.0 model
model = nn.HorusLensModel(
    model_id="tokenaii/Horus-Lens-1.0"
).load()

# Generate image with custom advanced settings:
# - width & height: custom dimensions
# - num_inference_steps: number of denoising steps
# - guidance_scale: classifier-free guidance scale (CFG)
# - seed: random seed for reproducible results
print("Generating image with custom settings...")
model.generate_image(
    prompt="A peaceful cottage in the woods, cinematic lighting, autumn colors",
    output_path="outputs/cottage_advanced.png",
    width=512,
    height=512,
    num_inference_steps=25,
    guidance_scale=8.0,
    seed=1337
)

print("Saved generated image to outputs/cottage_advanced.png")
