# AGI Day 1 Lab 5: Agent AI z zarządzaniem stanem i planowaniem wieloetapowym

## 📘 Opis
Notebook przedstawia rozszerzenie koncepcji agenta AI z poprzednich laboratoriów o elementy zarządzania stanem (pamięcią) oraz wieloetapowego planowania. Agent korzysta z modelu **Cohere** oraz wbudowanych funkcji, takich jak symulacja kalendarza, by wykonywać złożone zadania krok po kroku, w tym równoległe działania.

## 🧠 Cel
Celem notebooka jest:
- Pokazanie, jak budować agenta, który:
  - Wykonuje zadania sekwencyjne (multi-step),
  - Przeprowadza działania równoległe (parallel),
  - Zachowuje kontekst i pamięć stanu (state management).
- Integracja modelu językowego z funkcją zewnętrzną `list_calendar_events` – służącą do zarządzania wydarzeniami kalendarzowymi.
- Przećwiczenie pracy agenta z kontekstem i planowaniem zadań.

## ✅ Wykonywane zadania
- Tworzenie agenta obsługującego zapytania o dostępność w kalendarzu.
- Symulacja różnych trybów działania agenta:
  - Brak planowania,
  - Planowanie krokowe,
  - Planowanie równoległe,
  - Zachowanie stanu konwersacji.
