# AGI Day 02 – Lab 03: Agent LangChain z modelem Cohere i wyszukiwarką

## Opis

Notebook prezentuje wykorzystanie frameworka **LangChain** w połączeniu z dużym modelem językowym **Cohere** oraz narzędziem wyszukiwania internetowego **Tavily**. Demonstruje podejście ReAct (reasoning + acting) do rozwiązywania złożonych zapytań użytkownika poprzez interakcję z różnymi narzędziami.

## Użyte biblioteki

- `langchain`
- `langchain_cohere`
- `langchain_experimental`
- `langchain_community.tools.tavily_search`
- `pydantic`

## Użyty LLM

- **Cohere Command R+** – model językowy od Cohere wykorzystywany w trybie czatu do rozumowania i działania w kontekście zadań.

## Cel notebooka

Celem notebooka jest stworzenie agenta AI w stylu **ReAct**, który potrafi:
- Korzystać z wyszukiwarki internetowej Tavily do zdobywania informacji,
- Wykonywać obliczenia przy użyciu interpreterów kodu Python,
- Integruje wiele narzędzi w ramach jednego procesu rozumowania,
- Odpowiada na pytania użytkownika wymagające wieloetapowej analizy.
