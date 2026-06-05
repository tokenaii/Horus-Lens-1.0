<h1 align="center" style="font-size: 2.5em;">Horus Lens 1.0</h1>

<div align="center">
  <a href="https://huggingface.co/tokenaii/Horus-Lens-1.0">
    <img src="https://huggingface.co/datasets/huggingface/badges/resolve/main/model-on-hf-md.svg" alt="Model on Hugging Face">
  </a>
</div>
<br>

<div align="center">
  <img src="https://huggingface.co/tokenaii/Horus-Lens-1.0/resolve/main/media/panner.png" alt="Horus Lens 1.0 Banner" width="100%" />
</div>

## Overview
Horus Lens 1.0 is an advanced text-to-image and image-to-image generation model. It is a highly enhanced and fine-tuned version of the base model [Tongyi-MAI/Z-Image](https://huggingface.co/Tongyi-MAI/Z-Image). To achieve superior generation quality, Horus Lens 1.0 was extensively trained on hundreds of thousands of new, carefully curated, and clean images. This rigorous training process significantly improves the model's understanding of complex prompts, artistic fidelity, and overall visual output.

<div align="center">
  <img src="https://huggingface.co/tokenaii/Horus-Lens-1.0/resolve/main/media/HL1.0P.png" alt="Horus Lens 1.0 Preview" width="100%" />
</div>

## Generated Examples

Below is an example showcasing the model's ability to accurately follow prompt instructions and transform an image:

<table style="width:100%; border:none; border-collapse: collapse;">
  <tr>
    <td style="width:40%; text-align:center; border:none; padding: 10px;">
      <img src="https://huggingface.co/tokenaii/Horus-Lens-1.0/resolve/main/media/ex1f.jpeg" alt="Input/Original" style="max-width:100%; border-radius: 8px;" />
    </td>
    <td style="width:20%; text-align:center; border:none; vertical-align:middle; padding: 10px; font-weight: bold; font-size: 1.1em; color: #555;">
      <i>Make the scene in night and put glowing starts in the sky</i>
    </td>
    <td style="width:40%; text-align:center; border:none; padding: 10px;">
      <img src="https://huggingface.co/tokenaii/Horus-Lens-1.0/resolve/main/media/ex1s.png" alt="Generated Output" style="max-width:100%; border-radius: 8px;" />
    </td>
  </tr>
</table>

## Quick Start

You can download and use Horus Lens 1.0 directly from our Hugging Face repository:
👉 **[tokenaii/Horus-Lens-1.0](https://huggingface.co/tokenaii/Horus-Lens-1.0)**

### 1. Install or Upgrade NeuralNode
```bash
# Install the framework
pip install neuralnode

# Optional: Upgrade the framework
pip install --upgrade neuralnode
```

### 2. List available Horus models
```python
import neuralnode as nn

# Print all available Horus models in the registry
nn.print_model_list()
```

### 3. Load and generate an image
```python
import neuralnode as nn

# Load the Horus Lens 1.0 text-to-image model
model = nn.HorusLensModel("tokenaii/Horus-Lens-1.0").load()

# Generate and save the image
model.generate_image(
    prompt="A detailed cinematic image of an ancient Egyptian AI lab, golden light",
    output_path="outputs/horus_lens.png",
    seed=42
)

print("Saved image to outputs/horus_lens.png")
```
## GGUF Compressed Versions

For users with limited hardware resources or lower VRAM, we provide optimized GGUF compressed versions of Horus Lens 1.0 in a dedicated repository:
👉 **[tokenaii/Horus-Lens-1.0-GGUF](https://huggingface.co/tokenaii/Horus-Lens-1.0-GGUF)**

Below is a breakdown of the available GGUF versions, their file sizes, and estimated VRAM requirements for inference:

| Model File | File Size (GB) | Estimated VRAM Requirement | Recommended Hardware / Use Case |
| :--- | :---: | :---: | :--- |
| **Horus-Lens-1.0-Q3_K_M.gguf** | 4.56 GB | ~5.5 GB | Low VRAM GPUs (e.g., 6 GB cards) |
| **Horus-Lens-1.0-Q4_K_M.gguf** | 5.07 GB | ~6.0 GB | Standard consumer GPUs / Great balance of speed and quality |
| **Horus-Lens-1.0-Q6_K.gguf** | 6.10 GB | ~7.0 GB | High fidelity generation with medium-high VRAM |
| **Horus-Lens-1.0-Q8_0.gguf** | 7.22 GB | ~8.0 GB | Best quality, nearest to the original uncompressed model |

## About TokenAI & The Horus Family
**TokenAI** is a non-profit AI startup founded in 2025 by Assem Sabry, located in Alexandria, Egypt. 

The **Horus** family is our line of advanced AI models. The series began with **Horus 1.0 4B**, which achieved remarkable success as the very first language model to be fully trained from scratch in Egypt. Building on that foundation, Horus Lens brings specialized and powerful capabilities in image generation while retaining the high-quality standards of our models.

### Contact & Community
- **Website:** [tokenai.cloud](https://tokenai.cloud/)
- **Hugging Face:** [tokenaii](https://huggingface.co/tokenaii)
- **GitHub:** [tokenaii](https://github.com/tokenaii)
- **LinkedIn:** [TokenAI](https://www.linkedin.com/company/tokenaii)
- **Location:** Alexandria, Egypt

## License
This project is licensed under the Apache License 2.0.

## Citation
If you use Horus Lens 1.0 in your research or applications, please cite it as:
```bibtex
@misc{tokenai_horus_lens_1_0,
    title={Horus Lens 1.0: Advanced Image Generation Model},
    author={Assem Sabry and TokenAI},
    year={2026},
    url={https://huggingface.co/tokenaii/Horus-Lens-1.0}
}
```
