# Few-shot prompting
Is a method in prompt engineering where a model is provided with a small number of examples (usually 1–5) before being asked to complete a similar task. These examples serve as demonstrations to help the model understand the task better, improving performance without requiring additional fine-tuning. This technique is especially useful for complex or nuanced tasks where zero-shot prompting may not produce optimal results.

## Examples of Few-shot Prompting:

### Grammar Correction:
### Prompt:
```bash
Prompt:
"Fix the grammar in these sentences:

'She go to school every day.' → 'She goes to school every day.'
'He don't like coffee.' → 'He doesn't like coffee.'
'They is happy.' →"*
Response: 'They are happy.'


Prompt: 'To do a "farduddle" means to jump up and down really fast. An example of a sentence that uses the word farduddle is:'
Response: 'When we won the game, we all started to farduddle in celebration.'
```
### Text Classification:
```bash
Prompt:
"Classify the sentiment of these reviews:

'The movie was incredible, I loved every moment!' → Positive
'The food was terrible and overpriced.' → Negative
'The service was okay, nothing special.' →"*
Response: Neutral
```
### Translating Phrases:
```bash
Prompt:
"Translate the following English phrases into Spanish:

'Hello, how are you?' → 'Hola, ¿cómo estás?'
'I love learning new languages.' → 'Me encanta aprender nuevos idiomas.'
'What time is it?' →"*
Response: '¿Qué hora es?'
```

### Limitations of Few-shot Prompting

Standard few-shot prompting works well for many tasks but is still not a perfect technique, especially when dealing with more complex reasoning tasks. Let's demonstrate why this is the case. Do you recall the previous example where we provided the following task:

```
The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1. 

Answer: 
```

If we try this again, the model outputs the following:

```
Yes, the odd numbers in this group add up to 107, which is an even number.
```

This is not the correct response, which not only highlights the limitations of these systems but that there is a need for more advanced prompt engineering. 

Let's try to add some examples to see if few-shot prompting improves the results.

*Prompt:*
```py
The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1.
Answer: The answer is False.

The odd numbers in this group add up to an even number: 17,  10, 19, 4, 8, 12, 24.
Answer: The answer is True.

The odd numbers in this group add up to an even number: 16,  11, 14, 4, 8, 13, 24.
Answer: The answer is True.

The odd numbers in this group add up to an even number: 17,  9, 10, 12, 13, 4, 2.
Answer: The answer is False.

The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1. 
Answer: 
```

*Output:*
```
The answer is True.
```

That didn't work. It seems like few-shot prompting is not enough to get reliable responses for this type of reasoning problem. The example above provides basic information on the task. If you take a closer look, the type of task we have introduced involves a few more reasoning steps. In other words, it might help if we break the problem down into steps and demonstrate that to the model. More recently, [chain-of-thought (CoT) prompting]() has been popularized to address more complex arithmetic, commonsense, and symbolic reasoning tasks.

Overall, it seems that providing examples is useful for solving some tasks. When zero-shot prompting and few-shot prompting are not sufficient, it might mean that whatever was learned by the model isn't enough to do well at the task. From here it is recommended to start thinking about fine-tuning your models or experimenting with more advanced prompting techniques.