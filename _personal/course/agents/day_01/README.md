# AGI Day 1 – Przegląd laboratoriów

Zbiór notebooków demonstrujących różne sposoby tworzenia i rozwijania agentów AI z użyciem modeli językowych i integracji narzędziowych.

- [Lab 1: Prosty agent AI z Claude 3](lab_1/pl/agi_day_1_lab_1.ipynb): Tworzenie agenta językowego Claude 3 wykonującego operacje matematyczne z użyciem własnej funkcji kalkulatora. **Biblioteki**: _anthropic_
- [Lab 2: Agent AI z narzędziami OpenAI i Google](lab_2/pl/agi_day_1_lab_2.ipynb): Agent z dostępem do OpenAI i Google Search; rozwiązuje zadania z wykorzystaniem zewnętrznych API. **Biblioteki**: _openai, google-api-python-client_
- [Lab 3: Lokalny agent z LLaMA 3 i Ollama](lab_3/pl/agi_day_1_lab_3.ipynb): Agent lokalny uruchamiany przez Ollama; wykonuje zadania np. pobierając pogodę z lokalnej funkcji `get_current_weather`. **Biblioteki**: _ollama_
- [Lab 4: Agent Cohere z narzędziami](lab_4/pl/agi_day_1_lab_4.ipynb): Agent językowy Cohere korzystający z narzędzi: `daily_sales_report` i `product_lookup` do analizy sprzedaży. **Biblioteki**: _cohere_
- [Lab 5: Agent z pamięcią i planowaniem](lab_5/pl/agi_day_1_lab_5.ipynb): Rozszerzenie agenta Cohere o planowanie wieloetapowe, równoległe oraz zarządzanie stanem (pamięć). **Biblioteki**: _cohere_
- [Lab 6: Autonomiczny agent z wyszukiwarką](lab_6/pl/agi_day_1_lab_6.ipynb): Autonomiczny agent `smolagents`, który wyszukuje informacje w DuckDuckGo i generuje odpowiedzi tekstowe lub obrazowe. **Biblioteki**: _smolagents, duckduckgo-search, sentence-transformers, datasets_
