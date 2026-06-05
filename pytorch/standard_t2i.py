import neuralnode as nn

# Initialize the standard Horus Lens 1.0 text-to-image model
# This loads the full weights from Hugging Face Hub (tokenaii/Horus-Lens-1.0)
model = nn.HorusLensModel(
    model_id="tokenaii/Horus-Lens-1.0"
).load()

# Generate the image
print("Generating image using standard model...")
model.generate_image(
    prompt="A futuristic city with flying cars, neon lights, highly detailed, 4k",
    output_path="outputs/standard_city.png"
)

print("Saved generated image to outputs/standard_city.png")
