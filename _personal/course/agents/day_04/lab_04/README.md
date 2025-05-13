# AGI Day 04 Lab 04 – Multihop

## Cel notebooka

Notebook demonstruje wykorzystanie agenta LLM opartego na architekturze **ReAct** (Reasoning + Acting) do odpowiadania na złożone pytania wieloetapowe (multihop), które wymagają użycia więcej niż jednego źródła wiedzy lub narzędzia.

## Zadanie

Notebook realizuje:

1. Załadowanie dokumentu polityki HR,
2. Utworzenie bazy wektorowej z wykorzystaniem **ChromaDB**,
3. Stworzenie narzędzia do semantycznego przeszukiwania polityki HR (retriever),
4. Dodanie narzędzia do konwersji walut (API lub fikcyjne),
5. Skonfigurowanie agenta **ReAct**, który:
   - podejmuje decyzje na podstawie wyników działania narzędzi,
   - może łączyć dane z różnych źródeł, by odpowiedzieć na złożone pytanie użytkownika.

## Użyte modele LLM

Model OpenAI, skonfigurowany przez klasę `CFG`, wykorzystywany jest jako agent LLM do sterowania przepływem informacji i podejmowania decyzji w podejściu ReAct.

## Wykorzystane biblioteki

Notebook korzysta z narzędzi frameworka **LangChain** oraz innych komponentów:

- `langchain` – podstawowy framework,
- `langchain-openai` – integracja z modelami OpenAI,
- `langchain-community` – integracje i narzędzia społecznościowe,
- `langchain.hub` – dostęp do gotowych komponentów (np. promptów ReAct),
- `chromadb` – baza danych wektorowych do wyszukiwania semantycznego,
- `pydantic` – walidacja i struktury danych.
