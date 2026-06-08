'''
  Positional-Only Parameters (/) e Keyword-Only Arguments (*)
  *args (ilimitado de argumentos posicionais)
  **kwargs (ilimitado de argumentos nomeados)
  🟢 Positional-only Parameters (/) - Tudo antes da barra deve
  ser ❗️APENAS❗️ posicional.
  PEP 570 – Python Positional-Only Parameters
  https://peps.python.org/pep-0570/
  🟢 Keyword-Only Arguments (*) - Valendo só depois do *, c
  PEP 3102 – Keyword-Only Arguments
  https://peps.python.org/pep-3102/

  tudo antes da barra deve ser posicional
  tudo depois do asterisco deve ser nomeado
  na chamada da função
'''
def soma(a, b, /, *, c, **kwargs):
    print(kwargs)
    print(c)
    print(a + b + c)


soma(1, 2, c=3, nome='teste')