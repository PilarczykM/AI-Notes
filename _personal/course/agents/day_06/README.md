# AGI Day 06 – Laboratoria z agentami LLM

## 🎯 Cel dnia szkoleniowego

Celem dnia szkoleniowego AGI Day 06 było praktyczne zapoznanie się z wykorzystaniem **agentów opartych na dużych modelach językowych (LLM)** do różnych zastosowań: od pracy zespołowej agentów, przez generowanie wykresów i obrazów, po przeszukiwanie dokumentów i analizę humorystycznych tekstów. Uczestnicy mieli okazję pracować z bibliotekami takimi jak `autogen`, `crewai`, `pydantic_ai` i lokalnymi modelami przez `Ollama`.

Każdy notebook stanowi niezależne laboratorium prezentujące inne możliwości wykorzystania agentów LLM.

---

## 🧪 Lista laboratoriów

1. [Lab 01 – Autogen GroupChat](lab_01/README.md)  
   Wprowadzenie do pracy zespołowej agentów LLM w strukturze grupy (planer, developer, admin).  
   → **Model**: GPT-4.1  
   → **Biblioteka**: autogen

2. [Lab 02 – System wizualizacji z agentami Autogen](lab_02/README.md)  
   Iteracyjne tworzenie i ulepszanie wykresów danych przez zespół agentów.  
   → **Model**: gpt-4o-mini  
   → **Biblioteka**: autogen

3. [Lab 03 – Generowanie obrazów z agentami Autogen](lab_03/README.md)  
   Generowanie i krytyczna ocena obrazów z wykorzystaniem DALL·E i agentów multimodalnych.  
   → **Modele**: dalle, gpt-4-turbo, gpt-4o-mini  
   → **Biblioteka**: autogen

4. [Lab 04 – System RAG z agentami CrewAI](lab_04/README.md)  
   Przetwarzanie zapytań i analiza PDF-ów za pomocą zestawu agentów CrewAI w systemie Retrieval-Augmented Generation.  
   → **Modele**: gpt-4o-mini, BAAI/bge-small-en-v1.5  
   → **Biblioteki**: crewai, langchain

5. [Lab 05 – Generowanie i analiza sucharów z lokalnymi LLM](lab_05/README.md)  
   Lokalne modele generujące i analizujące żarty typu "dad joke" w iteracyjnym procesie z trzema agentami.  
   → **Modele**: deepseek-r1:14b, qwen2.5  
   → **Biblioteki**: pydantic_ai, rich, ollama

---

Każde laboratorium pozwala rozwijać kompetencje związane z projektowaniem, konfiguracją i zastosowaniem agentów LLM w różnych kontekstach aplikacyjnych.