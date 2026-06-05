import torch
from diffusers import ZImagePipeline, ZImageTransformer2DModel, AutoencoderKL, FlowMatchEulerDiscreteScheduler
from transformers import Qwen2Tokenizer, AutoModel

# This script shows how to load the Horus Lens 1.0 model directly using diffusers/pytorch
# We load the components individually to bypass model_index.json name mismatches.

repo_id = "tokenaii/Horus-Lens-1.0"
device = "cuda" if torch.cuda.is_available() else "cpu"

print("Loading pipeline components directly from Hugging Face...")

# 1. Load Scheduler
scheduler = FlowMatchEulerDiscreteScheduler.from_pretrained(repo_id, subfolder="horus_scheduler")

# 2. Load Tokenizer
tokenizer = Qwen2Tokenizer.from_pretrained(repo_id, subfolder="horus_tokenizer")

# 3. Load Text Encoder
text_encoder = AutoModel.from_pretrained(
    repo_id, 
    subfolder="horus_text_encoder", 
    torch_dtype=torch.float16 if device == "cuda" else torch.float32
)

# 4. Load Transformer
transformer = ZImageTransformer2DModel.from_pretrained(
    repo_id, 
    subfolder="horus_transformer", 
    torch_dtype=torch.float16 if device == "cuda" else torch.float32
)

# 5. Load VAE
vae = AutoencoderKL.from_pretrained(
    repo_id, 
    subfolder="horus_vae", 
    torch_dtype=torch.float16 if device == "cuda" else torch.float32
)

# 6. Instantiate pipeline directly using loaded modules
print("Initializing ZImagePipeline...")
pipeline = ZImagePipeline(
    scheduler=scheduler,
    text_encoder=text_encoder,
    tokenizer=tokenizer,
    transformer=transformer,
    vae=vae
).to(device)

# 7. Generate image
print("Generating image...")
image = pipeline(
    prompt="A futuristic city with flying cars, neon lights, highly detailed, 4k",
    height=512,
    width=512,
    num_inference_steps=30,
    guidance_scale=7.5
).images[0]

# Save output
import os
os.makedirs("outputs", exist_ok=True)
image.save("outputs/direct_pytorch_city.png")
print("Saved generated image to outputs/direct_pytorch_city.png")
