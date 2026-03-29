

## RESEARCH / PROJECT QUESTION

## Title: “Comparative Study of JSON and Pickle for Data Serialization in Python with Real-World Applications”

## Problem Statement

Develop a Python system to:

1.  Serialize and deserialize data using:
    -   JSON
    -   Pickle
2.  Compare:
    -   Performance
    -   Security
    -   Portability
3.  Demonstrate:
    -   API-style JSON usage
    -   Limitations of JSON
    -   Risks of Pickle

----------

## Objectives

### A. Functional Tasks

-   Store and retrieve:
    -   Dictionary
    -   List
    -   Custom class

----------

### B. API Simulation

-   Convert data → JSON string
-   Simulate sending/receiving data

----------

### C. Error Handling

-   Handle:
    -   Invalid JSON
    -   Unsupported data types

----------

### D. Security Study

-   Show why Pickle is unsafe
-   Show safe JSON usage

----------

## ANSWER (CONCEPTUAL)

### Key Findings

-   JSON:
    -   Portable, safe, widely used
-   Pickle:
    -   Powerful but unsafe
-   APIs use JSON because:
    -   Language-independent
    -   Text-based

## Comparison Table

| Feature | JSON | Pickle | Use Case |
| --- | --- | --- | --- |
| Portability | High | Low | APIs |
| Security | High | Low | Web |
| Object Support | Limited | Full | Python apps |
| Speed | Medium | High | Internal storage |


### Final Insight 

> Use **JSON** for:

-   APIs
-   Web
-   Data exchange

> Use **Pickle** for:

-   Python-only programs
-   Complex object storage









