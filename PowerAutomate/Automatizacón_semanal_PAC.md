# ☁️ Automatización semanal con Power Automate Cloud

**Autor**: José Antonio Romero Pérez  
**Firma técnica**: `Jarple90 | Logistics Automation Specialist`  
**Repositorio**: [github.com/Jarple90](https://github.com/Jarple90)

---

## 🎯 Objetivo

Automatizar el envío de un correo electrónico cada lunes a las 9:00 desde Power Automate Cloud, utilizando Outlook 365 como servicio de envío. Este flujo sirve como recordatorio logístico para revisar facturas y actualizar dashboards en Power BI.

---

## 🛠️ Tecnologías utilizadas

- **Power Automate Cloud (portal.office.com → Power Automate)**
- **Outlook 365 (conector integrado)**
- **Microsoft 365 (cuenta empresarial)**
- **Trigger programado (Recurrencia)**

---

## ⚙️ Estructura del flujo

### 1. Desencadenador: Recurrencia

```plaintext
Tipo: Programado
Frecuencia: Semanal
Día: Lunes
Hora: 09:00 (zona horaria configurada)

Este trigger inicia el flujo automáticamente cada lunes a las 9:00.

2. Acción: Enviar correo electrónico (Outlook 365)

Conector: Outlook 365
Para: xxxyyyzzz@outlook.com (puede ser cualquier dirección, incluyendo Gmail)
Asunto: Recordatorio semanal: revisión de facturas
Cuerpo:
Hola José,  
Recuerda revisar las facturas recibidas y actualizar el dashboard de Power BI.  
¡Buen inicio de semana!

Formato: HTML activado (opcional)
Adjuntos: Ninguno (por ahora)

✅ Validación

El flujo se ejecuta automáticamente sin intervención manual.

El correo llega al destinatario cada lunes a las 9:00.

Se puede monitorizar desde el historial de ejecuciones en Power Automate Cloud.

📁 Recomendaciones

Añadir condiciones para enviar el correo solo si hay nuevas facturas.

Incluir adjuntos desde OneDrive o SharePoint.

Integrar con Power BI para actualizar datasets.

Usar variables y plantillas para personalizar el mensaje.

🧠 Próximos pasos sugeridos

Añadir paso de compresión de documentos antes de enviar.

Leer datos desde Excel en OneDrive y generar resumen.

Integrar con Power Automate Desktop para procesamiento local (flujo híbrido).

Documentar cada flujo en Markdown con firma técnica y capturas.
