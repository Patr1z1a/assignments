
# aepy-oo_inheritance


OO, Inheritance, Encapsulation, InformationHiding -- SimpleBank
---------------------------------------------------------------

Implementieren Sie eine minimalistische Bank-Anwendung zur Verwaltung von Bankkonten (`oo_inheritance.py`).

Ihre Implementierung soll so gestaltet sein, dass die bereitgestellten Tests funktionieren. Hinweise: Anhand von etwaigen Fehlermeldungen der Tests bzw. auch gemäß Demo-Code können Sie auf die erwartete Benennung bzw. Reihenfolge von Variablen schließen.

Schreiben Sie hierzu eine Klasse `Account`, welche ein Bankkonto darstellt. Ein Bankkonto besitzt folgende Attribute: `owner` (der Name des Konto-Inhabers; `string`) und `balance` (der aktuelle Kontostand; `float`). 
Accounts haben initial einen Kontostand von 0. Der Konto-Inhaber soll im Konstruktor übergeben und gesetzt werden.

Weiters, soll es die Möglichkeit zum Einzahlen (`deposit(amount)`) und Abheben (`withdraw(amount)`) von Geld auf/von Konten geben. Duch eine Einzahlung bzw. Abhebung verändert sich der Kontostand.

Es soll nicht möglich sein, negative Werte beim Einzahlen bzw. Abheben zu übergeben (insbesondere soll z.B. eine Abhebung von -100 nicht zu einer Erhöhung des Kontostandes führen) .

Der Kontostand kann durch eine Abhebung auch negativ werden und beliebig lange negativ bleiben und durch weitere Abhebungen noch negativer werden. Sprich: Der Überziehungsrahmen ist quasi unendlich.

Der Kontostand eines Kontos soll abfragbar sein. Jedoch soll der Kontostand nicht direkt veränderbar sein (dies soll lediglich über die deposit/withdraw-Funktionalität erlaubt sein).

Zusätzlich bietet die Bank auch Studentenkonten `StudentAccount` an. Bei Studentenkonten ist es nicht erlaubt, ins Minus zu kommen (Überziehungsrahmen: 0). Würde eine Abbuchung zu einem Überziehen des Kontos führen, wird Sie nicht durchgeführt. Überlegen Sie, wie Ihr Programm auf eine solche versuchte Abbuchung am besten reagieren könnte. Ansonsten verhalten sich Studentenkonten wie normale Konten.

Zwischen zwei Konten (gilt für `Account` und `StudentAccount`) können mittels der Methode `transfer(amount, fromAccount, toAccount)` Überweisungen durchgeführt werden. Die Methode `transfer` soll eine mittels `@staticmethod` dekorierte Methode sein. Der Überweisungsbetrag führt bei einem Konto zu einer Abbuchung, während er beim anderen Konto zu einer Einzahlung führt. Achten Sie auf richtiges Verhalten bzw. gültige Kontostände (Achtung bei der Beteiligung von einem Studentenkonto)!

**Wichtig:**
* Nutzen Sie für die Umsetzung von Studentenkonten das Mittel der **Vererbung (Inheritance)**.
* Nutzen Sie die Prinzipien von **Encapsulation** und **Information hiding** (bzw. was Ihnen sonst noch sinnvoll erscheint):
Insbesondere soll balance intern mit einer PRIVATE (nicht protected!) Variable umgesetzt sein. Verwenden Sie die Namenskonventionen aus der Lecture für etwaige decorator.
* Sollte die gegebene "Spezifikation" nicht 100% eindeutig sein, treffen Sie geeignete Annahmen (und dokumentieren Sie diese im Code).

