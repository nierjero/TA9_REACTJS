
def eliminar_emails() :
  emails = {"Martín Rodríguez":["arodri@ucu.edu.uy", "rodriguez@gmail.com"], "Marcela Rodríguez":["mleites@gmail.com", "rodriguez@gmail.com"], "Juan Lamas":["jlamasucu.edu.uy", "juan.lamas@gmail.com"]}
  listadelistas_emails = list(emails.values())
  lista_nombres = list(emails.keys())
  for lista in listadelistas_emails :
    for email in lista :
      if "@" not in email or "." not in email :
        lista.remove(email)
  
  print(listadelistas_emails)
  print(lista_nombres)
eliminar_emails()