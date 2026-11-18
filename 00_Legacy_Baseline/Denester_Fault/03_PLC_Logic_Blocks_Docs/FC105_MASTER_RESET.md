# `FC105` — `MASTER_RESET`

- **EN**: Master reset control
- **DE**: Master-Reset Steuerung

## OEM Revision Header (`CO.RI.M.A. SRL`)

```text
***************************************************************************************************
* PROPRIETA'..........: CO.RI.M.A. SRL                                                            *
*                       via delle Vigne, 8                                                        *
*                       53100 loc. Tognazza (SI) ITALY                                            *
* TIPO MACCHINA.......: MP1                                                                       *
* TIPO DI BLOCCO......: MASTER RESET                                                              *
* DESCRIZIONE.........: gestione per inizializzare la macchina nella condizione di riposo in caso *
*                       di perdita globale dei dati, il master reset viene eseguito all'accensione*
*                       macchina solo se sono stati mantenuti premuti i tasti di START e STOP     *
*                       contemporaneamente durante l'accensione macchina.                         *
*                                                                                                 *
* VERSIONE............: 0.0 del 3/10/2005                                                         *
* AUTORE..............: BOCCI                                                                     *
* DESCRIZIONE.........: EMISSIONE                                                                 *
*                                                                                                 *
* VERSIONE............: 0.1 del 14/03/2016                                                        *
* AUTORE..............: TRECCI                                                                    *d
* DESCRIZIONE.........: REVISIONE: modificate per cambio formato nest 64                          * c
*                                                                                                 *
*                                                                                                 *
*                                                                                                 *
***************************************************************************************************
```

## Sequence / Network Titles (Original Italian)

1. `master reset passi sequenza`
2. `master reset handshake sequenze`
3. `master reset stato pistoni`
4. `comando estrattore siringhe avanti`
5. `comando estrattore siringhe alto`
6. `memoria master reset in corso`
