from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import EmailMessage

def contacto(request):
    formulario_contacto=FormularioContacto()

    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            envio=EmailMessage("Mensaje desde App Django",
            "El usuario con nombre {} con la dirección {} escribe lo siguiente: \n\n {}". format(nombre,email,contenido),
            "",["manubautista2009@gmail.com"],reply_to=[email])

            try:
                envio.send()

                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?error")

    return render(request, "contacto/contacto.html", {'miformulario': formulario_contacto})