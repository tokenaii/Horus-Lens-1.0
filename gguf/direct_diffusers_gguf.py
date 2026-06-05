import torch
from diffusers import ZImagePipeline, ZImageTransformer2DModel, AutoencoderKL, FlowMatchEulerDiscreteScheduler
from transformers import Qwen2Tokenizer, AutoModel
from huggingface_hub import hf_hub_download
import os

# This script shows how to load Horus Lens 1.0 GGUF models directly using diffusers/pytorch
# We load the GGUF transformer from the GGUF file, and load the remaining components from the base model.

base_repo_id = "tokenaii/Horus-Lens-1.0"
gguf_repo_id = "tokenaii/Horus-Lens-1.0-GGUF"
gguf_filename = "Horus-Lens-1.0-Q4_K_M.gguf"

device = "cuda" if torch.cuda.is_available() else "cpu"
compute_dtype = torch.float16 if device == "cuda" else torch.float32

# 1. Download GGUF weights from HF Hub
print(f"Downloading GGUF file: {gguf_filename}...")
model_path = hf_hub_download(repo_id=gguf_repo_id, filename=gguf_filename)

print("Loading GGUF Transformer weights...")
# 2. Load quantized GGUF transformer weights
transformer = ZImageTransformer2DModel.from_single_file(
    model_path,
    torch_dtype=compute_dtype
)

print("Loading remaining pipeline components from base repo...")
# 3. Load other components individually from the base model repo
scheduler = FlowMatchEulerDiscreteScheduler.from_pretrained(base_repo_id, subfolder="horus_scheduler")
tokenizer = Qwen2Tokenizer.from_pretrained(base_repo_id, subfolder="horus_tokenizer")
text_encoder = AutoModel.from_pretrained(base_repo_id, subfolder="horus_text_encoder", torch_dtype=compute_dtype)
vae = AutoencoderKL.from_pretrained(base_repo_id, subfolder="horus_vae", torch_dtype=compute_dtype)

# 4. Instantiate pipeline directly using loaded modules
print("Initializing ZImagePipeline...")
pipeline = ZImagePipeline(
    scheduler=scheduler,
    text_encoder=text_encoder,
    tokenizer=tokenizer,
    transformer=transformer,
    vae=vae
).to(device)

# 5. Generate image
print("Generating image...")
image = pipeline(
    prompt="A detailed cinematic image of an ancient Egyptian AI lab, golden light",
    height=512,
    width=512,
    num_inference_steps=30,
    guidance_scale=7.5
).images[0]

# Save output
os.makedirs("outputs", exist_ok=True)
image.save("outputs/direct_gguf_egypt.png")
print("Saved generated image to outputs/direct_gguf_egypt.png")
