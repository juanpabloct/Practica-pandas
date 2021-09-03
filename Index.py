"""Diccionario_estudiantes = {
    'Nombre': 'Juan',
    'Apellido': 'Castellanos',
    'notas': {
        'ingles': 40,
        'matematicas': 42,
        'sociales': 45}
}
table1 = pd.DataFrame(Diccionario_estudiantes, index=[
                      'ingles', 'matematicas', 'sociales'])
table1.index.name = 'Materias'
table1.columns.name = 'FEEE'
informacion_personas = [{
  'nombre': 'Julio',
  'apellido': 'Jaramillo',
  'canciones favoritas': {
      'pop': {
          'Robin schuls':['Spechless', 'all this love', 'Rather be alone'],
          'coldplay': ['fly on', 'The scientist', 'Yellow']
      },
      'electronica':{
          'shouse': ['Love Tonight', 'Into it'],
          'math simons':['Catch & Releases', 'We Can Do Better']
      }
  }
},
{
    'nombre':'Camila',
    'apellido':'suarez',
    'canciones favoritas':{
        'pop':{
        'Deorro':['I can be somebody', 'Five Hours', 'Five More Hours'],
        'will sparks':['Ah Yeah so what', 'Techno Viking']
        },
        'electronica':{
            'axwell & ingrosso':['More than you kmown', 'Dreamer', 'I love you']
        }
    }

}
]
table_gustos_musicales=pd.DataFrame(informacion_personas)
print(table_gustos_musicales)"""