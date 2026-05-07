from django.shortcuts import render, redirect, get_object_or_404 #render e redirect - mostrare e reinderizzare pg html
from django.db import connection #connessione per usare query dirette a db
from ..models.model_utente import Utente
from ..models.model_testimonianza import Testimonianza
from ..forms.form_utente import UtenteForm
from ..forms.form_testimonianza import TestimonianzaForm
from django.contrib.admin.views.decorators import staff_member_required # permette l'accesso solo admin
from django.views.decorators.http import require_POST #permette solo richieste post quindi azione solo su tasto premuto


def home(request):
        if request.method == 'POST': #controlla form
            form = UtenteForm(request.POST) 
            if form.is_valid():  #controlla dati validi
                utente = form.save() #salva dati 
                request.session['utente_id'] = utente.id #salva id
                return redirect('testimonianza') #ti rimanda a testimonianza
        else:
            form = UtenteForm()

        return render(request, 'home.html', {'form': form}) #in fine ritorni home


def testimonianza(request):
    utente_id = request.session.get('utente_id')  #recupera id  

    if not utente_id:               #se non esiste id torna home
        return redirect('home')

    if request.method == 'POST': #controlla form
        form = TestimonianzaForm(request.POST)
        if form.is_valid():      #controlla dati validi
            t = form.save(commit=False)  #salva dati 
            t.utente_id = utente_id #collega testimonianza a id
            t.save() #salva nel db
            return redirect('conferma')  # si va pagina conferma
    else:
        form = TestimonianzaForm() #se richiesta non è form allora 

    return render(request, 'testimonianza.html', {'form': form}) #mostra pagina testimonianza


def conferma(request):
    return render(request, 'conferma.html') #mostra pagina conferma 


@staff_member_required(login_url='/login/') #solo gli admin possono accedere 
def pannello_admin(request):
    query  = request.GET.get('q', '').strip() #prende paramentro di ricerca 

    ordine = request.GET.get('ordine', '-id')  #prende il parametro dell ordine

    ordini_validi = {
        'id':     'testimonianza.id ASC',
        '-id':    'testimonianza.id DESC',
        'nome':   'utente.nome ASC',            #mostra i possibili ordini
        '-nome':  'utente.nome DESC',
        'stato':  'testimonianza.stato ASC',
        '-stato': 'testimonianza.stato DESC',
    }

    # Se l'ordine richiesto è valido lo usa, altrimenti usa id DESC
    order_sql = ordini_validi.get(ordine, 'testimonianza.id DESC')

    with connection.cursor() as cursor:  #connessione diretta con il database
        if query: # se il db esiste allora fai la query
            sql = f"""
                SELECT
                    testimonianza.id,
                    utente.nome,
                    utente.cognome,
                    utente.cell_email,
                    utente.regione,
                    testimonianza.testo,
                    testimonianza.stato
                FROM femminicidioapp_testimonianza AS testimonianza
                JOIN femminicidioapp_utente AS utente
                  ON testimonianza.utente_id = utente.id
                WHERE utente.nome    LIKE %s
                   OR utente.cognome LIKE %s
                   OR testimonianza.testo LIKE %s
                ORDER BY {order_sql}
            """
            like = f'%{query}%' # %% serve per vedere i valori in qualisiasi campo sia davanti che alla fine che in mezzo
            #like serve per trovare dei parametri simili

            cursor.execute(sql, [like, like, like]) #riga per la sicurezza sql injection 

        else:
            sql = f"""
                SELECT
                    testimonianza.id,
                    utente.nome,
                    utente.cognome,
                    utente.cell_email,
                    utente.regione,
                    testimonianza.testo,
                    testimonianza.stato
                FROM femminicidioapp_testimonianza AS testimonianza
                JOIN femminicidioapp_utente AS utente
                  ON testimonianza.utente_id = utente.id
                ORDER BY {order_sql}
            """
            cursor.execute(sql) #esegue query

        colonne = [col[0] for col in cursor.description] #Prende i nomi delle colonne restituiti dalla query
        #Converte ogni riga del risultato in una lista di dizionari
        testimonianze = [dict(zip(colonne, row)) for row in cursor.fetchall()] #[complicata da rifare mi sono fatto aiutare]


    return render(request, 'pannello_admin.html', {     # Mostra la pagina pannello_admin passando i dati
        'testimonianze': testimonianze,
        'query':         query, 
        'ordine':        ordine,
    })


@staff_member_required(login_url='/login/') #di nuovo solo admin
@require_POST           #e solo richieste post
def aggiorna_stato(request, pk):
    t = get_object_or_404(Testimonianza, pk=pk)  # cerca testim per id se no err 404
    nuovo_stato = request.POST.get('stato') #prende stato form
    stati_validi = ['in_attesa', 'accettata', 'rifiutata']  #lista stati validi
    if nuovo_stato in stati_validi: # se valido
        t.stato = nuovo_stato
        t.save() #salva db
    return redirect(request.META.get('HTTP_REFERER', 'pannello_admin')) #torna all pagina precedente o pannadmin