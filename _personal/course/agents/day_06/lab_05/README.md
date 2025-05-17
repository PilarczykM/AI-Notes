# AGI Day 06 Lab 05 – Generowanie i analiza sucharów z lokalnymi LLM

## 🎯 Cel notebooka

Notebook prezentuje system do automatycznego generowania, analizy i ulepszania żartów typu **"dad joke" (sucharów)**. Wykorzystuje współpracę trzech agentów:

- **Kreatora** – generuje oryginalny żart,
- **Parsera** – analizuje żart według ośmiu kryteriów jakości,
- **Sędziego** – ocenia analizę i proponuje poprawioną wersję żartu.

Cały proces odbywa się lokalnie, z wykorzystaniem modeli uruchamianych za pomocą **Ollama**.

---

## 📚 Użyte biblioteki

- `pydantic_ai` – integracja Pydantic z modelami językowymi do walidacji i przetwarzania danych,
- `pydantic` – do definiowania schematów danych i ich walidacji,
- `rich` – do formatowania wyników w estetyczne tabele w konsoli,
- `typing` – typowanie danych w Pythonie.

---

## 🧠 Użyte modele LLM

Notebook wykorzystuje dwa lokalne modele LLM skonfigurowane w klasie `CFG`:

- **deepseek-r1:14b**
- **qwen2.5**

Oba modele są uruchamiane lokalnie za pomocą **Ollama**, co zapewnia pełną kontrolę nad środowiskiem i możliwość działania offline.