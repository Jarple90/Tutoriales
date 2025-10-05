# 🔍 01 - Localización de comandos en PowerShell

## 🧠 ¿Qué es un cmdlet?

Un **cmdlet** (pronunciado *command-let*) es un **comando compilado** que se puede desarrollar en `.NET` o `.NET Core` y ejecutar en PowerShell.

- PowerShell incluye **miles de cmdlets**.
- El reto está en **descubrir qué hacen** y **cómo encontrarlos**.

---

## 🧩 Nomenclatura: Verbo-Sustantivo

Los cmdlets siguen el patrón `Verbo-Sustantivo`, lo que facilita:
- Comprender su función.
- Buscar comandos de forma lógica.
- Mantener consistencia en el desarrollo de nuevos cmdlets.

### 📋 Ejemplo de verbos aprobados (`Get-Verb`)

| Verb   | AliasPrefix | Grupo  | Descripción breve                       |
|--------|-------------|--------|----------------------------------------|
| Add    | a           | Common | Añade un recurso a un contenedor       |
| Clear  | cl          | Common | Elimina todos los recursos de un contenedor |

Los desarrolladores deben usar **verbos aprobados** y asegurarse de que la descripción se ajuste a la función del cmdlet.

---

## 🛠️ Cmdlets clave para explorar comandos

### 🔎 `Get-Command`
Muestra todos los cmdlets disponibles en el sistema.  
✅ Puedes **filtrar** por verbo o sustantivo para localizar comandos específicos.

### 📚 `Get-Help`
Invoca el sistema de ayuda integrado.  
También puedes usar el alias `help` para una lectura paginada.

### 🧬 `Get-Member`
Explora las **propiedades del objeto** devuelto por un comando.  
Ideal para entender la estructura de salida y trabajar con objetos.

---

## 🔍 Filtrado de comandos con `Get-Command`

### 🎯 Filtrar por sustantivo

```powershell
Get-Command -Noun alias*

🔹 Muestra todos los cmdlets cuyo sustantivo comienza por alias.

🎯 Filtrar por verbo y sustantivo

Get-Command -Verb Get -Noun alias*

🔹 Muestra los cmdlets cuyo verbo es Get y el sustantivo comienza por alias.

📌 Puedes usar comodines (*) para buscar coincidencias parciales.

🧠 Concepto clave

PowerShell permite explorar, filtrar y entender los comandos disponibles gracias a su estructura basada en objetos y su sistema de ayuda integrado.

---

