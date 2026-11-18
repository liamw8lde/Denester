# `FC40` — `SYS_TP170_M6`

- **EN**: TP170 HMI interface control
- **DE**: TP170 HMI Schnittstelle

## OEM Revision Header (`CO.RI.M.A. SRL`)

```text
***************************************************************************************************
* PROPRIETA'..........: CO.RI.M.A. SRL                                                            *
*                       via delle Vigne, 8                                                        *
*                       53100 loc. Tognazza (SI) ITALY                                            *
* TIPO MACCHINA.......: TUTTE                                                                     *
* TIPO DI BLOCCO......: INTERFACCIA OPERATORE TP170                                               *
* DESCRIZIONE.........: vengono richiamate tutte le funzioni macchina                             *
*                                                                                                 *
* ISTRUZIONI PER PERSONALIZZAZIONE:                                                               *
*                                                                                                 *
* Segmento 20: Aggiornamento dei campi stringa per scrittura nome programma, data e versione      *
*                                                                                                 *
* Segmento 21: Gestione trasferimento dati FORMATO/LAVAGGIO da DB80 a DB100.                      *
*              E' possibile su alcuni, tutti o nessun dato eseguire il controllo di coerenza dati *
*              prima di eseguire la copia, in caso di dato errato è possibile segnalare esito     *
*              negativo del dato visualizzando un'unica descrizione di errore (Es. codice 12 -    *
*              errore parametri formato) oppure una descrizione per singola variabile utilizzando *
*              altri codici (Es. codice 13, 14, 15, ecc...).                                      *
*              Queste operazioni possone essere fatte per la ricetta FORMATO che per la ricetta   *
*              LAVAGGIO quando presente. I testi di descrizione errore devono essere implementati *
*              sul pannello nelle lista simbolici AVVISI_RICETTA_R1 (R1=riga 1) AVVISI_RICETTA_R2 *
*              e AVVISI_RICETTA_R3 se l'informazione che si vuole visualizzare richiede più righe *
*              altrimenti utilizzare R1 e riempire con spazi R2 e R3.                             *
*                                                                                                 *
* Segmento 22: configurazione del riconoscimento allarmi macchina con pulsante ACK, configurare   *
*              i propri allarmi con l'esigenze della macchina. l'ACK si può eseguire su tutta     *
*              l'area messaggi, mettere bit a 1 nella parola di filtro del messaggio che si deve  *
*              eseguire ACK.  Es. caricare nella parola di filtro sigifica:                       *
*              2#0000_0010_0000_1111 - solo i messaggi corrispondenti a 1 eseguono ACK.           *
*              2#1111_1111_1111_1111 - tutti i messaggi della parola eseguono ACK.                *
*              2#0000_0000_0000_0000 - nessun messaggio esegue ACK                                *
*                                                                                                 *
*                                                                                                 *
* VERSIONE............: 0.0 del 24/02/2004                                                        *
* AUTORE..............: BOCCI                                                                     *
* DESCRIZIONE.........: EMISSIONE                                                                 *
*                       ATTENZIONE: l'azzeramento dei contapezzi e contaore viene fatto dal TP170.*
*                                                                                                 *
* VERSIONE............: 0.1 del 13/04/2004                                                        *
* AUTORE..............: BOCCI                                                                     *
* DESCRIZIONE.........: possibilita eseguire messaggi con ACK.                                    *
*                       Ricavato da Marchesini versione 2.1 del 02/04/2004                        *
*                                                                                                 *
* VERSIONE............: 0.2 del 25/10/2004                                                        *
* AUTORE..............: BOCCI                                                                     *
* DESCRIZIONE.........: inserico controllo:                                                       *
*                       In_JogOn     - lettura marcia impulsi inserita                            *
*                       Out_MesJogOn - messaggio jog inserito                                     *
*                       Out_MesStop  - messaggio macchina pronta a partire                        *
*                                                                                                 *
* VERSIONE............: 0.3 del 4/11/2004                                                         *
* AUTORE..............: TRECCI                                                                    *
* DESCRIZIONE.........: inserito reset bit "InOut_SuonoContinuo" quando con alr o war viene       *
*                       premuto il tasto di reset.          *                                     *                                   c
*                       Inserita gestione parametri selettori a 3 stati "INC-ESC-ALT" (seqmento 2)*
*                                                                                                 *
* VERSIONE............: 0.4 del 31/01/2005                                                        *
* AUTORE..............: BOCCI                                                                     *
* DESCRIZIONE.........: inizializzazione variabile temporanea #IniPointer (segmento 3)            *
*                                                                                                 *
* VERSIONE............: 0.5 del 7/06/2005                                                         *
* AUTORE..............: BARTALINI                                                                 *
* DESCRIZIONE.........: eliminato la gestione di cambio parametri Out_ChanPar dal segmento 2 ed   *
*                       inserita nel segmento 21 al momento di trasferire i dati da DB106 a DB100,*
*                       per evitare il problema di attivazione di Out_ChanPar durante la fase di  *
*                       salvataggio ricetta.                                                      *
*                                                                                                 *
* VERSIONE............: 0.6 del 2/08/2005                                                         *
* AUTORE..............: BARTALINI                                                                 *
* DESCRIZIONE.........: abilitato reset word messaggi in caso pressione del pulsante di reset     *
*                       (segmento 2 riga 34)                                                      *
*                                                                                                 *
***************************************************************************************************
```

