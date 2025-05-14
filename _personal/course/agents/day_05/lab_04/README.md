# AGI Day 05 - Lab 04: Przygotowanie do spotkania

## Cel notebooka

Notebook demonstruje zastosowanie agentów AI do **przygotowania się do spotkania** – poprzez wyszukiwanie informacji, analizę tematów oraz planowanie przebiegu rozmowy. Celem jest wykorzystanie potencjału agentów opartych na LLM do wspomagania zadań wymagających przygotowania merytorycznego i kontekstowego.

## Użyte biblioteki

Notebook wykorzystuje:

- `streamlit` – do tworzenia prostego interfejsu użytkownika.
- `crewai` – do definiowania agentów, zadań i całej "załogi" (Crew).
- `crewai.process` – do zarządzania procesem współpracy agentów.
- `crewai_tools.SerperDevTool` – do wyszukiwania informacji w sieci.
- `os` – do pobierania kluczy API i innych zmiennych środowiskowych.

## Użyte modele LLM

Notebook korzysta z modelu:

- **GPT-4o-mini** – używanego bezpośrednio w konfiguracji agentów CrewAI.
