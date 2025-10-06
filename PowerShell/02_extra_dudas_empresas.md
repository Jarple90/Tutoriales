# 🧩 02 - ¿Por qué puede variar la lista de comandos en PowerShell?

## 🔄 1. Dependencia del entorno

PowerShell carga los cmdlets disponibles según los **módulos instalados**.

🔹 En entornos corporativos, puede que solo estén disponibles los módulos aprobados por la empresa.

---

## 🔐 2. Restricciones de seguridad

Algunas empresas limitan el uso de ciertos comandos por **políticas de seguridad**.

🔸 Ejemplos de cmdlets bloqueados:
- Acceso a red
- Modificación de archivos sensibles
- Cambios en el sistema

---

## 🧩 3. Módulos personalizados

Las empresas pueden desarrollar sus **propios módulos** con cmdlets específicos para sus procesos internos.

📦 Ejemplos:
- `Get-LogisticaReporte`
- `Set-InventarioEstado`

---

## 🧬 4. Versiones de PowerShell

Existen diferencias entre versiones:

| Versión             | Características principales                          |
|---------------------|------------------------------------------------------|
| PowerShell 5.1      | Windows PowerShell, más antiguo, aún usado en empresas |
| PowerShell 7+ (Core)| Multiplataforma, más moderno, basado en .NET Core     |

🔸 Algunas empresas siguen usando 5.1 por compatibilidad con sistemas antiguos.

---

## 🧠 ¿Qué puedes hacer tú?

### 🔍 Ver todos los comandos disponibles
```powershell
Get-Command

📦 Ver los módulos cargados

Get-Module

📚 Ver todos los módulos instalados

Get-Module -ListAvailable

🧪 Ver si hay cmdlets personalizados

Busca nombres que no reconozcas o que estén agrupados en módulos internos.

🛡️ Consejo práctico para tu entorno

Como trabajas en logística y automatización:

✅ Identifica qué módulos están disponibles.

📝 Documenta los cmdlets internos si existen.

📦 Valida si puedes instalar módulos útiles como:

ImportExcel

PSReadLine

🧪 Mini práctica recomendada 

1. Explorar todos los comandos disponibles

Get-Command

💡 Usa Get-Command | more para paginar si hay muchos resultados.

2. Ver los verbos aprobados

Get-Verb

📋 Te muestra los verbos estándar usados en cmdlets como Get-Item, Set-Date, etc.

3. Filtrar comandos por verbo o sustantivo

Get-Command -Verb Get
Get-Command -Noun alias*
Get-Command -Verb Get -Noun alias*

🎯 Así puedes ver cómo se agrupan los comandos y detectar patrones.

4. Explorar la ayuda de un comando

Get-Help Get-Process

📚 Ideal para entender qué hace un cmdlet, qué parámetros acepta y ver ejemplos.

5. Ver las propiedades de un objeto

Get-Process | Get-Member

🧬 Muestra todas las propiedades y métodos del objeto devuelto por Get-Process.

🧠 ¿Qué vas a ganar con esto?

🧭 Entender cómo se organizan los comandos en PowerShell.

🕵️‍♂️ Detectar si hay cmdlets personalizados en tu empresa.

🧱 Familiarizarte con el estilo de nomenclatura y estructura de objetos.

🚀 Prepararte para automatizar con más precisión y confianza.

---

✍️ **Autor:** José Antonio Romero Pérez  
🔧 **Rol técnico:** Especialista en automatización logística, reporting y mejora continua con Power Platform  
📁 **Repositorio técnico:** [github.com/Jarple90](https://github.com/Jarple90)  
📅 **Última actualización:** 06/10/2025  
📌 **Licencia de uso:** Este archivo forma parte de una colección de soluciones técnicas reutilizables.  
🔐 **Condiciones:** Uso personal y profesional con atribución. No redistribuir sin permiso explícito.  
📣 **Contacto profesional:** Disponible en GitHub para colaboración, revisión o propuestas de mejora.

---



