# `FC102` — `PISTONI`

- **EN**: Valve outputs control
- **DE**: Ventilausgaenge Steuerung

## OEM Revision Header (`CO.RI.M.A. SRL`)

```text
***************************************************************************************************
* PROPRIETA'..........: CO.RI.M.A. SRL                                                            *
*                       via delle Vigne, 8                                                        *
*                       53100 loc. Tognazza (SI) ITALY                                            *
* TIPO MACCHINA.......: MP1                                                                       *
* TIPO DI BLOCCO......: PISTONI                                                                   *
* DESCRIZIONE.........: vengono controllati tutti i pistoni macchina                              *
*                                                                                                 *
* VERSIONE............: 0.0 del 3/10/2005                                                         *
* AUTORE..............: BOCCI                                                                     *
* DESCRIZIONE.........: EMISSIONE                                                                 *
*                                                                                                 *
***************************************************************************************************
```

## Block Interface (`VAR_INPUT / VAR_OUTPUT / VAR_TEMP`)

```iecst
VAR_TEMP
  Vel_X : INT ;	
  Vel_Y : INT ;	
  Anag_X : INT ;	
  Anag_Y : INT ;	
  Ferma : BOOL ;	
  EsegueFerma : BOOL ;	
  CambioRack : BOOL ;	
  Fonica : INT ;	
END_VAR
```

## Sequence / Network Titles (Original Italian)

1. `comando pinza`
2. `comando sollevatore`
3. `comando sollevamento guida estrazione siringhe`
4. `comando avanzamento guida estrazione siringhe`
5. `comando posizionatore esteso`
6. `comando asse x`
7. `gestione asse X 
accelerazione, velocita' lineare, decelerazione`
8. `comando asse y`
9. `gestione asse Y 
accelerazione, velocita' lineare, decelerazione`
10. `passo fittizio`
