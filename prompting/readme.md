# Prompt Techniques

* [Zero-Shot Prompting](./src/zero-shot.ipynb):
  
  > **Definition**: Technique where a model is given a task without any prior examples or context.
* [Few-Shot Prompting](./src/few-shot.md)

  > **Definition**: Technique where a model is given a few examples of a task / word / meaning in the prompt before being asked to generate a response. This helps guide the model toward the desired output format and improves accuracy.

* [Chain-of_thought (COT) Prompting](./src/chain-of-though.md)

  > **Definition**: Technique where the model is encouraged to think through intermediate steps to solve a problem or reach a conclusion. It helps the model break down complex tasks and make its reasoning process more explicit, leading to better answers.

  * [Zero-Shot Chain-of-Thought](./src/chain-of-thought-zero-shot.md)
  * [Manual Chain-of-Thought](./src/chain-of-thought-manual.md)
* [Self-Consistency](./src/self-consistency.md)
  > **Definition**: Technique where multiple reasoning paths are generated for a given problem, and the most consistent answer is selected. This helps improve accuracy by reducing errors from a single reasoning chain.