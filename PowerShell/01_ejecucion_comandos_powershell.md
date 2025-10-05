# ⚙️ 01 - Ejecución de los primeros comandos de PowerShell

## 🧪 Entorno de práctica: Azure Cloud Shell

En este ejercicio se utiliza **Azure Cloud Shell** como terminal de Linux para ejecutar comandos de PowerShell.  
✅ No es necesario instalar nada en tu equipo.

### Opciones para acceder:
- Desde el **Azure Portal**.
- Desde el **inicio de sesión de Cloud Shell**.
- En situaciones reales, también puedes usar el terminal integrado en **Visual Studio Code**:
  - Menú: `Terminal > Nuevo terminal`
  - Selecciona `PowerShell` en el desplegable superior izquierdo.

---

## 🧩 Activación del espacio aislado

Antes de ejecutar comandos:
1. Asegúrate de que el **espacio aislado** esté activado.
2. En Cloud Shell (lado derecho de la pantalla), selecciona:
   - `Cambiar a PowerShell`
   - Luego, `Confirmar`

---

## 🧠 Comando para verificar la instalación

```powershell
$PSVersionTable

Este comando muestra una tabla con información sobre la instalación de PowerShell:

Propiedad	Valor ejemplo
PSVersion	7.3.6
PSEdition	Core
GitCommitId	7.3.6
OS	Linux Ubuntu
Platform	Unix
PSCompatibleVersions	{1.0, 2.0, 3.0, 4.0…}
PSRemotingProtocolVersion	2.3
SerializationVersion	1.1.0.1
WSManStackVersion	3.0
🔍 Esta salida parece una tabla, pero en realidad es un objeto. Esto permite acceder a propiedades específicas usando el operador punto (.).

🔎 Comando para ver solo la versión
powershell
$PSVersionTable.PSVersion
Salida esperada:

Major	Minor	Patch
7	3	6
Este comando accede directamente a la propiedad PSVersion del objeto $PSVersionTable.

🧠 Concepto clave
PowerShell trabaja con objetos, no solo texto. Esto permite acceder a propiedades específicas, filtrar datos y automatizar tareas de forma más precisa.

📌 Recomendación
Practica estos comandos en Cloud Shell o en el terminal de Visual Studio Code para familiarizarte con la estructura de salida y el uso de objetos.

