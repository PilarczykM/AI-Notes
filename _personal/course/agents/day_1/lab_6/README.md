# AGI Day 1 Lab 6: Autonomiczny agent AI z wyszukiwaniem i generowaniem treści

## 📘 Opis
Ten notebook demonstruje wykorzystanie biblioteki `smolagents` do stworzenia małego, autonomicznego agenta AI, który jest w stanie samodzielnie planować i wykonywać zadania wymagające dostępu do internetu i przetwarzania języka naturalnego. Agent korzysta z wyszukiwarki DuckDuckGo oraz modeli językowych do analizy i generowania odpowiedzi.

## 🧠 Cel
Celem notebooka jest:
- Pokazanie, jak zbudować autonomicznego agenta zdolnego do działania w oparciu o językowe polecenia.
- Integracja z narzędziami do wyszukiwania informacji (DuckDuckGo) oraz tworzenia osadzeń semantycznych (`sentence-transformers`).
- Demonstracja użycia gotowych bibliotek jak `smolagents`, `datasets` i `transformers`.

## ✅ Wykonywane zadania
- Instalacja i konfiguracja środowiska z bibliotekami: `smolagents`, `datasets`, `sentence-transformers`, `duckduckgo-search`.
- Uruchomienie agenta, który:
  - Otrzymuje otwarte pytanie (np. o samochód Jamesa Bonda z najnowszego filmu),
  - Wyszukuje potrzebne informacje w sieci,
  - Analizuje wyniki i generuje odpowiedź tekstową lub graficzną.
