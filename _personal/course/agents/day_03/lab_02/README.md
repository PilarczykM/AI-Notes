# 📘 AGI Day 03 – Lab 02: Asystent Planowania Podróży z LangGraph

## 🎯 Cel projektu

Ten notebook demonstruje, jak stworzyć interaktywnego asystenta do planowania jednodniowej wycieczki z wykorzystaniem **LangGraph** i modeli językowych. System prowadzi użytkownika przez dialog, zbierając dane o mieście docelowym i zainteresowaniach, a następnie generuje dopasowany plan podróży.

---

## 🛠️ Wykorzystane biblioteki

- [langgraph](https://github.com/langchain-ai/langgraph) – do tworzenia konwersacyjnego grafu przepływu informacji,
- [langchain](https://github.com/langchain-ai/langchain) – do integracji z LLM oraz zarządzania stanem rozmowy,
- `langchain-openai` – do korzystania z modeli OpenAI (np. GPT-4),
- `typing`, `annotated-types` – do definiowania struktury stanu (`PlannerState`).

---

## 🤖 Modele językowe (LLM)

Notebook korzysta z modeli językowych OpenAI:

- **OpenAI GPT (np. gpt-4)** – wykorzystywany do generowania planów podróży na podstawie danych od użytkownika.