# CheckOpeningHoursSpecification

Prüft und vergleicht Öffnungszeiten eines Objekts im Contentdesk mit den Öffnungszeiten auf der Webseite.
Mit unterstützung von AI (OpenAI).

## AI Task

Die AI durchsucht die Webseite nach Öffnungszeiten und gibt diese als schema.org/openingHoursSpecification zurück, wenn diese vorhanden sind.
Ansonsten wir null/none zurückgegeben.

AI liefert zudem die URL zurück, wo die Öffnungszeiten gefunden wurden. Damit dies geprüft/verglichen werden kann.

## Ablaufdiagramm

```mermaid
flowchart TD
    A[Starte Prüfung] --> A1[Liste von geprüften Objekten mit URL]
    A1 --> B[{{fa:robot}} Öffnungszeiten auf Webseite suchen mit AI]
    B -- Ja --> C[{{fa:robot}} Extrahiere Öffnungszeiten mit AI]
    B -- Nein --> D[Gib null/none zurück]
    C --> E[Vergleiche mit Contentdesk]
    D --> E
    E --> F[Ergebnis anzeigen]
```