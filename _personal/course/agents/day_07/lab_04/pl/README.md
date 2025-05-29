
# AGI Day 07 – AnyAgent z ewaluacją

## Opis

Notebook demonstruje użycie biblioteki **AnyAgent** do tworzenia i testowania agenta AI z wbudowanym narzędziem wyszukiwania informacji w sieci oraz możliwością śledzenia działania (tracing). Przedstawiony jest również proces ewaluacji działania agenta za pomocą predefiniowanego przypadku testowego (`EvaluationCase`).

## Zakres działania

Notebook zawiera:

- Instalację biblioteki `any-agent[all]` z dodatkowymi funkcjonalnościami,
- Konfigurację agenta AI z użyciem klasy `AnyAgent`,
- Wykorzystanie narzędzia `search_web` do rozszerzenia zdolności agenta,
- Zbieranie śladów wykonania z wykorzystaniem `TracingConfig`,
- Zdefiniowanie przypadku ewaluacyjnego (pytanie + oczekiwana odpowiedź + kryteria),
- Ocena działania agenta przez inny model językowy (`llm_judge`) i wyliczenie punktacji.

## Technologie i biblioteki

Notebook wykorzystuje:

- **`any-agent`** – biblioteka do budowy i ewaluacji agentów AI,
- **`search_web`** – narzędzie do pobierania aktualnych informacji z internetu,
- **`evaluate`** – funkcja do oceny jakości odpowiedzi agenta w odniesieniu do tzw. "ground truth",
- **`TracingConfig`** – opcjonalne śledzenie przebiegu działania agenta,
- **`nest_asyncio`** – do poprawnego działania pętli asynchronicznych w środowisku Jupyter.

## Kluczowe komponenty

- `AnyAgent` – główna klasa do tworzenia agenta,
- `AgentConfig` – konfiguracja agenta (model, narzędzia, itd.),
- `EvaluationCase` – definicja przypadku testowego do oceny działania agenta,
- `evaluate()` – funkcja analizująca wynik działania na podstawie metryk jakościowych,
- Model językowy: **`gpt-4o-mini`** – używany zarówno jako silnik agenta, jak i jako sędzia oceniający odpowiedź.

## Przykład

Przypadek testowy dotyczy pytania:
> *"How many seconds would it take for a leopard at full speed to run through Pont des Arts?"*

Ewaluacja oparta jest o:
- zgodność z oczekiwaną wartością (9 sekund),
- wykonanie obliczenia,
- liczba użytych kroków (maks. 5).
