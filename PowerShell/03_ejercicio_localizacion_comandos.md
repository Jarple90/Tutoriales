# 🧠 Localización de comandos en PowerShell  
**Aplicación práctica en entornos logísticos**

---

## 🎯 Objetivo del ejercicio

Aprender a localizar cmdlets en PowerShell mediante el uso de filtros por **nombre** (`-Noun`) y **acción** (`-Verb`), con el fin de identificar comandos útiles para tareas específicas como la gestión de archivos en entornos empresariales.

---

## 🧩 Contexto técnico

En entornos como logística, donde se procesan informes, documentos y registros de entregas, es fundamental automatizar tareas como:

- Validación de archivos
- Generación de logs
- Clasificación y desbloqueo de documentos

PowerShell permite localizar rápidamente los comandos adecuados para cada tarea mediante el cmdlet `Get-Command`.

---

## 🔍 Ejemplo práctico: Gestión de archivos

### 1. Buscar cmdlets relacionados con archivos

```powershell
Get-Command -Noun File*


Cmdlet          Get-FileHash
Cmdlet          Out-File
Cmdlet          Unblock-File

2. Filtrar por acción específica (por ejemplo, "Get")

Get-Command -Verb Get -Noun File*

📄 Resultado esperado:

Cmdlet          Get-FileHash

⚙️ Aplicación en la empresa

✅ Validación de archivos recibidos

Get-FileHash "C:\Logistica\InformeTransportista.xlsx"

Verifica que el archivo no ha sido modificado.

Permite comparar versiones de documentos.

Puede integrarse en flujos de Power Automate para automatización preventiva.

✅ Generación de logs automáticos

"Archivo procesado correctamente" | Out-File "C:\Logs\procesos.txt" -Append

Registra eventos en tiempo real.

Facilita trazabilidad y auditoría interna.

✅ Desbloqueo de archivos descargados

Unblock-File "C:\Descargas\documento.pdf"

Evita errores por restricciones de seguridad.

Útil para automatizar la preparación de archivos antes de su uso.

📁 Recomendación para repositorio técnico

Estructura sugerida para tu GitHub:

📁 powershell-logistica/
├── scripts/
│   ├── validar_hash_archivos.ps1
│   ├── generar_log_archivo.ps1
│   ├── desbloquear_archivos.ps1
├── docs/
│   ├── localizacion_cmdlets.md
│   ├── manual_tecnico.md


🚀 Conclusión

Este enfoque te permite explorar PowerShell de forma segura, localizar comandos útiles según el escenario y documentar soluciones reutilizables. Es una base sólida para construir automatizaciones aplicables en cualquier empresa, reforzando tu perfil técnico en logística y mejora continua.


---

✍️ **Autor:** José Antonio Romero Pérez  
🔧 **Rol técnico:** Especialista en automatización logística, reporting y mejora continua con Power Platform  
📁 **Repositorio técnico:** [github.com/Jarple90](https://github.com/Jarple90)  
📅 **Última actualización:** 06/10/2025  
📌 **Licencia de uso:** Este archivo forma parte de una colección de soluciones técnicas reutilizables.  
🔐 **Condiciones:** Uso personal y profesional con atribución. No redistribuir sin permiso explícito.  
📣 **Contacto profesional:** Disponible en GitHub para colaboración, revisión o propuestas de mejora.

---



