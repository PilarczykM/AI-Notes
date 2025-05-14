# AGI Day 05 - Lab 02: Baza danych

## Cel notebooka

Celem tego notebooka jest demonstracja wykorzystania agentów opartych na dużych modelach językowych (LLM) do wykonywania zadań związanych z bazami danych SQL. Notebook pozwala na analizowanie i wykonywanie zapytań do bazy SQLite za pomocą agentów AI w środowisku CrewAI.

## Użyte biblioteki

Notebook wykorzystuje następujące biblioteki:

- `os` – do operacji na zmiennych środowiskowych.
- `sqlite3` – do interakcji z lokalną bazą danych SQLite.
- `pandas` – do manipulacji i prezentacji danych w formacie DataFrame.
- `textwrap.dedent` – do wygodniejszego formatowania tekstu.
- `crewai` – do tworzenia agentów, zadań i zarządzania ich współpracą.
- `langchain_community.tools.sql_database.tool` – narzędzia do wykonywania zapytań SQL przez agentów.
- `langchain_community.utilities.sql_database` – integracja z bazą danych SQL.
- `langchain_openai.ChatOpenAI` – interfejs do użycia modelu LLM z OpenAI.
- `google.colab.userdata` – bezpieczne zarządzanie danymi użytkownika w Google Colab.

## Użyte modele LLM

W notebooku używany jest model:

- **GPT-4o-mini** – zdefiniowany w klasie `CFG` jako domyślny model językowy dla agentów CrewAI.
