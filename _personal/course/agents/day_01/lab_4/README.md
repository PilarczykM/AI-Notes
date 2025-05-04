# AGI Day 1 Lab 4: Agent AI wykorzystujący modele Cohere i narzędzia zewnętrzne

## 📘 Opis
Ten notebook prezentuje sposób budowy agenta AI opartego na modelu **Cohere command-r-plus**, który potrafi wykonywać złożone polecenia z wykorzystaniem tzw. "tool use" — integracji z funkcjami zewnętrznymi. Agent może analizować dane i podejmować decyzje na podstawie wyników pozyskanych z zewnętrznych źródeł.

## 🧠 Cel
Celem notebooka jest:
- Pokazanie integracji modelu językowego Cohere z funkcjami zewnętrznymi.
- Zbudowanie prostego agenta, który korzysta z narzędzi do przetwarzania danych.
- Przećwiczenie interakcji modelu językowego z własnymi funkcjami użytkownika.

## ✅ Wykonywane zadania
- Konfiguracja modelu **Cohere command-r-plus**.
- Definicja i rejestracja dwóch zewnętrznych narzędzi:
  - `daily_sales_report` – symuluje pobieranie danych sprzedażowych z bazy danych.
  - `product_lookup` – umożliwia agentowi uzyskanie informacji o produktach.
- Implementacja agenta wykorzystującego te narzędzia do odpowiadania na złożone pytania, np.:
  - „Który produkt sprzedał się najlepiej w poniedziałek?”
  - „Ile sztuk produktu X sprzedano ostatnio?”
- Demonstracja pracy modelu z planowaniem kroków i wnioskowaniem na podstawie danych z narzędzi.
