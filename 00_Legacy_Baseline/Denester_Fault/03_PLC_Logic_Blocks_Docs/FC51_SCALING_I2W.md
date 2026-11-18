# `FC51` — `SCALING_I2W`

- **EN**: Analog scaling INT to WORD
- **DE**: Analogwert-Skalierung

## OEM Revision Header (`CO.RI.M.A. SRL`)

```text
***************************************************************************************************
* PROPRIETA'..........: CO.RI.M.A. SRL                                                            *
*                       via delle Vigne, 8                                                        *
*                       53100 loc. Tognazza (SI) ITALY                                            *
* TIPO MACCHINA.......: TUTTE                                                                     *
* TIPO DI BLOCCO......: SCALING DI GRANDEZZE                                                      *
* DESCRIZIONE.........: la funzione viene utilizzata per convertire in modo lineare un valore di  *
*                       ingresso decimale (INT) in valore di uscita binario (WORD), il rusultato  *
*                       viene calcolato utilizzando la seguente formula:                          *
*                       YRESULT=Y2-[(Y2-Y1)/(X2-X1)*(X2-XSOURCE)]                                 *
*                       attenzione: non impostare X2=X1 e Y2=Y1                                   *
*                                                                                                 *
* VERSIONE............: 0.0 del 20/10/2002                                                        *
* AUTORE..............: BOCCI                                                                     *
* DESCRIZIONE.........: EMISSIONE                                                                 *
*                                                                                                 *
***************************************************************************************************
```

## Block Interface (`VAR_INPUT / VAR_OUTPUT / VAR_TEMP`)

```iecst
VAR_INPUT
  X1 : INT ;	//ingresso asse X1
  X2 : INT  := 100;	
  Y1 : WORD ;	
  Y2 : WORD  := W#16#100;	
  XSOURCE : INT ;	
END_VAR
VAR_OUTPUT
  YRESULT : WORD ;	
END_VAR
VAR_TEMP
  OFF_Y : REAL ;	
  OFF_X : REAL ;	
  RISOLUZ : REAL ;	
  DELTAX : REAL ;	
  DELTAY : DINT ;	
END_VAR
```

## Sequence / Network Titles (Original Italian)

1. `Y2(WORD)-Y1(WORD)=OFF_Y(REAL)`
2. `X2(INT)-X1(INT)=OFF_X(REAL)`
3. `OFF_Y(REAL)/OFF_X(REAL)=RISOLUZ(REAL)`
4. `X2(INT)-XSOURCE(INT)=DELTAX(REAL)`
5. `RISOLUZ(REAL)*DELTAX(REAL)=DELTAY(DINT)`
6. `Y2(INT)-DELTAY(DINT)=YRESULT(WORD)`
