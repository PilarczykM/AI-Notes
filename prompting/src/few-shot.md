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