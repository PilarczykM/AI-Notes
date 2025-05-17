# AGI Day 06 Lab 4 – System RAG z agentami CrewAI

## 🎯 Cel notebooka

Notebook prezentuje implementację systemu typu **Retrieval-Augmented Generation (RAG)** z wykorzystaniem biblioteki **CrewAI**, w której zespół agentów współpracuje w celu przetwarzania zapytań użytkownika i dostarczania trafnych odpowiedzi na podstawie zewnętrznych źródeł wiedzy.

Zespół składa się z pięciu wyspecjalizowanych agentów, z których każdy pełni określoną rolę w przetwarzaniu i wzbogacaniu odpowiedzi. Notebook demonstruje kompletny pipeline oparty o zapytanie użytkownika oraz analizę dokumentu źródłowego (artykuł PDF z NeurIPS).

---

## 📚 Użyte biblioteki

- `crewai` – do tworzenia zespołów współpracujących agentów,
- `crewai_tools` – zestaw narzędzi wspierających działanie agentów (np. wyszukiwanie, analiza dokumentów),
- `langchain_openai` – integracja z modelami OpenAI za pomocą LangChain,
- `langchain_community` – narzędzia z ekosystemu LangChain,
- `google.colab.userdata` – do pobierania kluczy API w Colabie,
- `requests` – do pobierania treści z internetu,
- `os` – operacje systemowe.

---

## 🧠 Użyte modele LLM

Notebook wykorzystuje dwa typy modeli:

- **gpt-4o-mini** – główny model językowy do generowania odpowiedzi,
- **BAAI/bge-small-en-v1.5** – model do generowania osadzeń (embeddingów) tekstowych, używany przy przeszukiwaniu dokumentów PDF i dopasowywaniu kontekstu.