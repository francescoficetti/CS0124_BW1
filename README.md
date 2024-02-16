# Corso Cybersecurity Specialist, Build Week 1

<br /><h2>Traccia</h2><br />
Siamo stati ingaggiati dalla compagnia Theta per eseguire delle valutazioni di sicurezza su alcune delle infrastrutture critiche dei loro data center. Il perimetro delle attività si concentra principalmente su:<br />
  - Un Web server che espone diversi servizi su internet.<br />
  - Un Application server che espone sulla rete interna un applicativo di e-commerce accessibile dai soli impiegati della compagnia Theta.<br /><br />

In base alle informazioni sopra, il capo della sicurezza informatica, ci richiede:<br />
- Di proporre un modello di rete per mettere in sicurezza le due componenti critiche, includendo nell’analisi i dispositivi di sicurezza che potrebbero servire per aumentare la protezione della rete.<br />
- Di effettuare dei test puntuali sulle due componenti critiche per valutarne lo stato di sicurezza.<br />

Nella fattispecie, il CISO ci chiede di effettuare i seguenti controlli:<br />
- Sul Web Server:<br />
  ● Scan dei servizi attivi sulla macchina.<br />
  ● Eventuale enumerazione dei metodi HTTP abilitati sul servizio HTTP in ascolto sulla porta 80.<br />
- Sull'application server:<br />
  ● Enumerazione dei metodi HTTP abilitati.<br />
  ● Valutazione della robustezza della pagina di login agli attacchi di tipo Brute Force.

Il CISO ci ha esplicitamente richiesto di non effettuare nessun test invasivo in ambiente di produzione, quindi gli abbiamo proposto di riprodurre le due componenti nei nostri laboratori, così da poter effettuare i test in sicurezza.<br /><br />


<br /><h2>Risultati attesi</h2><br />
● Design di rete per la messa in sicurezza delle componenti critiche oggetto di analisi.<br />
● Programma in Python per l’enumerazione dei metodi HTTP abilitati su un determinato target.<br />
● Programma in Python per la valutazione dei servizi attivi (port scanning).<br />
● Report degli attacchi Brute Force sulla 'DVWA' per ogni livello di sicurezza.<br />
● Report totale che include i risultati trovati e le contromisure da adottare per ridurre eventuali rischi.<br />
