# Manual Chain-of-Thought

> [!TIP]
> Based on [CoT](./chain-of-thought.md)

The key idea behind Manual-CoT is to manually generate the demonstration examples that the language model (LM) can use for chain-of-thought (CoT) prompting.

*Prompt*:
```bash
Prompt:
You will formulate Chain of Thought (CoT) reasoning traces.
CoT is a prompting technique that helps you to think about a problem in a structured way. It breaks down a problem into a series of logical reasoning traces.

You will be given a question, and using this question, you will decompose the question into a series of logical reasoning traces. Only write the reasoning traces and do not answer the question yourself.

Examples of CoT reasoning traces:

Question: Did Brazilian jiu-jitsu Gracie founders have at least a baker iss dozen of kids between them?
Reasoning traces:
Who were the founders of Brazilian jiu-jitsu?
What is the number represented by a baker is dozen?
How many children do the Gracie founders have altogether?
Is this number bigger than a baker iss dozen?

Question: Is cow methane safer for the environment than cars?
Reasoning traces:
How much methane is produced by cars annually?
How much methane is produced by cows annually?
Is methane produced by cows less than methane produced by cars?

Question: {{question}}
Reasoning traces:
```