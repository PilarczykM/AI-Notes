# 🧪 GenAI Day 10 Lab 6 – Analiza Bezpieczeństwa Kodu z CodeShield

## 📋 Opis

Notebook pokazuje, jak używać biblioteki **CodeShield** do **automatycznej analizy bezpieczeństwa kodu** wygenerowanego przez modele językowe (np. za pomocą OpenAI). Celem jest wykrycie potencjalnych podatności, takich jak:
- niebezpieczne operacje systemowe,
- brak walidacji danych wejściowych,
- wstrzyknięcia kodu,
- wykorzystanie niezalecanych bibliotek.

Analiza odbywa się **asynchronicznie**, a na podstawie wyników generowana jest rekomendacja działania: **ostrzeżenie** lub **zablokowanie** kodu.

## 📦 Wymagane biblioteki

Notebook korzysta z:

- **`codeshield`** – głównej biblioteki do analizy bezpieczeństwa kodu źródłowego.
- **`openai`** – (potencjalnie) do generowania kodu przy użyciu LLM.
- `asyncio` i składni `async def` do obsługi asynchronicznych zapytań.

## 🧠 Działanie

Główna funkcja notebooka to:
```python
async def scan_llm_output(llm_output_code)
```

Funkcja ta:
- przesyła wygenerowany kod do skanera CodeShield,
- sprawdza, czy kod zawiera problemy bezpieczeństwa,
- podejmuje działanie: ostrzega lub blokuje fragment kodu,
- drukuje podsumowanie, zalecane działanie oraz szczegóły wykrytych problemów.

## 🛡️ Przykładowe użycie

Notebook zawiera symulację analizy kodu, gdzie CodeShield identyfikuje zagrożenia i sugeruje działania prewencyjne. Jest to szczególnie istotne w scenariuszach, gdzie użytkownik końcowy nie weryfikuje treści generowanego kodu – np. w chatbotach programistycznych, agentach AI czy systemach do automatycznego generowania skryptów.
