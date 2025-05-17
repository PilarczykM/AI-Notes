# agi_day_06_lab_01_autogen_groupchat

## 🎯 Cel projektu

Celem tego laboratorium jest demonstracja wykorzystania biblioteki **AutoGen** do stworzenia i zarządzania zespołem agentów opartych na dużych modelach językowych (LLM), które wspólnie rozwiązują zadania programistyczne. Projekt pokazuje, jak skonfigurować symulowaną grupę składającą się z planera, dewelopera i administratora, która współpracuje nad rozwiązaniem problemu.

## 🧠 Wykorzystywane modele LLM

Zgodnie z konfiguracją w notebooku, do obsługi agentów wykorzystywany jest model:

- **GPT-4.1** (zdefiniowany jako `"model": "gpt-4.1"` w `config_list`)

```python
config_list = [{"model": "gpt-4.1"}]
```

Model ten wykorzystywany jest przez wszystkich agentów w notebooku.

## 🛠️ Użyte biblioteki

Notebook używa następujących bibliotek:

- `autogen` – biblioteka Microsoftu do zarządzania LLM-agentami.
- `networkx` – do wizualizacji i reprezentacji struktur (np. grafów rozmów).
- `matplotlib.pyplot` – do tworzenia wykresów i wizualizacji.
- `pprint` – do estetycznego drukowania struktur danych.
- `google.colab.userdata` – do pobierania klucza API użytkownika.
