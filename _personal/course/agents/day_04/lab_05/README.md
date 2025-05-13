# AGI Day 04 Lab 05 – arXiv

## Cel notebooka

Notebook pokazuje, jak stworzyć agenta ReAct wspieranego przez dużego modela językowego (LLM), który potrafi przeszukiwać bazę artykułów naukowych z serwisu **arXiv**, pobierać ich treść, analizować ją i odpowiadać na pytania użytkownika na ich podstawie.

## Zadanie

Notebook wykonuje następujące operacje:

1. Pobiera artykuły naukowe z arXiv na podstawie podanego tematu,
2. Tworzy z nich indeks wektorowy (Vector Store) z wykorzystaniem **LlamaIndex**,
3. Zapisuje indeks na dysku lokalnym w celu ponownego wykorzystania,
4. Tworzy agenta **ReAct**, który ma dostęp do trzech narzędzi:
   - Przeszukiwania lokalnego indeksu,
   - Pobierania nowych artykułów z arXiv,
   - Pobierania plików PDF publikacji,
5. Agent odpowiada na złożone zapytania użytkownika, podejmując decyzje o kolejnych działaniach w ramach architektury ReAct.

## Użyte modele LLM

Zdefiniowane w klasie `CFG`:

- `gpt-4o-mini` – model językowy wykorzystywany przez agenta ReAct do analizy i generowania odpowiedzi,
- `text-embedding-3-small` – model OpenAI służący do generowania osadzeń tekstu (embeddingów) na potrzeby indeksowania i przeszukiwania dokumentów.

## Wykorzystane biblioteki

Notebook korzysta z następujących bibliotek:

- `arxiv` – pobieranie metadanych i treści publikacji z serwisu arXiv,
- `llama_index` – tworzenie i zarządzanie indeksem dokumentów wspieranym przez LLM,
- `llama-index-llms-openai` – integracja z modelami językowymi OpenAI,
- `llama-index-embeddings-openai` – generowanie embeddingów OpenAI,
- `requests` – pobieranie plików PDF z Internetu,
- `os` – operacje na plikach i ścieżkach systemowych.
