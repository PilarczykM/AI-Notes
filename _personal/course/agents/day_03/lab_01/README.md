# 📘 AGI Day 03 – Lab 01: LangGraph Text Analysis Workflow

## 🎯 Cel projektu

Ten notebook demonstruje, jak zbudować modularny workflow do analizy tekstu z wykorzystaniem biblioteki **LangGraph**. Zawiera trzy główne etapy:

1. **Klasyfikację tekstu**,
2. **Ekstrakcję encji**,
3. **Tworzenie podsumowania**.

Celem jest pokazanie, jak zintegrować modele językowe z logiką przepływu danych.

---

## 🛠️ Wykorzystane biblioteki

- [langgraph](https://github.com/langchain-ai/langgraph) – do budowy grafów przepływu sterowania,
- [langchain](https://github.com/langchain-ai/langchain) – do obsługi LLM i komponentów aplikacji,
- `langchain-openai` – integracja z OpenAI API,
- `ollama` – do uruchamiania modeli lokalnych (np. Qwen3),
- `typing`, `functools` – pomocnicze moduły Pythona.

---

## 🤖 Modele językowe (LLM)

W notebooku wykorzystywane są dwa typy modeli językowych:

- **OpenAI GPT (np. gpt-3.5-turbo, gpt-4)** – dostępny przez API,
- **Qwen3 (via Ollama)** – model lokalny, uruchamiany lokalnie bez potrzeby łączenia z chmurą.