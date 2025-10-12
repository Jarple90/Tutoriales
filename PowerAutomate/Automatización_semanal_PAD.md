# 🧭 Automatización semanal con Power Automate Desktop

**Autor**: José Antonio Romero Pérez  
**Firma técnica**: `Jarple90 | Logistics Automation Specialist`  
**Repositorio**: [github.com/Jarple90](https://github.com/Jarple90)

---

## 🎯 Objetivo

Automatizar el envío de un correo electrónico semanal cada lunes a las 9:00 desde Power Automate Desktop, utilizando Outlook como cliente de envío. Este flujo sirve como recordatorio logístico para revisar facturas y actualizar dashboards en Power BI.

---

## 🛠️ Tecnologías utilizadas

- **Power Automate Desktop**
- **Microsoft Outlook**
- **Programador de tareas de Windows**
- **Cuenta de usuario local con permisos de ejecución**

---

## ⚙️ Estructura del flujo

### 1. Iniciar Outlook

```plaintext
Acción: Iniciar Outlook
Variable generada: OutlookInstance

Esta acción abre Outlook y crea una instancia que se usará para enviar el correo.

2. Enviar correo electrónico

Acción: Enviar mensaje de correo electrónico mediante Outlook
Instancia: OutlookInstance
Para: xxxxyyyyzzz@outlook.com (puede ser cualquier dirección, incluyendo Gmail)
Asunto: Hola mundo
Cuerpo: Este es mi mejor app!
Formato: Texto plano (HTML desactivado)
Adjuntos: Ninguno


🗓️ Programación automática

Programador de tareas de Windows
Nombre de la tarea: Recordatorio semanal - Power Automate Desktop 
Frecuencia: Semanal 
Día: Lunes Hora: 09:00 
Acción: Ejecutar flujo de Power Automate Desktop

Comando de ejecución
PAD.Console.Host.exe run --flow "Mi flujo"
🔹 Sustituir "Mi flujo" por el nombre exacto del flujo en Power Automate Desktop (ej. "Main").

🔐 Autenticación

Durante la creación de la tarea, se solicitó la contraseña de la cuenta de Windows (DESKTOP-H2H83IA\jarpl) para permitir la ejecución automática con privilegios.


✅ Validación

El flujo se ejecuta correctamente al iniciar Outlook y enviar el correo.

La tarea programada se activa automáticamente cada lunes a las 9:00.

El correo llega al destinatario sin errores.

📁 Recomendaciones

Documentar cada flujo en Markdown con firma técnica.

Subir capturas y ejemplos al repositorio de GitHub.

Añadir mejoras progresivas: adjuntos, lectura de Excel, compresión de PDFs, integración con Power BI.

🧠 Próximos pasos sugeridos

Añadir adjuntos al correo desde carpeta local.

Leer datos de Excel y generar resumen dinámico.

Comprimir documentos y enviarlos automáticamente.

Integrar con Power Automate Cloud para flujos híbridos.