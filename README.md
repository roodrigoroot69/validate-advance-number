### EJERCICIO 2. Validación y Normalización Avanzada de Números de Teléfono
**Descripción**:
Tienes una lista de números de teléfono en diferentes formatos y debes validar y normalizar estos
números de teléfono al formato estándar internacional: +{country_code}{area_code}{local_number}.
Un número de teléfono válido debe cumplir con las siguientes reglas:

Debe comenzar con un signo más seguido del código de país.
Debe contener solo dígitos y opcionalmente espacios, guiones, o paréntesis que delimitan el área y el número local.

Debe seguir la longitud esperada según el código de país.
El formato de salida debe eliminar todos los espacios, guiones y paréntesis innecesarios y normalizar los números.

Longitud Esperada:
- +1 (Estados Unidos): 10 dígitos después del código de país.
- +44 (Reino Unido): 10 dígitos después del código de país.
- +91 (India): 10 dígitos después del código de país.
- +86 (China): 11 dígitos después del código de país.
- +49 (Alemania): 10 dígitos después del código de país.

*Ejemplo de entrada*:

```
phone_numbers = [
"+1 (234) 567-8901",
"+44 123 456 7890",
"+91-9876543210",
"+86 10 12345678",
"123-456-7890",
"+49 (0) 30 1234567"
]
```

```
Ejemplo de salida:
[
"+12345678901",
"+441234567890",
"+919876543210",
"+861012345678",
"Invalid",
"+49301234567"
]
```

*Nota:* Para el ejemplo del teléfono China hubo un error que se detecto al procesar y al ejemplo le falta un número.




