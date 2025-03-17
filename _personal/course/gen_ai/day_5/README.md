# Module 5: Generative AI - Video  

## Topics Covered  
- **How Generative AI Models for Video Work**  
- **Use Case 1:** Text-to-Video Generation  
- **Use Case 2:** Image-to-Video Transformation  
- **Use Case 3:** Video-to-Video Style Transfer  

## Learning Outcomes  
By the end of this module, you will be able to:  
✅ Explain how **Generative AI models for video** work, describing the fundamental principles and techniques used for video creation and modification.  
✅ Generate videos from **text inputs** (Text-to-Video), showcasing AI-powered content creation.  
✅ Transform **images into videos** (Image-to-Video), demonstrating the ability to create dynamic visuals from static content.  
✅ Apply **style transfer techniques** to videos (Video-to-Video), modifying their appearance while preserving motion and structure.  
✅ Fine-tune **video generative models** for specific tasks, optimizing them to achieve desired visual effects.  

## Example Projects  
### 🛠 Lab Exercises & Applications  
- **Video Style Transfer:** Modify the artistic style of videos for marketing and creative applications.  
- **Automated Product Demonstration Videos:** Generate promotional videos showcasing product features.  
- **Virtual 3D Interior Design:** Create immersive 3D environments demonstrating interior design concepts.  

This module provides a practical approach to **creating and transforming video content using Generative AI**. 🎥✨🚀  

# Projects:
- **[Lab 1](./src/lab_1/pl/lab_1.ipynb) - Generate video from text**  
  - **Model:** emilianJR/epiCRealism
  - **Tools:** diffusers peft imageio-ffmpeg
- **[Lab 2](./src/lab_2/pl/lab_2.ipynb) - Generate video from image**  
  - **Model:** stabilityai/stable-video-diffusion-img2vid-xt
  - **Tools:** diffusers transformers accelerate imageio-ffmpeg
- **[Lab 3](./src/lab_3/pl/lab_3.ipynb) - Edit video using prompt**  
  - **Model:** THUDM/CogVideoX-5b camenduru/cogvideox-5b-float16
  - **Tools:** torch torchvision torchaudio accelerate
