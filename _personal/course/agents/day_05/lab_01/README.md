# AGI Day 05 - Lab 01: Filozofia

## Cel notebooka

Celem tego notebooka jest eksploracja koncepcji sztucznej inteligencji ogólnej (AGI) w kontekście filozoficznym, przy użyciu agentów opartych na dużych modelach językowych (LLM). Notebook umożliwia symulację dyskusji filozoficznej między agentami o różnych "osobowościach", reprezentującymi różne nurty filozoficzne.

## Użyte biblioteki

Notebook korzysta z następujących bibliotek:

- `crewai` – do definiowania i zarządzania agentami oraz ich współpracą w ramach zadań.
- `os` – do operacji systemowych, takich jak pobieranie zmiennych środowiskowych.
- `google.colab.userdata` – do bezpiecznego przechowywania i pobierania danych użytkownika w środowisku Google Colab.

## Użyte modele LLM

Notebook korzysta z modelu językowego:

- **GPT-4o-mini** – wariant modelu GPT-4o dostarczany przez OpenAI, przypisany w klasie `CFG`.
