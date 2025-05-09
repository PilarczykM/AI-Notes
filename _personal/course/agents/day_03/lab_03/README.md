# 📘 AGI Day 03 – Lab 03: Agregator Wiadomości z LangGraph

## 🎯 Cel projektu

Notebook demonstruje, jak zbudować agenta do wyszukiwania i streszczania wiadomości z różnych źródeł za pomocą **LangGraph**, **NewsAPI** i **OpenAI**. Agent pobiera aktualne wiadomości z internetu, przetwarza ich treść i generuje krótkie podsumowania, umożliwiając szybki przegląd najważniejszych informacji.

---

## 🛠️ Wykorzystane biblioteki

- [langgraph](https://github.com/langchain-ai/langgraph) – do budowy przepływu sterowania agenta,
- [langchain-openai](https://github.com/langchain-ai/langchain) – do integracji z modelami językowymi OpenAI,
- `langchain-core` – podstawowe komponenty LangChaina,
- `newsapi-python` – do pobierania wiadomości z serwisów informacyjnych przez NewsAPI,
- `beautifulsoup4` – do parsowania stron HTML i wydobywania treści artykułów,
- `pydantic` – do walidacji danych,
- `nest_asyncio`, `ipython` – narzędzia wspierające uruchamianie kodu w środowisku Jupyter.

---

## 🤖 Modele językowe (LLM)

Notebook korzysta z modeli językowych OpenAI, takich jak:

- **GPT-3.5** lub **GPT-4** – wykorzystywane do streszczania treści wiadomości oraz interakcji agenta z użytkownikiem.