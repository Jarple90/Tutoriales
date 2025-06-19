"""
🔄 100 Continue
###¿Qué significa? El cliente ha enviado los encabezados (headers) y el servidor responde con "todo bien, puedes enviar el cuerpo de la solicitud".
###¿Cuándo se usa? En comunicaciones avanzadas donde se envía una petición grande (por ejemplo, un archivo enorme). Antes de mandar todo el contenido, el cliente puede decir: > “¿Está bien que te mande esto?”
###El servidor responde con 100 Continue, y el cliente dice: > “Perfecto, allá va el resto.”
###¿Lo necesitas tú? Probablemente no. En FastAPI y la mayoría de pruebas básicas con Thunder Client o Postman no se ve. Es más común en clientes HTTP de bajo nivel y cargas grandes con control fino del flujo.

✅ Códigos 2xx – Éxito
200 OK → Todo ha ido bien. Petición procesada correctamente (es el más común).

201 Created → Algo ha sido creado con éxito (por ejemplo, al usar POST).

204 No Content → Todo bien, pero no hay datos para devolver (útil con DELETE).

🔀 Códigos 3xx – Redirección
301 Moved Permanently → El recurso se ha movido a una nueva URL de forma permanente.

302 Found → Redirección temporal.

307 Temporary Redirect → Redirección temporal, pero el método (GET, POST, etc.) no cambia. Muy usado en APIs cuando se reubican temporalmente.

⚠️ Códigos 4xx – Error del cliente
400 Bad Request → El servidor no puede procesar la petición por formato incorrecto o datos inválidos.

401 Unauthorized → No has enviado credenciales válidas.

403 Forbidden → No tienes permiso para acceder, aunque estés autenticado.

404 Not Found → No se encuentra el recurso solicitado (el clásico).

405 Method Not Allowed → El recurso existe, pero ese verbo HTTP (GET, PUT, etc.) no está permitido.

422 Unprocessable Entity → El servidor ha recibido los datos, pero no puede validarlos. Muy común en FastAPI cuando el JSON no coincide con el modelo esperado.

🧨 Códigos 5xx – Error del servidor
500 Internal Server Error → Algo ha fallado dentro del servidor.

502 Bad Gateway → El servidor está actuando como “puerta de enlace” y ha recibido una respuesta inválida.

503 Service Unavailable → El servidor no puede responder temporalmente (quizás por mantenimiento o alta carga).

Piénsalo como un semáforo:

🟢 2xx = todo bien,

🟡 3xx = cambio de dirección,

🔴 4xx = culpa del cliente,

🔥 5xx = culpa del servidor.

"""