## Block Interface (`VAR_INPUT / VAR_OUTPUT / VAR_TEMP`)

```iecst
VAR_INPUT
  In_StatoRun : BOOL ;	//stato run
  In_JogOn : BOOL ;	//jog inserito
  In_RstAlr : BOOL ;	//azzeramento allarmi
END_VAR
VAR_OUTPUT
  Out_MesDatiStandard : BOOL ;	//messaggio dati standard settati
  Out_MesNoRete : BOOL ;	//messaggio assenza rete
  Out_MesManutenzione : BOOL ;	//messaggio manutenzione programmata
  Out_MesRun : BOOL ;	//messaggio macchina in moto
  Out_MesJogOn : BOOL ;	//messaggio jog inserito
  Out_MesStop : BOOL ;	//messaggio macchina pronta a partire
  Out_ChanPar : BOOL ;	//cambio parametri effettuato
  Out_Alarm : BOOL ;	//allarmi attivi
  Out_Warning : BOOL ;	//warning attivi
  Out_Message : BOOL ;	//massaggi attivi
END_VAR
VAR_IN_OUT
  InOut_Alr1 : WORD ;	//allarmi
  InOut_Alr2 : WORD ;	//allarmi
  InOut_Alr3 : WORD ;	//allarmi
  InOut_War1 : WORD ;	//warning
  InOut_War2 : WORD ;	//warning
  InOut_War3 : WORD ;	//warning
  InOut_Mes1 : WORD ;	//messaggi
  InOut_Mes2 : WORD ;	//messaggi
  InOut_SuonoContinuo : BOOL ;	//suono in modo continuo
  InOut_SuonoSingolo : BOOL ;	//suono in modo singolo
END_VAR
VAR_TEMP
  IniPointer : DWORD ;	//Puntatore servizio azzeramento all'accensione
  ServiceRegister : DWORD ;	//Registro di servizio
  SFC0_Retval : INT ;	//Servizio impostazione orodatario
  SFC1_Retval : INT ;	//Servizio lettura orodatario
  VFVarArea : BYTE ;	//Registro tipo area visualizza/comanda variabili
  VFVarDimension : BYTE ;	//Registro dimensione variabile da visualizzare/comandare
  VFVarDB : WORD ;	//Registro numero di DB per visualizza/comanda variabili
  VFVarAddress16 : WORD ;	//Registro puntatore 16 bit per indirizzo visualizza/comanda variabili
  VFVarAddress32 : DWORD ;	//Registro puntatore 32 bit per indirizzo visualizza/comanda variabili
  SFC20_Retval : INT ;	//Registro servizio BLOCKMOVE
  AdrTestMes : DWORD ;	//appoggio indirizzo test messaggi
  OkAck1 : BOOL ;	
  OkAck2 : BOOL ;	
  OkAck3 : BOOL ;	
  OkAck4 : BOOL ;	
  OkAck5 : BOOL ;	
  OkAck6 : BOOL ;	
  AckDone : BOOL ;	
  AlarmSuOp : BOOL ;	
END_VAR
```

