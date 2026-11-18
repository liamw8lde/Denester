# `FC99` — `MOT_NEST`

- **EN**: Nest conveyor motor control
- **DE**: Nest-Transportband Motor

## OEM Revision Header (`CO.RI.M.A. SRL`)

```text
***************************************************************************************************
* PROPRIETA'..........: CO.RI.M.A. SRL                                                            *
*                       via delle Vigne, 8                                                        *
*                       53100 loc. Tognazza (SI) ITALY                                            *
* TIPO MACCHINA.......: MP1                                                                       *
* TIPO DI BLOCCO......: MOTORE NASTRO NEST + ENCODER                                              *
* DESCRIZIONE.........: gestione della movimentazione passo nastro nest e lettura encoder per     *
*                       eseguire il posizionamento per il sollevameto siringhe in base al formato *
*                       selezionato. Implementati i dati passo nest per il 100 e il 160.          *
*                                                                                                 *
* VERSIONE............: 0.0 del 3/10/2005                                                         *
* AUTORE..............: BOCCI                                                                     *
* DESCRIZIONE.........: EMISSIONE                                                                 *
*                                                                                                 *
* VERSIONE............: 0.1 del 14/03/2016                                                        *
* AUTORE..............: TRECCI                                                                    *
* DESCRIZIONE.........: REVISIONE: modificate per cambio formato nest 64                          *
*                                                                                                 *
*                                                                                                 *
***************************************************************************************************
```

## Sequence / Network Titles (Original Italian)

1. `abilitazione encoder`
2. `lettura encoder`
3. `lettura encoder macchina`
4. `calcolo posizione arresto nest da 100 con 1 pinza`
5. `calcolo posizione arresto nest da 160 con 1 pinza`
6. `calcolo posizione arresto nest da 160 con 1 pinza`
7. `condizioni partenza nastro`
8. `gestione passo nastro
- start motore
- attende che il sensore sia fuori fase
- attende che il sensore sia in fase
- stop motore`
9. `impulso di fase nastro`
10. `comando passo nastro nest`
11. `partenza nastro`
12. `motore nastro nest`
13. `inverter motore`
14. `controllo movimento motore nastro nest`
15. `fase controllo nastro`
16. `controllo presenza nest`
17. `carico minimo nest`
18. `timer scarico massimo 1`
19. `SCARICO MASSIMO NEST`
