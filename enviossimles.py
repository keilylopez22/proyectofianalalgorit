#Crear un programa en python que envie emails simples usando la consola.
import smtplib
import os
import sys

#Crear un objeto smtp
smpt_objecto = smtplib.SMTP("smtp.gmail.com", 587)
contrasena = os.getenv('GOOGLE_APP_PASS')
usuario = os.getenv("GOOGLE_APP_EMAIL")


def enviar_correo_simple(asunto, mensaje, destinatario):
    smpt_objecto.starttls()
    smpt_objecto.login(usuario, contrasena)
    smpt_objecto.sendmail("Notificaciones algoritmos", destinatario,f"Subject: {asunto} \n{mensaje}" )

enviar_correo_simple("Hola", "Buen dia", "kl8679967@gmail.com")