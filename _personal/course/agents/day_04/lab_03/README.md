# AGI Day 04 Lab 03 – Pytania do Bazy

## Cel notebooka

Celem notebooka jest porównanie dwóch podejść do odpowiadania na pytania dotyczące dokumentacji technicznej (na przykładzie Hugging Face): klasycznego podejścia **RAG (Retrieval-Augmented Generation)** oraz podejścia **agentowego RAG**, w którym agent wybiera narzędzia i strategie odpowiedzi w oparciu o kontekst i dane.

## Zadanie

Notebook wykonuje następujące kroki:

1. Ładuje dokumentację Hugging Face jako zbiór danych tekstowych,
2. Generuje osadzenia (embeddingi) tekstu za pomocą `sentence-transformers`,
3. Tworzy bazę wektorową w **FAISS** z pomocą **LangChain**,
4. Tworzy narzędzie wyszukiwania semantycznego w tej bazie,
5. Tworzy dwa systemy odpowiedzi:
   - **Standardowy RAG** – klasyczne podejście z przeszukiwaniem i generowaniem odpowiedzi,
   - **Agentowy RAG** – agent LLM zintegrowany z narzędziem, który decyduje, kiedy i jak używać wyszukiwania.

## Użyte modele LLM

Modele są wczytywane przez `smolagents` i `langchain`. W konfiguracji klasy `CFG` zapisano:

- `gpt-4o-mini` – główny model językowy używany przez agenta do przetwarzania zapytań i podejmowania decyzji,
- `sentence-transformers/all-MiniLM-L6-v2` – model generujący embeddingi dla indeksu wektorowego FAISS.

## Wykorzystane biblioteki

Notebook korzysta z ekosystemu **LangChain** oraz narzędzi Hugging Face:

- `langchain` – do budowania systemów RAG oraz integracji z wektorowymi bazami danych,
- `langchain-community` – dodatkowe integracje m.in. z FAISS,
- `sentence-transformers` – generowanie embeddingów tekstowych,
- `faiss-cpu` – szybkie wyszukiwanie podobnych wektorów,
- `smolagents` – tworzenie agentów opartych na LLM,
- `datasets`, `huggingface_hub` – pobieranie i zarządzanie dokumentacją oraz modelami z Hugging Face.
