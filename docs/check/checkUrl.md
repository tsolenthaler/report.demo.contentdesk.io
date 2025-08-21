# Check Url valid

Prüft ob die URL / Domain "noch" funktioniert


## Ablauf

```mermaid
flowchart TD
    subgrah Contentdesk
        Export --> Objects
        Objects --> CheckUrlExist
        CheckUrlExist -->|Yes| AddToCheckObjects
        CheckUrlExist -->|No| IgnoreObjects
        AddToCheckObjects --> sendHTTPRequest
        sendHTTPRequest -->|Status kleiner als 400| AddToOkObjects
        sendHTTPRequest -->|Status grösser als 400| AddToFalseObjects
```