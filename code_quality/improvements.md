# Mejoras aplicadas
## Convertir arreglos de usuarios y passwords a un hash
Esta mejora implica que esta información queda ligada en una misma estructura de datos, para evitar posteriores búsquedas por índice, y dar una respuesta más rápida. Se modifican todos los métodos para que siga dando la misma respuesta.
## Creación de métodos de acceso a variables internas
Esto se realiza para dar continuidad al acceso de las variables internas, simulando el comportamiento anterior con el uso de las nuevas estructuras de datos.
## Reutilización de métodos
Se re-utilizan los métodos creados cada vez que es posible para evitar redundancia de código fuente
## Convertir arreglo sessions a Hash
Esto al igual que el primer cambio, implica un acceso más eficiente a los datos almacenados (sin búsqueda). Se agregan métodos para poder acceder a la variable de la forma anterior.
