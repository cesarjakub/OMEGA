# OMEGA
- **Název projektu**: Library management
- **Autor**: Jakub César
- **Email**: cesar@spsejecna.cz
- **LinkedIn**: [LinkedIn - Jakub César](https://tr.linkedin.com/in/jakub-c%C3%A9sar-714584243)
- **Github**: [Github - Jakub César](https://github.com/cesarjakub)
    - **Github odkaz na repozitář projektu**: [Github - repo](https://github.com/cesarjakub/OMEGA)
- **Datum vypracování**: 18.04.2024
- **Škola**: Střední průmyslová škola elektrotechnická, Praha 2, Ječná 30 
- **Projekt**: Jedná se o školní projekt

## Popis používání
- Po [instalaci a puštění programu](#instalace-a-spuštění-aplikace).
- Si stáhneme ve složce `DATABASE/library_managemente.sql`
a nahrajeme ho do **SQL server Management Studio** a spustíme script (script obsahuje již demo data) a vytvoříme uživatele následně přepíšeme [configurační soubor](#nastavení-config-souboru) aby vše odpovídalo.
- Pokud je vše správně nastavené tak po spuštění se na obrazovce objeví hlavní menu aplikace.
  - Zde už vybíríme z nabídky po levé starně.

## Popis architektury
- Three tier architektura
  - Popis: Tento vzor rozděluje aplikaci na tři základní části - Database tier (logika a data), Presentation tier (uživatelské rozhraní) a Application tier (řídící logika).
  - Využití: MVC by mohl být použit pro oddělení logiky databáze a uživatelského rozhraní. 
- Data Access Object (DAO):
  - Popis: Poskytuje abstrakci nad datovým uložištěm a umožňuje přístup k datům bez znalosti jejich podrobností.
  - Využití: DAO můžeš použít pro oddělení logiky přístupu k databázi od zbytku aplikace.

## E-R diagram
- Logické schéma databáze

  1. see [here](DATABASE/logical_schema.pdf) 

- Relační schéma databáze

  2. see [here](DATABASE/relational_schema.pdf)


## Nastavení config souboru
- Po [instalaci](#instalace-a-spuštění-aplikace) si otevřeme složku `Config/`
- Zde se nachází soubor `config_main.json`, který vypadá takto:
```json
{
  "database": {
    "server": "******",
    "DATABASE": "******",
    "UID": "******",
    "PWD": "******"
  }
}
```
- Database část obsahuje configuraci databáze tedy než pustíme aplikaci musíme nakonfigurovat databázi
    - **server**: název serveru zde je lokální je **třeba přepsat na svůj server** 
    - **DATABASE**: název databáze můžeme nechat 
    - **UID**: název uživatele (vytvoříme v databázi poté přepíšeme jméno zde)
    - **PWD**: heslo pro uživatele (vytovoříme v databázi poté přepíšeme heslo zde)

## Instalace a Spuštění aplikace
- **Instalace**
    - máme 2 možnosti: 
        1) stáhneme si zdrojový kód z githubu [odkaz víše](#omega)
    
- **Spuštění bez vývojového prostředí**
    - Nejpreve si zkontrolujme jestli jsem nastavili vše správně v [config souboru](#nastavení-config-souboru)
    - Otevřete si v **cmd**(Příkazovým řádeku) složku *ALpha_3* a pomocí příkazu:
    ```commandline
    python .\main.py
    ```
     - poté nám program běží

## Chybové stavy
- Chyba může nastat při pokusu připojení do databáze
  - Řešení:
    1) kontrola configu zda jsou informace správně napsané
- Ostatní chyby by měly být řešeny přímo v aplikaci tedy neměla by nastat žádná s kterou by si uživatel nevěděl rady

## Knihovy třetích stran
- knihovny:
    - **requests** knihovna
    - **qrcode** knihovna
    - **pyodbc** knivovna
    - **reportlab** knihovna
    - **customtkinter** knivovna
    - **CTkMessagebox** knihovna
    - **configparser** knihovna

## Závěr
- Projekt využívá knihovny třetích stran, jako jsou *pyodbc* pro připojení k databázi a standardní knihovny jako *json*, *sys*, *uuid*, *datetime*, a *os*, což přispívá k efektivnímu vývoji a spolehlivosti aplikace.
- Tento databázový systém je otevřený dalšímu rozšíření pro danou problematiku e-receptů
- Tento projekt, poskytuje aplikaci pro správu knihoven.
- Závěrem lze říci, že tento databázový systém je snaha o modernizaci knihovního systému
