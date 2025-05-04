# Module 2: Generative AI - Image  

## Topics Covered  
- **How Diffusion Models Work**  
- **Building a Prompt Step by Step**  
- **Custom Application: Gradio + Stable Diffusion**  
- **Fine-Tuning Stable Diffusion (Dreambooth)**  

## Learning Outcomes  
By the end of this module, you will be able to:  
✅ Understand how diffusion models work and describe their fundamental principles in the context of Generative AI.  
✅ Create and refine prompts for image generation step by step, demonstrating an understanding of the process and techniques.  
✅ Use tools like **Gradio** and **Streamlit** to deploy and test generative models.  
✅ Utilize **DALL·E 3** via OpenAI's GUI and API, showcasing the ability to integrate and apply these tools in practical scenarios.  
✅ Fine-tune **Stable Diffusion (SD)** using techniques like **Dreambooth** to create personalized content.  

## Example Projects
- **Synthetic Models:** Create visualizations with virtual models of any gender, color, or body type.  
- **Interior Design:** Generate room designs from textual descriptions and modify spaces based on client inputs.  
- **Automated Image Generation:** Develop a workflow for generating marketing graphics and other visual assets.  

This module deepens your understanding of image-based Generative AI, equipping you with hands-on skills for real-world applications. 🎨🚀  

## Projects  
### 🛠 Lab Exercises  
- **[Lab 1](./src/lab_1/pl/lab_1.ipynb) - Image generation using text**  
  - **Model:** stabilityai/stable-diffusion-xl-base-1.0
  - **Tools:** transformers diffusers accelerate safetensors
- **[Lab 2](./src/lab_2/pl/lab_2.ipynb) - Image generation using text with encoder VUE, prompt and negative prompt**  
  - **Model:** stabilityai/stable-diffusion-xl-base-1.0, madebyollin/sdxl-vae-fp16-fix
  - **Tools:** transformers diffusers accelerate safetensors
- **[Lab 3](./src/lab_3/pl/lab_3.ipynb) - Image modification using Inpainting or outpainting technique**  
  - **Model:** stabilityai/stable-diffusion-2-inpainting
  - **Tools:** transformers diffusers accelerate safetensors segment-anything
- **[Lab 4](./src/lab_4/pl/lab_4.ipynb) - Create images with web app using Gradio**  
  - **Model:** sstabilityai/stable-diffusion-xl-base-1.0
  - **Tools:** gradio transformers diffusers accelerate safetensors segment-anything
- **[Lab 5](./src/lab_5/pl/lab_5.ipynb) - Create images with web app using Gradio**  
  - **Model:** sstabilityai/stable-diffusion-xl-base-1.0
  - **Tools:** gradio transformers diffusers accelerate safetensors segment-anything
- **[Lab 6](./src/lab_6/pl/lab_6.ipynb) - Train model to create images based on samples**  
  - **Model:** stabilityai/stable-diffusion-xl-base-1.0
  - **Tools:** transformers bitsandbytes accelerate safetensors peft autotrain-advanced
- **[Lab 7](./src/lab_7/pl/lab_7.ipynb) - Image generation using FLUX model (4-bits)**  
  - **Model:** sayakpaul/flux.1-dev-nf4-pkg
  - **Tools:** transformers accelerate bitsandbytes diffusers
