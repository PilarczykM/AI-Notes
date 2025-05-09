# AGI_day_03_lab_05 – Deep Research DIY

## 🎯 Cel projektu

Notebook ten prezentuje sposób budowy agenta AI do prowadzenia zaawansowanych badań w internecie – tzw. **Deep Research** – w wersji „Do It Yourself”. Celem jest stworzenie elastycznego i rozszerzalnego rozwiązania, które pozwala na eksplorację tematów z wykorzystaniem narzędzi AI i dostępnych źródeł online.

Agent umożliwia:

- formułowanie zapytań badawczych,
- pozyskiwanie informacji z internetu,
- agregowanie wyników,
- oraz ich dalsze przetwarzanie z użyciem modeli językowych i narzędzi pomocniczych.

## 🛠️ Użyte biblioteki

Notebook wykorzystuje następujące biblioteki:

- `litellm` – do komunikacji z modelami językowymi,
- `tavily` – do wyszukiwania informacji w internecie,
- `pydantic_ai` – strukturyzacja danych i walidacja promptów,
- `nest_asyncio`, `IPython.display`, `json`, `os`, `typing`, `dataclasses` – pomocnicze biblioteki do zarządzania kodem i asynchroniczności.

## 🧠 Modele

Notebook wykorzystuje model językowy **`gpt-4o-mini`**, skonfigurowany przez `litellm` oraz używany w konstrukcji agenta badawczego. Model jest osadzony poprzez klasę `OpenAIModel`, co oznacza, że korzysta z API OpenAI i może być łatwo zastąpiony innym wariantem (np. `gpt-3.5-turbo`, `gpt-4`, `gpt-4o`).
