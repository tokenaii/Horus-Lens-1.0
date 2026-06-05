import neuralnode as nn

# Load the GGUF model with the Q4_K_M quantization format
# Specifying the filename triggers GGUF loading automatically
print("Loading Horus Lens GGUF Q4_K_M model...")
model = nn.HorusLensModel(
    model_id="tokenaii/Horus-Lens-1.0-GGUF",
    filename="Horus-Lens-1.0-Q4_K_M.gguf"
).load()

# Generate the image
print("Generating image using Q4_K_M GGUF model...")
model.generate_image(
    prompt="A detailed cinematic image of an ancient Egyptian AI lab, golden light",
    output_path="outputs/gguf_egypt_q4.png",
    seed=42
)

print("Saved generated image to outputs/gguf_egypt_q4.png")
