# AGI Day 05 - Lab 05: Hierarchiczne Agenty

## Cel notebooka

Celem tego notebooka jest przedstawienie struktury **hierarchicznej współpracy agentów AI**, w której różne role (np. lider, analitycy, wykonawcy) współpracują przy realizacji złożonych zadań. Przykład ukazuje, jak można wykorzystać CrewAI do budowania złożonych struktur agentowych rozwiązujących rzeczywiste problemy poprzez analizę danych z różnych źródeł.

## Użyte biblioteki

Notebook korzysta z następujących bibliotek:

- `os` – do ustawiania kluczy API i zmiennych środowiskowych.
- `crewai` – do definiowania agentów, zadań i ich współpracy (w tym `LLM`, `Agent`, `Crew`, `Process`, `Task`).
- `crewai_tools` – do wykorzystania narzędzi:
  - `FileReadTool` – do czytania plików tekstowych.
  - `ScrapeWebsiteTool` – do ekstrakcji danych ze stron WWW.
  - `SerperDevTool` – do wyszukiwania informacji w internecie.
- `crewai.tools.BaseTool` – baza do tworzenia własnych narzędzi.
- `google.colab.userdata` – bezpieczne zarządzanie danymi użytkownika.
- `loguru` – zaawansowane logowanie do debugowania.
- `datetime` – operacje na datach i godzinach.
- `pydantic.Field` – walidacja danych i definicje pól klas.
- `langchain_community.tools.DuckDuckGoSearchRun` – alternatywne narzędzie wyszukiwania.

## Użyte modele LLM

Notebook wykorzystuje model:

- **GPT-4o-mini** – ustawiony w konfiguracji klasy `CFG` jako domyślny model dla agentów AI.
