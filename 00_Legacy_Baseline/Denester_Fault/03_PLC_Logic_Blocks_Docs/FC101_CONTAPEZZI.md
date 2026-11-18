# `FC101` — `CONTAPEZZI`

- **EN**: HMI terminal interface
- **DE**: Bedienterminal-Schnittstelle

## OEM Revision Header (`CO.RI.M.A. SRL`)

```text
***************************************************************************************************
* PROPRIETA'..........: CO.RI.M.A. SRL                                                            *
*                       via delle Vigne, 8                                                        *
*                       53100 loc. Tognazza (SI) ITALY                                            *
* TIPO MACCHINA.......: MP1                                                                       *
* TIPO DI BLOCCO......: CONTAPEZZI                                                                *
* DESCRIZIONE.........: contati il numero di siringhe in uscita e la velocità di produzione       *
*                                                                                                 *
* VERSIONE............: 0.0 del 3/10/2005                                                         *
* AUTORE..............: BOCCI                                                                     *
* DESCRIZIONE.........: EMISSIONE                                                                 *
*                                                                                                 *
* VERSIONE............: 0.1 del 14/03/2016                                                        *
* AUTORE..............: TRECCI                                                                    *
* DESCRIZIONE.........: REVISIONE: modificate per cambio formato nest 64                          *
*                                                                                                 *
***************************************************************************************************
```

## Block Interface (`VAR_INPUT / VAR_OUTPUT / VAR_TEMP`)

```iecst
VAR_TEMP
  tmp1 : BOOL ;	
  tmp2 : BOOL ;	
  tmp3 : BOOL ;	
  tmp4 : INT ;	
  tmp5 : BOOL ;	
END_VAR
```

## Sequence / Network Titles (Original Italian)

1. `incremento contapezzi`
2. `controllo del conteggio dei pezzi e degli scarti, con la suddivisione del tipo 
di scarto su piu contatori.`
3. `CONTATORE PEZZI ORA`
4. `visualizza tempo`
