# AGI Day 04 Lab 02 – Serwis Samochodowy

## Cel notebooka

Notebook prezentuje budowę inteligentnego systemu wsparcia dla serwisu samochodowego, który umożliwia użytkownikom zadawanie pytań związanych z naprawą, diagnozą oraz przeglądami technicznymi pojazdów. System korzysta z dużych modeli językowych (LLM), indeksów wektorowych oraz zdefiniowanych funkcji, by odpowiadać na zapytania użytkowników w sposób kontekstowy i zrozumiały.

## Zadanie

System oparty na `LlamaIndex`:

1. Wczytuje dane w formacie JSON dotyczące:
   - Problemów i usterek pojazdów,
   - Kosztów napraw,
   - Części samochodowych,
   - Harmonogramów serwisowych.

2. Tworzy wektorowe bazy danych (Vector Store Index) dla szybkiego przeszukiwania danych.

3. Definiuje narzędzia (funkcje) LLM do:
   - Diagnozowania problemów technicznych,
   - Szacowania kosztów naprawy,
   - Proponowania przeglądów okresowych.

4. Udostępnia te funkcje agentowi LLM, który wybiera odpowiednie narzędzie do odpowiedzi na zapytanie użytkownika.

## Użyte modele LLM

Zdefiniowane w klasie `CFG`:

- `gpt-4o-mini` – model językowy OpenAI wykorzystywany do obsługi agenta (`FunctionCallingAgentWorker`),
- `text-embedding-3-small` – model OpenAI do generowania embeddingów tekstowych dla indeksu wektorowego.

## Wykorzystane biblioteki

- `llama_index.core` – podstawowy framework:
  - `Document`, `Settings`, `StorageContext`, `VectorStoreIndex`,
- `llama_index.core.agent` – agenci i ich obsługa:
  - `AgentRunner`, `FunctionCallingAgentWorker`,
- `llama_index.llms.openai` – dostęp do modeli LLM,
- `llama_index.embeddings.openai` – embeddingi OpenAI,
- `llama_index.vector_stores.lancedb` – integracja z wektorową bazą danych **LanceDB**,
- `llama_parse` – biblioteka do parsowania dokumentów (np. JSON),
- `pandas`, `json` – pomocnicze biblioteki do obsługi danych.
