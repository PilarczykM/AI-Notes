# 🧠 AGI Day 08 – Agent Evaluation & Observability

## 📋 Przegląd dnia

Celem dnia 08 w ścieżce AGI Labs jest zrozumienie, jak **oceniać, monitorować i analizować działania agentów opartych na dużych modelach językowych (LLM)**. Przez cztery laboratoria uczestnik uczy się:

- budowy i testowania agentów rozwiązujących zadania,
- automatycznej ewaluacji ich odpowiedzi,
- generowania danych testowych,
- integracji z narzędziami do monitorowania (Arize Phoenix),
- oraz obsługi zapytań SQL za pomocą języka naturalnego.

---

## 🧪 Laboratoria

### ✅ [Lab 01 – AgentEval z AutoGen](lab_01/pl/README.md)
Automatyczna ewaluacja odpowiedzi agentów przy użyciu kryteriów wygenerowanych przez LLM.

➡️ *Model:* GPT-4.1  
➡️ *Narzędzia:* AutoGen, matplotlib, scipy

---

### ✅ [Lab 02 – OpenAI Agent Evaluation + Phoenix](lab_02/pl/README.md)
Ocena agenta rozwiązującego zadania matematyczne przy pomocy `llm_classify` i logowanie do Phoenix.

➡️ *Model:* GPT-4.1  
➡️ *Narzędzia:* Phoenix, OpenAI Agents

---

### ✅ [Lab 03 – SmolAgents z obserwowalnością](lab_03/pl/README.md)
Lekki agent (`SmolAgent`) z narzędziami wyszukiwania i kodu, monitorowany i oceniany przez Phoenix.

➡️ *Model:* GPT-4.1  
➡️ *Narzędzia:* SmolAgents, Phoenix, DuckDuckGo, Langchain

---

### ✅ [Lab 04 – SQL Agent z ewaluacją](lab_04/pl/README.md)
Agent odpowiadający na pytania w języku naturalnym przez generowanie zapytań SQL do bazy danych SQLite.

➡️ *Model:* GPT-4.1  
➡️ *Narzędzia:* SQLite, Phoenix, OpenAI, `llm_classify`

---

## 📦 Wymagania ogólne

- Konto i klucz API OpenAI
- Konto Arize Phoenix (do monitorowania agentów)
- Środowisko zgodne z Google Colab lub lokalne z Pythonem 3.9+
