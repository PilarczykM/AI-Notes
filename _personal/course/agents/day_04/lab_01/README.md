# AGI Day 04 Lab 01 – Query Router

## Cel notebooka

Notebook demonstruje budowę systemu automatycznego kierowania zapytań użytkownika do właściwego silnika wyszukiwania informacji, wykorzystując różne typy indeksów utworzonych na podstawie dokumentu PDF.

## Zadanie

Notebook realizuje następujące kroki:
1. Wczytanie dokumentu PDF (`agents_paper.pdf`),
2. Utworzenie dwóch typów indeksów:
   - **Summary Index** – do zapytań wymagających ogólnego przeglądu treści,
   - **Vector Store Index** – do zapytań wymagających semantycznego dopasowania,
3. Konfiguracja silników zapytań (Query Engines),
4. Utworzenie routera zapytań (`RouterQueryEngine`), który przy pomocy LLM wybiera odpowiedni silnik.

## Użyte modele LLM

Nazwy modeli konfigurowane są w klasie `CFG`. W notebooku użyto:

- `gpt-4o-mini` – jako model językowy do wyboru odpowiedniego silnika zapytań (via `LLMSingleSelector`),
- `BAAI/bge-small-en-v1.5` – jako model osadzeń do indeksu wektorowego (via `HuggingFaceEmbedding`).

## Wykorzystane biblioteki

Notebook wykorzystuje bibliotekę **LlamaIndex** i powiązane moduły:

- `llama_index.core`:
  - `SimpleDirectoryReader` – do ładowania dokumentów,
  - `SentenceSplitter` – do dzielenia tekstu na segmenty,
  - `SummaryIndex`, `VectorStoreIndex` – typy indeksów,
  - `QueryEngineTool`, `RouterQueryEngine` – do zapytań i routingu,
  - `Settings` – konfiguracja środowiska,
- `llama_index.llms.openai.OpenAI` – dostęp do modeli LLM (OpenAI),
- `llama_index.embeddings.huggingface.HuggingFaceEmbedding` – osadzenia z modeli Hugging Face,
- `llama_index.core.selectors.LLMSingleSelector` – wybór najlepszego silnika zapytań za pomocą LLM.