## Sequence / Network Titles (Original Italian)

1. `Personalizzazione CORIMA`
2. `---------------------------------------------------------------------------------`
3. `resetto il bit suono continuo`
4. `---------------------------------------------------------------------------------5`
5. `azzera l'area dati che funge da MERKER non ritentivi`
6. `azzeramento messaggi assenza rete`
7. `bit somma di allarmi attivi su macchina`
8. `bit somma di warning attivi su macchina`
9. `bit somma di messaggi attivi su macchina`
10. `suono continuo`
11. `suono singolo`
12. `eliminato in data 7/06/05 e inserita la gestione nel segmento 21&`
13. `comando cambio parametri 1a scansione#`
14. `U     "MERKER".SET_DI_DATI_OK`
15. `=     #Out_ChanPar`
16. `messaggio jog inserito`
17. `messsaggio pronta a partire`
18. `comando azzeramento contapezzi e contaore2`
19. `ATTENZIONE: eseguito da dentro pannello operatore`
20. `INIZIALIZZAZIONE`
21. `---------------------------------------------------------------------------------7`
22. `FC109 del programma MarchesiniQ`
23. `---------------------------------------------------------------------------------`
24. `INIZIALIZZAZIONE DEL BLOCCO`
25. `Azzeramento area d'interfaccia`
26. `Verifica azzeramento terminato`
27. `Incremento puntatore(`
28. `Azzeramento area segnalazioni di allarme`
29. `Verifica azzeramento terminato`
30. `Incremento puntatore+`
31. `Comando messaggio mancanza tensione di rete(`
32. `Inizializzazione registro setup orologio4`
33. `Inizializzazione puntatore visualizzazione variabili`
34. `COMANDO MEMORIA LAMPEGGI`
35. `---------------------------------------------------------------------------------`
36. `CONTROLLO COLLEGAMENTO PLC/OP - COMANDO LED SENDING ERROR`
37. `---------------------------------------------------------------------------------$`
38. `Verifica del bit di attività dell'OP`
39. `Reset bit di avviamento!`
40. `Temporizzazione bit di avviamento`
41. `IMPOSTAZIONE DATA E ORA DI SISTEMA ALL'OP`
42. `---------------------------------------------------------------------------------.`
43. `Verifica richiesta impostazione nuova data/ora?`
44. `Reset memorie di servizio per setup data/ora di sistema dell'OP*`
45. `Richiamo SFC0 per set orologio interno PLC`
46. `Fronte impostazione data/ora`
47. `Verifica nuovo avviamento'`
48. `Verifica impostazione data/ora avvenuta`
49. `Verifica JOB in corso(`
50. `Richiamo SFC1 per aggiornamento orologio`
51. `Impostazione dell'ora$`
52. `Comando del JOB per impostare l'ora`
53. `Impostazione della data%`
54. `Comando del JOB per impostare la data`
55. `COMANDO PAGINA MAIN`
56. `---------------------------------------------------------------------------------%`
57. `Comando memoria avviamento completato.`
58. `Comando del JOB per commutare alla pagina MAIN`
59. `Verifica scollegamento`
60. `GESTIONE LOGOUT PASSWORD`
61. `Verifica livello di password attivo`
62. `Durata abilitazione password7`
63. `Alla scadenza del tempo di durata abilitazione password+`
64. `viene impostata la password di livello ZERO9`
65. `Comando del JOB per impostare la password di livello ZERO`
66. `GESTIONE TEST SEGNALAZIONI DI SERVIZIO`
67. `--------------------------------------------------------------------------------`
68. `Verifica funzione attivata`
69. `Inizializzazione puntatoreB`
70. `Cancellazione preventiva del buffer delle segnalazioni di servizio:`
71. `Verifica underflow puntatore per caricamento messaggio 1287`
72. `Verifica overflow puntatore per caricamento messaggio 13`
73. `Decodifca puntatore per set segnalazione da testare"`
74. `(Ottengo il numero del byte puntato(`
75. `(Se NON ZERO il numero del byte è dispari$`
76. `(Ricompone il puntatore come byte.bit$`
77. `Attiviazione segnalazione da testare`
78. `AGGIORNAMENTO SEGNALAZIONI DI SERVIZIO`
79. `Verifica collegamento stabilito per aggiornamento buffer delle segnalazioni`
80. `GESTIONE RICONOSCIMENTO SEGNALAZIONI DI ALLARME`
81. `Caricamento puntatori"`
82. `(Ottengo il numero del byte puntato(`
83. `(Se NON ZERO il numero del byte è dispari$`
84. `(Ricompone il puntatore come byte.bit`
85. `Verifica messaggio stato ON`
86. `Il messaggio è OFF:C`
87. `Verifica se richiede il riconoscimento per cancellazione bit di ACK`
88. `Il messaggio è ON:#`
89. `Verifica se richiede riconoscimento`
90. `E' richiesto il riconoscimento:$`
91. `Verifica se è già stato riconosciuto`
92. `Comando segnalazione di allarme=`
93. `Verifica bit di conferma attivato per impostazione bit di ACK`
94. `À(.`
95. `Incremento puntatore per completamento ricerca`
96. `Verifica fine ricerca3`
97. `GESTIONE COMMUTAZIONE PAGINA DI ACETTAZIONE ALLARMI.`
98. `Comando del JOB per commutare alla pagina MAIN`
99. `GESTIONE ELABORAZIONE DEL SET DI DATI`
100. `---------------------------------------------------------------------------------1`
101. `VERIFICA RICHESTA DI ELABORAZIONE DEL SET DI DATI`
102. `Azzeramento registro avvisi)`
103. `COMANDO CONSENSO ELABORAZIONE SET DI DATI`
104. `( "SET_DI_DATI_RDY"-`
105. `VERIFICA RICHIESTA MEMORIZZAZIONE SET DI DATI5`
106. `VERIFICA RICHIESTA IMPOSTAZIONE SET DI DATI OPERATIVO'`
107. `VERIFICA ESITO ELABORAZIONE SET DI DATI`
108. `VERIFICA DATI VALIDI5`
109. `VERIFICA RICHIESTA IMPOSTAZIONE SET DI DATI OPERATIVO"`
110. `COMANDO MEMORIZZAZIONE SET DI DATI`
111. `GESTIONE CONTAORE`
112. `---------------------------------------------------------------------------------`
113. `Secondi totali e parziali`
114. `Verifica overflow secondi totali`
115. `Incrmento minuti totali`
116. `Verifica overflow minuti totali"`
117. `Verifica overflow secondi parziali`
118. `Incremento minuti parziali`
119. `Verifica overflow minuti totali`
120. `GESTIONE MANUTENZIONE PERIODICA`
121. `---------------------------------------------------------------------------------#`
122. `Verifica ore manutenzione trascorse`
123. `Ore manutenzione non trascorse:`
124. `Decremento conta-tempo`
125. `Ore manutenzione trascorse:`
126. `Incremento conta-tempo`
127. `Verifica overflow dei secondi`
128. `Incremento minuti`
129. `Verifica overflow dei minuti`
130. `Incremento ore#`
131. `Verifica ore manutenzione trascorse6`
132. `Ore trascorse: predisposizione del conteggio in avanti`
133. `Verifica underflow dei secondi`
134. `Decremento minuti`
135. `Verifica underflow dei minuti`
136. `Decremento ore`
137. `Comando segnalazione4`
138. `Abilitazione alla funzione di azzeramento contatempo`
139. `GESTIONE TIMER BASE TEMPI 1 SECONDO`
140. `---------------------------------------------------------------------------------`
141. `GESTIONE CONTROLLO VARIABILI`
142. `---------------------------------------------------------------------------------)`
143. `VERIFICA ABILITAZIONE CAMPI PER FORZATURA#`
144. `VERIFICA ATTIVAZIONE DELLA FUNZIONE`
145. `SCOMPOSIZIONE PUNTATORE OPERANDO`
146. `À(6`
147. `Verifica esistenza variabile da visualizzare / forzare(`
148. `Dimensione area di memoria (Byte / Word)`
149. `Tipo area di memoria`
150. `Identificazione numero del DB1`
151. `DETERMINAZIONE PUNTATORE INDIRIZZO DA CONTROLLARE`
152. `AREA DB$`
153. `Verifica visualizzazione o forzatura(`
154. `Verifica dimensione dell'area di memoria`
155. `Forzatura byte indicizzato`
156. `Forzatura word indicizzata`
157. `À((`
158. `Verifica dimensione dell'area di memoria`
159. `Visualizzazione byte indicizzato`
160. `Visualizzazione word indicizzata`
161. `AREA MERKER$`
162. `Verifica visualizzazione o forzatura(`
163. `Verifica dimensione dell'area di memoria`
164. `Forzatura byte indicizzato`
165. `Forzatura word indicizzata`
166. `À((`
167. `Verifica dimensione dell'area di memoria`
168. `Visualizzazione byte indicizzato`
169. `Visualizzazione word indicizzata`
170. `AREA INPUT(`
171. `Verifica dimensione dell'area di memoria`
172. `Visualizzazione byte indicizzato`
173. `Visualizzazione word indicizzata`
174. `AREA OUTPUT(`
175. `Verifica dimensione dell'area di memoria`
176. `Visualizzazione byte indicizzato`
177. `Visualizzazione word indicizzata`
178. `AREA TIMER!`
179. `Visualizzazione timer indicizzato`
180. `AREA COUNTER$`
181. `Verifica visualizzazione o forzatura`
182. `Forzatura counter indicizzato`
183. `À(#`
184. `Visualizzazione counter indicizzato`
185. `AGGIORNAMENTO VARIABILE`
186. `À(6`
187. `INCREMENTO PUNTATORE PER NUOVA RIGA DI VISUALIZZAZIONE`
188. `VERIFICA FINE TABELLA%`
189. `CARICAMENTO PUNTATORE PER NUOVO CICLO`
190. `GESTIONE FORZATURA USCITE`
191. `VERIFICA ATTIVAZIONE DELLA FUNZIONE`
192. `COMANDO FORZATURA ATTIVATA'`
193. `CARICAMENTO PUNTATORE BYTE DA COMANDARE`
194. `SALVATAGGIO STATO DELLE USCITE`
195. `AZZERAMENTO STATO DELLE USCITE'`
196. `CARICAMENTO PUNTATORE BYTE DA COMANDARE`
197. `ATTIVAZIONE FORZATURA`
198. `VERIFICA FUNZIONE TERMINATA'`
199. `CARICAMENTO PUNTATORE BYTE DA COMANDARE`
200. `RIPRISTINO STATO DELLE USCITE`
201. `GESTIONE AVVISI TEMPORIZZATI`
202. `---------------------------------------------------------------------------------)`
203. `Durata visualizzazione della segnalazione`
204. `Spegnimento della segnalazione`
205. `GESTIONE ORDINI OP`
206. `---------------------------------------------------------------------------------`
207. `Verifica ordine terminato`
208. `AGGIORNAMENTO VERSIONE SOFTWARE OP`
209. `---------------------------------------------------------------------------------2`
210. `OB1 - del programma Marchesini`
211. `<< DA CONFIGURARE SECONDO LE NECESSITA PROPRIE DELLA MACCHINA DALL'OPERATORE >>Q`
212. `---------------------------------------------------------------------------------5`
213. `allaccensione setta le versioni programmi installati`
214. `Numero di programma,`
215. `(Numero di caratteri della stringa (fisso 12)4`
216. `(Numero massimo di caratteri della stringa (fisso 12).`
217. `(Primi 4 caratteri della stringa partendo da SX"`
218. `(4 caratteri centrali della stringa`
219. `(Ultimi 4 caratteri della stringa`
220. `Versione`
221. `Data giorno,mese`
222. `Data anno`
223. `GESTIONE ELABORAZIONE RICETTE (FORMATO / LAVAGGIO)`
224. `VERIFICA RICHESTA DI ELABORAZIONE DEL SET DI DATI`
225. `---------------------------------------------------`
226. `FORMATO3`
227. `---------------------------------------------------`
228. `VERIFICA NUMERO DI RICETTA (1=FORMATO / 2=LAVAGGIO)(`
229. `L     "HMI".BUFFER_RICETTA.Ricetta`
230. `L     1`
231. `==I`
232. `SPBN  SD2(`
233. `Se esiste una sola ricetta (Es. FORMATO)`
234. `SPBN  SDKO`
235. `FORMATO:U`
236. `VERIFICA RICHIESTA DI MEMORIZZAZIONE SET DI DATI PER CARICAMENTO BUFFER DELLA RICETTA/`
237. `U     "LAVORO".FORMATO.Includi.Formato1609`
238. `=     "HMI".BUFFER_RICETTA.D03_Selettori.Formato160`
239. `CONTROLLO DATI VALIDI ALL'INTERNO DEL BUFFER DELLA RICETTA`
240. `Parametro 10`
241. `L     "HMI".BUFFER_RICETTA.D07_PercentCarMax0`
242. `L     "HMI".BUFFER_RICETTA.D06_PercentCarMin`
243. `SPB   S1K1`
244. `SEGNALAZIONE ESITO POSITIVO ELABORAZIONE SET DI DATI5`
245. `VERIFICA RICHIESTA IMPOSTAZIONE SET DI DATI OPERATIVO(`
246. `RICHESTA IMPOSTAZIONE FORMATO OPERATIVO:B`
247. `TRASFERIMENTO DAL BUFFER DELLA RICETTA ALLA TABELLA DATI DI LAVORO`
248. `U     "HMI".BUFFER_RICETTA.D03_Selettori.Formato160/`
249. `=     "LAVORO".FORMATO.Includi.Formato160`
250. `AGGIORNAMENTO NUMERO E NOME DEL FORMATO OPERATIVO`
251. `SEGNALAZIONE ESITO POSITIVO IMPOSTAZIONE SET DI DATI`
252. `---------------------------------------------------`
253. `ERRORE3`
254. `---------------------------------------------------`
255. `SEGNALAZIONE ESITO NEGATIVO MEMORIZZAZIONE / IMPOSTAZIONE SET DI DATIc`
256. `E' possibile visulizzare un unica descrizione di errore (Es. codice 12 Errore parametri di formato)I`
257. `oppure una desrizione per gruppi di errori (Es. codici 13, 14, 15 ecc...)`
258. `ERRORE PARAMETRI FORMATO`
259. `S1K1: L     12`
260. `SPA   SDKO`
261. `FORMATO Parametro 2`
262. `S1K2: L     13`
263. `SPA   SDKO`
264. `FORMATO Parametro 3`
265. `S1K3: L     14`
266. `SPA   SDKO`
267. `ERRORE RICETTA`
268. `FUNZIONAMENTO CON DATI STANDARD`
269. `ESEMPIO DI CONFIGURAZIONE RICONOSCIMENTO ALLARMI MACCHINA`
270. `Impostare a 1 i bit dell'area DB106.DBB240 - DB106.DBB255 dove si vuole che il
messaggio corrispondente venga riconosciuto per abilitarne la cancellazione.
Volendo riconoscere i messaggi 1, 65 e 127 vedere l'esempio seguente.`
271. `--------------------------------------------------------------------------`
272. `Richiesta riconoscimento messaggi`
273. `L     2#1111111111111111`
274. `( allarmi`
275. `( allarmi`
276. `( allarmi`
277. `( warning`
278. `( warning`
279. `( warning`
280. `( messaggi`
281. `( messaggi`
282. `ESEMPIO FUNZIONE DI RESET`
283. `La funzione di reset deve essere eseguita a macchina ferma e se la 
comunicazione con il display è stata stabilita. Nell'esempio seguente è
previsto l'azzeramento di numerosi messaggi che richiedono il riconoscimento.`
284. `(Pulsante di RESET`
285. `(Memoria collegamento PLC-OP`
286. `(Memoria di macchina in moto`
287. `AZZERAMENTO 1° WORD MESSAGGI`
288. `( ack fatto`
289. `( swap byte per visualizzazione`
290. `( word allarmiN`
291. `( Maschera 1=allarmi che non devono essere azzerati dal reset ma dalla macchina`
292. `( maschera allarmi(`
293. `( Azzeramento di tutti gli altri messaggi`
294. `AZZERAMENTO 2° WORD MESSAGGI`
295. `( ack fatto`
296. `( swap byte per visualizzazione`
297. `( word allarmiN`
298. `( Maschera 1=allarmi che non devono essere azzerati dal reset ma dalla macchina`
299. `( maschera allarmi(`
300. `( Azzeramento di tutti gli altri messaggi`
301. `AZZERAMENTO 3° WORD MESSAGGI`
302. `( ack fatto`
303. `( swap byte per visualizzazione`
304. `( word allarmiN`
305. `( Maschera 1=allarmi che non devono essere azzerati dal reset ma dalla macchina`
306. `( maschera allarmi(`
307. `( Azzeramento di tutti gli altri messaggi`
308. `AZZERAMENTO 4° WORD MESSAGGI`
309. `( ack fatto`
310. `( swap byte per visualizzazione`
311. `( word allarmiN`
312. `( Maschera 1=allarmi che non devono essere azzerati dal reset ma dalla macchina`
313. `( maschera allarmi(`
314. `( Azzeramento di tutti gli altri messaggi`
315. `AZZERAMENTO 5° WORD MESSAGGI`
316. `( ack fatto`
317. `( swap byte per visualizzazione`
318. `( word allarmiN`
319. `( Maschera 1=allarmi che non devono essere azzerati dal reset ma dalla macchina`
320. `( maschera allarmi(`
321. `( Azzeramento di tutti gli altri messaggi`
322. `AZZERAMENTO 6° WORD MESSAGGI`
323. `( ack fatto`
324. `( swap byte per visualizzazione`
325. `( word allarmiN`
326. `( Maschera 1=allarmi che non devono essere azzerati dal reset ma dalla macchina`
327. `( maschera allarmi(`
328. `( Azzeramento di tutti gli altri messaggi-`
329. `Azzeramento delle memorie di arresto macchina.`
330. `solo se le cause che richiedono riconoscimento$`
331. `sono state confermate dall'operatoreC`
332. `R     #Out_Alarm                  //Memoria arresti immediati@`
333. `R     #Out_Warning                //Memoria arresti logici`
334. `ESEMPIO INCREMENTO CONTAORE / SEGNALAZIONE MACCHINA IN MOTO`
335. `(Memoria macchina in moto`
336. `(Memoria per incremento contaore`
337. `(Messaggio MACCHINA IN MOTO`
338. `ESEMPIO ABILITAZIONE ALLA PROGRAMMAZIONE`
339. `La programmazione del display deve essere abilitata a macchina ferma`
340. `(Memoria macchina in moto`
341. `(Abilitazione alla programmazione`
342. `ultimo passo`
