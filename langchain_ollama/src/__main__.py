from operator import itemgetter
from typing import Optional

from langchain_core.language_models import BaseLLM
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import PromptTemplate

STORY = """
Once upon a time, there was a lazy cat named Muffin and an overachieving dog named Biscuit who lived together in a cozy little house. One rainy afternoon, Biscuit decided to build a "super pillow fort" while Muffin lounged on the couch like royalty.

“Why don’t you help me, Muffin?” asked Biscuit, balancing a stack of cushions taller than him.
“I am helping,” said Muffin, swatting a single sock toward the fort. “It’s emotional support.”

Just as Biscuit finished his masterpiece, the roof collapsed with a spectacular poof of feathers. Muffin, watching from her spot, sighed dramatically. “Tragic. Another victim of poor leadership.”

Annoyed but determined, Biscuit rebuilt the fort twice as tall, only for Muffin to climb inside and declare, “Finally, a throne worthy of me.” Biscuit stared at her and muttered, “Next time, I’m getting a goldfish.”

And from then on, Muffin ruled her pillow kingdom while Biscuit planned a rebellion in the snack drawer.
"""
BASE_TEMPLATE = """
Answer the question based on the context below. If you can't 
answer the question, reply "I don't know".

Context: {context}

Question: {question}
"""


def run():
    model = create_model()

    prompt = PromptTemplate(input_variables=["context", "question"], template=BASE_TEMPLATE)

    # chain = prompt | model
    # print(chain.invoke({"context" : STORY, "question": "Why Muffin wasn't helping?"}))

    translation_chain = create_translation_chain(prompt, model)
    result = translation_chain({
        "context": STORY,
        "question": "Why Muffin wasn't helping?"
    })
    print(result)


def create_translation_chain(prompt: PromptTemplate, model: BaseLLM):
    """
    Creates a reusable translation chain that translates an answer if a language is specified.
    """
    translation_prompt_template = """
        Translate '{answer}' to {language}.
        Return only translation, without any additional explanation.
        """
    translation_prompt = PromptTemplate.from_template(translation_prompt_template)

    def translation_chain(data: dict[str: Optional[str]]):
        """
        Executes the chain with optional translation.

        Parameters:
            data (ChainInput): Dictionary with 'context', 'question', and optional 'language'.

        Returns:
            str: Translated answer or original answer.
        """
        # Invoke the main chain to get the answer
        answer = (prompt | model).invoke({"context": data["context"], "question": data["question"]})

        # If a language is specified, translate the answer
        if "language" in data and data["language"]:
            return ({"answer": answer, "language": data["language"]}
                    | translation_prompt
                    | model).invoke(data)
        return answer

    return translation_chain

def create_model(name: str = "llama3.2"):
    try:
        return OllamaLLM(model=name)
    except ModuleNotFoundError as e:
        print("Please install ollama first.")
        print(e.msg)
        exit()


if __name__ == "__main__":
    run()