# AGI Day 02 – Lab 04: Agent LangChain z analizą DataFrame i GPT

## Opis

Notebook demonstruje tworzenie agenta AI z wykorzystaniem frameworka **LangChain** oraz modelu językowego **GPT (OpenAI)**, który potrafi analizować dane zapisane w strukturze **pandas DataFrame**. Dzięki integracji z narzędziem `create_pandas_dataframe_agent`, agent jest w stanie odpowiadać na pytania użytkownika w języku naturalnym i wykonywać rzeczywiste operacje analityczne na danych.

## Użyte biblioteki

- `langchain`
- `langchain_openai`
- `langchain_experimental`
- `pydantic`
- `pandas`

## Użyty LLM

- **GPT (OpenAI)** – model językowy wykorzystywany do przekształcania zapytań użytkownika w operacje na danych i generowania odpowiedzi.

## Cel notebooka

Celem notebooka jest stworzenie agenta AI, który:
- Potrafi **czytać i analizować dane z pandas DataFrame**,
- Odpowiada na pytania w języku naturalnym związane z zawartością danych,
- Wykonuje operacje statystyczne, sortowanie, filtrowanie, podsumowania itp.,
- Łączy model językowy z kontekstem danych w celu inteligentnej analizy informacji.
