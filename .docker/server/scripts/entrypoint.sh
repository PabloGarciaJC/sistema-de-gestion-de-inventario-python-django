#!/bin/bash

## ---------------------------------------------------------
## Corregir permisos de todos los archivos root en /var/www/html
## ---------------------------------------------------------

echo "Corrigiendo permisos de archivos root..."
find /var/www/html -user root -exec sudo chown ${MY_USER}:${MY_GROUP} {} \; 2>/dev/null || true
echo "✓ Permisos corregidos"

## ---------------------------------------------------------
## Ejecutar comando principal
## ---------------------------------------------------------

exec "$@"
