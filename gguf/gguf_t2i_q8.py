import neuralnode as nn

# Load the GGUF model with the Q8_0 quantization format
# Q8_0 offers higher image quality at the cost of larger file size and memory usage
print("Loading Horus Lens GGUF Q8_0 model...")
model = nn.HorusLensModel(
    model_id="tokenaii/Horus-Lens-1.0-GGUF",
    filename="Horus-Lens-1.0-Q8_0.gguf"
).load()

# Generate the image
print("Generating image using Q8_0 GGUF model...")
model.generate_image(
    prompt="An astronaut riding a horse on Mars, highly detailed, photorealistic",
    output_path="outputs/gguf_mars_q8.png",
    seed=42
)

print("Saved generated image to outputs/gguf_mars_q8.png")
