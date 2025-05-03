# 🧪 GenAI Day 10 Lab 4 – OpenAI API & Data Validation with Pydantic

## 📋 Opis

Notebook demonstruje bezpieczne korzystanie z **OpenAI API** w połączeniu z walidacją danych wejściowych i wyjściowych za pomocą **Pydantic**. Umożliwia budowanie interakcji z modelem (np. GPT-4o) w sposób zgodny z założoną strukturą danych – przydatne m.in. w tworzeniu aplikacji, agentów czy narzędzi automatyzujących decyzje.

## 📦 Wymagane biblioteki

Notebook wykorzystuje:

- **`openai`** – oficjalna biblioteka do interakcji z modelami językowymi OpenAI.
- **`pydantic`** – służy do walidacji i strukturyzacji danych (wejściowych i wyjściowych).
- **`google.colab.userdata`** – do bezpiecznego uwierzytelniania w Colabie.
- **`typing`** – do definiowania typów danych, m.in. z `Literal`.

## 🧠 Model

Notebook korzysta z modelu:
```
gpt-4o-mini
```

Jest to model językowy używany do generowania odpowiedzi zgodnych z kontekstem, nad którymi następnie czuwa walidator.

## 🛡️ Funkcjonalności

Notebook zawiera:
- Konfigurację parametrów odpowiedzi (np. liczba tokenów).
- Tworzenie klas Pydantic opisujących oczekiwane struktury danych.
- Przesyłanie promptów do modelu i odbieranie odpowiedzi.
- Walidację odpowiedzi z modelu przy pomocy Pydantic.
- Obsługę błędów walidacyjnych.

## 🧪 Przykładowe użycie

Notebook zawiera konkretne przykłady interakcji, w których:
- Model proszony jest o wygenerowanie danych w określonym formacie (np. lista produktów, JSON z zadaniami).
- Odpowiedź jest walidowana – jeśli nie spełnia wymagań, zostaje odrzucona lub przetworzona ponownie.
