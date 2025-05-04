# AGI Day 02 – Lab 05: Agent LangChain do zapytań SQL i przeszukiwania baz danych

## Opis

Notebook prezentuje stworzenie agenta z użyciem frameworka **LangChain** i modelu **Cohere**, który potrafi wykonywać zapytania do zewnętrznej bazy danych SQL. Agent działa w stylu ReAct i potrafi korzystać z narzędzi do wykonywania operacji na strukturach danych, łącząc je z generowaniem odpowiedzi w języku naturalnym.

## Użyte biblioteki

- `langchain`
- `langchain_cohere`
- `langchain_experimental`
- `langchain_community.utilities.sql_database`

## Użyty LLM

- **Cohere Command R+** – model językowy firmy Cohere, wykorzystany do przetwarzania zapytań, interpretacji wyników i planowania działania agenta.

## Cel notebooka

Celem notebooka jest zbudowanie agenta, który:
- Może **komunikować się z relacyjną bazą danych SQL**,
- Wykonuje zapytania SQL generowane automatycznie na podstawie pytań w języku naturalnym,
- Interpretuje wyniki i potrafi podać odpowiedzi użytkownikowi w zrozumiałej formie,
- Integruje podejście RAG (retrieval-augmented generation) z dostępem do danych strukturalnych.
