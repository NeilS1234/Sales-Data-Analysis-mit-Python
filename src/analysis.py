import os
import matplotlib.pyplot as plt
import pandas as pd

print("src:", os.getcwd())
print("data:", os.listdir())

df = pd.read_csv("data/sales.csv")

print(df.head())

# Umsatz berechnen
df["Revenue"] = df["Sales"] * df["Quantity"]

# 1. Wichtige Kennzahlen berechnen
gesamtumsatz = df["Revenue"].sum()
gesamtmenge = df["Quantity"].sum()
durchschnittlicher_umsatz = df["Revenue"].mean()

print("=== Wichtige Kennzahlen ===")
print("Gesamtumsatz:", gesamtumsatz)
print("Verkaufte Gesamtmenge:", gesamtmenge)
print("Durchschnittlicher Umsatz pro Datensatz:",
      round(durchschnittlicher_umsatz, 2))

# Ordner für die Diagramme erstellen
os.makedirs("output", exist_ok=True)

# 2. Diagramm: Umsatz pro Produkt
umsatz_pro_produkt = df.groupby("Product")["Revenue"].sum()

umsatz_pro_produkt.plot(
    kind="bar",
    title="Umsatz pro Produkt"
)
plt.ylabel("Umsatz")
plt.xlabel("Produkt")
plt.tight_layout()
plt.savefig("output/umsatz_pro_produkt.png")
plt.show()
plt.close()

# 3. Diagramm: Verkaufte Menge pro Monat
menge_pro_monat = df.groupby("Month")["Quantity"].sum()

menge_pro_monat.plot(
    kind="line",
    marker="o",
    title="Verkaufte Menge pro Monat"
)
plt.ylabel("Verkaufte Menge")
plt.xlabel("Monat")
plt.tight_layout()
plt.savefig("output/verkaufte_menge_pro_monat.png")
plt.show()
plt.close()

# 4. Diagramm: Umsatz pro Monat
umsatz_pro_monat = df.groupby("Month")["Revenue"].sum()

umsatz_pro_monat.plot(
    kind="bar",
    title="Umsatz pro Monat"
)
plt.ylabel("Umsatz")
plt.xlabel("Monat")
plt.tight_layout()
plt.savefig("output/umsatz_pro_monat.png")
plt.show()
plt.close()

# 5. Wichtige Muster und Auffälligkeiten
print("\n=== Umsatz pro Produkt ===")
print(umsatz_pro_produkt)

print("\n=== Umsatz pro Monat ===")
print(umsatz_pro_monat)

# Datensatz mit dem höchsten Umsatz finden
hoechster_umsatz = df.loc[df["Revenue"].idxmax()]

print("\n=== Verkauf mit dem höchsten Umsatz ===")
print(hoechster_umsatz)

# 6. Ergebnisse anhand der Daten
bestes_produkt = umsatz_pro_produkt.idxmax()
bester_monat = umsatz_pro_monat.idxmax()

print("\n=== Ergebnisse der Analyse ===")
print("Produkt mit dem höchsten Umsatz:", bestes_produkt)
print("Monat mit dem höchsten Umsatz:", bester_monat)

# 7. Annahmen und Einschränkungen
print("\n=== Annahmen und Einschränkungen ===")
print("- Sales wird als Preis pro Einheit angenommen.")
print("- Der Umsatz wird aus Preis mal Menge berechnet.")
print("- Kosten, Rabatte und Rückerstattungen werden nicht berücksichtigt.")
print("- Die Ergebnisse hängen von den verfügbaren Daten ab.")

print("\nAnalyse abgeschlossen!")