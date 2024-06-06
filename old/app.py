from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
    return 'Luis Jair Escalante Cruz - 20200770 - 9A'

@app.route('/prueba', methods=['GET'])
def prueba():
    return ( 
        '<body>'
        '<script src="https://cdn.tailwindcss.com"></script>'
            '<div class="flex flex-col items-center my-10 justify-center">'
                '<div class="bg-white p-10 rounded-md flex flex-col shadow-2xl md:w-3/5">'
                    '<div class="flex justify-center"><img src="https://registro.uthh.edu.mx/images/uthh.png" class="w-40 mb-5"/></div>'
                    '<ul>'
                        '<li><p class="font-bold text-lg text-center">INGENIERÍA EN DESARROLLO Y GESTIÓN DE SOFTWARE</p></li>'
                        '<li><p id="name" class="font-bold text-xl text-gray-500">Nombre: Luis Jair Escalante Cruz</p></li>'
                        '<li><p class="font-bold text-xl text-gray-500">Grado: 9</p></li>'
                        '<li><p class="font-bold text-xl text-gray-500">Grupo: A</p></li>'
                    '</ul>'
                    '<form class="mt-5 flex flex-col md:grid md:grid-cols-2 gap-3">'
                    '<h3 class="text-center font-bold text-xl col-span-2">Calcular promedio</h3>'
                        '<div class="flex flex-col">'
                            '<label>Administracion de proyectos TI</label>'
                            '<input class="px-1 ring-2 ring-gray-200 hover:ring-blue-400 rounded-sm" id="admin" type="number">'
                        '</div>'
                        '<div class="flex flex-col">'
                            '<label>Extraccion de conociemiento</label>'
                            '<input class="px-1 ring-2 ring-gray-200 hover:ring-blue-400 rounded-sm" id="base" type="number">'
                        '</div>'
                        '<div  class="flex flex-col">'
                            '<label>Desarrollo web integral</label>'
                            '<input class="px-1  ring-2 ring-gray-200 hover:ring-blue-400 rounded-sm" id="web" type="number">'
                        '</div>'
                        '<div class="flex flex-col">'
                            '<label>Dispositivos inteligentes</label>'
                            '<input class="px-1 ring-2 ring-gray-200 hover:ring-blue-400 rounded-sm" id="disp" type="number">'
                        '</div>'
                        '<div class="flex flex-col">'
                            '<label>Ingles VIII</label>'
                            '<input class="px-1 ring-2 ring-gray-200 hover:ring-blue-400 rounded-sm" id="ingles" type="number">'
                        '</div>'
                        '<div class="flex flex-col">'
                            '<label>Direccion de equipo</label>'
                            '<input class="px-1 ring-2 ring-gray-200 hover:ring-blue-400 rounded-sm" id="direcc" type="number">'
                        '</div>'
                    '</form>'
                    '<div class="flex flex-col bg-gray-400 text-white rounded-sm font-bold py-2"><button id="button">Calcular</button></div>'
                '</div>'
            '</div>'
        '<script>'
        'document.addEventListener("DOMContentLoaded", () => { const btn = document.getElementById("button");let ingles = document.getElementById("ingles");let web = document.getElementById("web");let base = document.getElementById("base");let admin = document.getElementById("admin");let direcc = document.getElementById("direcc");let disp = document.getElementById("disp");btn.addEventListener("click", async() => {let suma = parseInt(ingles.value) + parseInt(web.value) +parseInt(base.value) + parseInt(admin.value) + parseInt(direcc.value)+ parseInt(disp.value);let promedio = suma / 6;alert("Tu promedio es: "+promedio);});});'
        '</script>'
        '</body>'
    )

if __name__ == '__main__':
    app.run(debug=True)