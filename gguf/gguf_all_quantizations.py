import neuralnode as nn

def generate_with_quantization(filename, output_name):
    print(f"\n--- Loading GGUF model: {filename} ---")
    
    # Load GGUF model dynamically by specifying the filename
    model = nn.HorusLensModel(
        model_id="tokenaii/Horus-Lens-1.0-GGUF",
        filename=filename
    ).load()
    
    print(f"Generating image with {filename}...")
    model.generate_image(
        prompt="A majestic lion wearing a golden crown, fantasy art, digital painting",
        output_path=f"outputs/{output_name}.png",
        seed=100
    )
    print(f"Image saved to outputs/{output_name}.png")

if __name__ == "__main__":
    # You can choose the filename that fits your hardware/memory limits:
    # 1. Horus-Lens-1.0-Q3_K_M.gguf (Very lightweight, ~4GB VRAM/RAM)
    # 2. Horus-Lens-1.0-Q4_K_M.gguf (Balanced quality/size, ~6GB VRAM/RAM)
    # 3. Horus-Lens-1.0-Q6_K.gguf (High quality, ~8GB VRAM/RAM)
    # 4. Horus-Lens-1.0-Q8_0.gguf (Highest quality, ~10GB+ VRAM/RAM)
    
    # Example usage: Generate using the lightweight Q3_K_M quantization
    generate_with_quantization(
        filename="Horus-Lens-1.0-Q3_K_M.gguf",
        output_name="majestic_lion_q3"
    )
