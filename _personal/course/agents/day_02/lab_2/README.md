# AGI Day 02 – Lab 02: Agent z obsługą terminala i modelem Ollama

## Opis

Ten notebook prezentuje nowoczesne podejście do budowy agenta AI, który integruje modele językowe **OpenAI** oraz **Ollama**, z możliwością interakcji z lokalnym terminalem systemowym. Umożliwia to wykonywanie poleceń systemowych i korzystanie z lokalnie uruchomionych modeli, co daje dużą elastyczność i niezależność od zewnętrznych API.

Dzięki wykorzystaniu frameworku **LlamaIndex**, agent może zarządzać działaniami, delegować zadania do terminala i korzystać z lokalnych modeli LLM w środowisku Colab.

## Użyte biblioteki

- `llama-index` – główny framework do budowy agentów i aplikacji opartych o LLM.
- `llama-index-llms-openai` – integracja modeli OpenAI (np. GPT-4) z LlamaIndex.
- `llama-index-llms-ollama` – integracja z lokalnymi modelami obsługiwanymi przez serwer Ollama.

## Użyty LLM

- **Gemma 3 4B (przez Ollama)** – lokalny model językowy uruchamiany przez serwer Ollama. Pozwala na wydajne działanie bez konieczności użycia usług chmurowych.

## Przypadek użycia

W tym notebooku agent AI potrafi:

- Uruchamiać komendy w terminalu Google Colab dzięki integracji z `colab-xterm`,
- Korzystać z modeli LLM uruchamianych lokalnie (np. Gemma 3 4B przez Ollama),
- Rozsądnie delegować zadania do OpenAI lub Ollama w zależności od potrzeb,
- Wspierać hybrydowe scenariusze interakcji z użytkownikiem i systemem.
