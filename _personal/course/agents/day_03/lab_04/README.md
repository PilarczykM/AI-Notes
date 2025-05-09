# 📘 AGI Day 03 – Lab 04: Agent Badawczy z Wykorzystaniem Wikipedii i LLM

## 🎯 Cel projektu

Celem tego notebooka jest implementacja agenta badawczego, który automatycznie przetwarza pytania użytkownika, korzystając z:

- Wikipedii jako źródła wiedzy,
- dużego modelu językowego (LLM),
- wektorowej bazy danych Milvus,
- oraz biblioteki LangChain do tworzenia łańcuchów przetwarzania.

Agent:

1. Rozbija pytanie na mniejsze podpytania,
2. Wyszukuje odpowiednie informacje na Wikipedii,
3. Zapisuje ich reprezentacje wektorowe w Milvusie,
4. Używa łańcucha RAG (Retrieval-Augmented Generation) do generowania odpowiedzi,
5. Na koniec tworzy końcowy raport w formacie Markdown.

## 🛠️ Użyte biblioteki

- `langchain` – do tworzenia agenta i łańcuchów RAG,
- `wikipediaapi` – pobieranie treści z Wikipedii,
- `pymilvus` – integracja z bazą wektorową Milvus,
- `langchain_ollama` – interfejs do lokalnych modeli LLM oraz embeddingów,
- `pandas`, `json`, `uuid`, `os`, `re`, `tqdm` – wspierające przetwarzanie danych i organizację pracy agenta.

## 🧠 Modele

Notebook wykorzystuje dwa modele:

- **`deepseek-r1:8b`** – główny model językowy (LLM) używany do analizy pytań i generowania odpowiedzi,
- **`nomic-embed-text`** – model embeddingowy, służący do przekształcania treści z Wikipedii na wektory umieszczane w bazie danych Milvus.
